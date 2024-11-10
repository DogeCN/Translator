from difflib import SequenceMatcher
from .api import api_translate
import info

class Result:
    top = False
    match = False
    online = False

    def __init__(self, word:str='', value:list[str, list[str]]=[*['']*3, []]):
        self.word = word
        self.value = value

    @property
    def translation(self):
        translation = self.value[2]
        return translation if translation else info.nontr[0]
    
    @translation.setter
    def translation(self, translation):
        self.value[2] = translation

    def get_translation(self, lang):
        return self.definition if lang else self.translation

    @property
    def definition(self):
        definition = self.value[1]
        return definition if definition else info.nontr[1]

    @definition.setter
    def definition(self, definition):
        self.value[1] = definition

    def get_definition(self, lang):
        return self.translation if lang else self.definition

    @property
    def exchanges(self):
        results = []
        for form in self.value[3]:
            result = translate(form)
            if result:
                results.append(result)
        return results

    @property
    def phonetic(self):
        return self.value[0]
    
    def __bool__(self):
        return bool(self.value[2]) and not self.match
    
    def __eq__(self, value):
        return self.word == value
    
    def get_tip(self, lang):
        trans_html = self.get_translation(lang).replace('\n', '<br>')
        return info.htip_hint % (info.Tr['htip'][lang] % self.word, trans_html)

def fast(func):
    def wrapper(word: str, Results: list[Result] = []) -> Result:
        for result in Results:
            if result == word:
                return result
        return func(word)
    return wrapper

@fast
def online_translate(word: str) -> Result:
    result = Result(word)
    try: result.translation = api_translate(word, 0)
    except: ...
    else: result.online = True
    return result

@fast
def translate(word: str) -> Result:
    from .dict import dictionaries
    max = 0.3
    s = SequenceMatcher()
    s.set_seq2(word)
    result = None
    for dictionary in dictionaries:
        if not dictionary.enabled: continue
        for wp in [word, word.lower(), word.capitalize()]:
            if wp in dictionary:
                return Result(word, dictionary[wp])

        for wm in dictionary:
            if wm[0] == word[0]:
                s.set_seq1(wm)
                if s.real_quick_ratio() > max and s.quick_ratio() > max:
                    ratio = s.ratio()
                    if ratio > max:
                        result = Result(wm, dictionary[wm])
                        max = ratio

    if result is not None:
        result.match = True
        return result
    else:
        return Result(word)
