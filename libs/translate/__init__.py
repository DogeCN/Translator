from difflib import SequenceMatcher
from .api import api_translate

class Result:
    top = False
    match = False
    online = False

    def __init__(self, word:str='', expect:list[str]=['' for i in range(12)]):
        self.word = word
        self.expect = expect
        #keys = ['phonetic','definition','translation','pos','collins','oxford','tag','bnc','frq','exchange','detail','audio']

    @property
    def translation(self):
        translation = self.expect[2]
        return translation if translation else '暂无翻译\nNone Translations'
    
    @translation.setter
    def translation(self, translation):
        self.expect[2] = translation

    def get_translation(self, lang):
        return self.definition if lang else self.translation

    @property
    def definition(self):
        return self.expect[1]

    @definition.setter
    def definition(self, definition):
        self.expect[1] = definition

    def get_definition(self, lang):
        return self.translation if lang else self.definition

    @property
    def detail(self):
        words = []
        results = []
        for form in self.expect[9].split('/'):
            if form:
                key, word = form.split(':')
                if key != '1' and word not in words and word != self:
                    words.append(word)
                    try: result = translate(word, results+[self])
                    except: continue
                    if result:
                        results.append(result)
        return results

    @property
    def info(self):
        return self.expect[0] #Phonetic
    
    def __bool__(self):
        return bool(self.expect[2]) and not self.match
    
    def __eq__(self, value):
        return self.word == value
    
    def get_tip(self, lang):
        trans_html = self.get_translation(lang).replace('\n', '<br>')
        htip = 'Do you mean %s: ' if lang else '你是否在找 %s: '
        return f'<html><body><p><span style=" font-size:11pt; font-weight:600;">{htip%self.word}</span style=" font-size:10pt"></p><p>{trans_html}</p></body></html>'

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
    letter = word[0].lower()
    for dictionary in dictionaries:
        if not dictionary.enabled: continue

        if letter.isalpha():
            if letter in dictionary:
                dict_letter = dictionary[letter]
            elif letter.isascii(): continue
            else:
                try: _word = api_translate(word, 1)
                except: return Result(word)
                result = translate(_word)
                result.match = True
                return result
        else:
            dict_letter = dictionary['#']

        if word in dict_letter:
            return Result(word, dict_letter[word])
        elif word.lower() in dict_letter:
            return Result(word.lower(), dict_letter[word.lower()])

    max = 0.3
    s = SequenceMatcher()
    s.set_seq2(word)
    for dictionary in dictionaries:
        if not dictionary.enabled: continue
        dict_letter = {}

        if letter.isalpha():
            if letter in dictionary:
                dict_letter = dictionary[letter]
        else:
            dict_letter = dictionary['#']

        if not dict_letter:
            for dict_letter in dictionary:
                pres, ratio = match(dict_letter, s)
                if pres and ratio > max:
                    max = ratio
                    result = pres
        else:
            result, _ = match(dict_letter, s)

    if result:
        result.match = True
    else:
        result = online_translate(word)
    return result

def match(dict_letter, s:SequenceMatcher):
    max = 0.3
    result = None
    for dict_key in dict_letter:
        s.set_seq1(dict_key)
        if s.real_quick_ratio() > max and s.quick_ratio() > max:
            ratio = s.ratio()
            if ratio > max:
                result = Result(dict_key, dict_letter[dict_key])
                max = ratio
    return result, max
