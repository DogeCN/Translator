import requests
from urllib.parse import quote
import info

def api_translate(text:str, tl:int=0|1):
    url = info.url_trans%(['zh','en'][tl], quote(text))
    res = requests.get(url, timeout=5)
    return res.json()[0][0][0]
