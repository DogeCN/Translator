import requests
from urllib.parse import quote
from libs.io.base import load

ustr = load('res/url.s')

def api_translate(text:str, tl:int=0|1):
    url = ustr%(['zh','en'][tl], quote(text))
    res = requests.get(url, timeout=5)
    return res.json()[0][0][0]
