import os

prog_name = 'Translator'
prog_name_cn = '翻译器'
version = 'v1.14.7'
data_dir = os.getenv('AppData') + os.sep + prog_name + os.sep
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
dicts_dir = data_dir + 'dictionaries'  + os.sep
if not os.path.exists(dicts_dir):
    os.mkdir(dicts_dir)
ext_dict = '.tdf'
ext_tvf = '.tvf'
ext_all_tvf = '*' + ext_tvf
ext_self_exe = '.exe'
debug_file = data_dir + '.DEBUG'
debug = os.path.exists(debug_file)
api_timeout = 3
running = data_dir + 'running'
tools = 'tools'
default_tvf = data_dir + 'vocabulary' + ext_tvf
lang_setting = 'res/lang/setting.qm'
lang_zh = 'res/lang/zh.qm'
reg_ext = 'Software\\Classes\\' + ext_tvf
reg_cmd = 'shell\\open\\command'
url_repo = 'github.com/DogeCN/Translator'
url_trans = 'https://trans-api.dogecn.workers.dev/translate_a/single?client=gtx&dt=t&sl=auto&tl=%s&q=%s'
htip_hint = '<html><body><p><span style=" font-size:11pt; font-weight:600;">%s</span style=" font-size:10pt"></p><p>%s</p></body></html>'
match_hint = '<html><body style=" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; "><p>%s</p></body></html>'
log = data_dir + 'latest.log'
setting = data_dir + 'setting.tsf'
public = data_dir + 'public.data'
temp = data_dir + 'temp'
nontr = ('暂无翻译', 'None Translations')
dnames = ('Base', 'Long', 'Phrase', 'Proper', 'Term')
durl = 'https://raw.githubusercontent.com/DogeCN/Translator/refs/heads/main/dictionaries/%s'
durl_cn = 'https://ghproxy.cn/' + durl

Tr = {
    'load' : ('载入单词表', 'Load Vocubulary File'),
    'save_as' : ('保存单词表', 'Save Vocubulary File'),
    'warning' : ('警告', 'Warning'),
    'translate_function_unavailable' : (
        '''无法加载字典
翻译功能不可用
但你可以浏览已有词汇
(首次使用需连接互联网)''',
        '''Can't load dictionaries.
Although the translate function is unavailable,
you can read existed vocabularies.
(Internet connection required for the first use)'''
        ),
    'correct_hint' : ('双击更正', 'Double Click to Correct'),
    'speech_hint' : ('双击朗读', 'Double Click to Speech Out'),
    'default_file' : ('选择默认单词表', 'Choose The Default Vocabulary File'),
    'htip' : ('你是否在找 %s: ', 'Do you mean %s: '),
}

StlSheets = {
    'tmenu' : 'border-radius:5px;',
    'raw' : 'background-color: rgb(30, 30, 30);'
}

UITr = {
    prog_name : prog_name_cn,
    'Setting' : '设置',
    'Language' : '语言',
    'Auto Save' : '自动保存',
    'Top' : '置顶',
    'Files' : '文件',
    'Delete' : '删除',
    'Vocabulary' : '词汇表',
    'Secs' : '秒',
    'Add' : '添加',
    'Hotkeys' : '快捷键',
    'Translate' : '翻译器',
    'Word Entry' : '输入框',
    'Enter a word' : '请输入单词',
    'Add into Vocabulary' : '加入单词表',
    'Vocabulary Bank' : '词汇表',
    'Translations' : '翻译',
    'Top the Words' : '置顶单词',
    'Delete the Words' : '删除已选单词',
    'Detail' : '变形',
    'Infomations' : '信息',
    'File' : '文件',
    'Tools' : '工具',
    'Settings' : '设置',
    'About' : '关于',
    'Dicts' : '字典',
    'Reload' : '重载',
    'Reload File' : '重载文件',
    'Save' : '保存',
    'Save File' : '保存文件',
    'Load' : '载入',
    'Load Files' : '加载文件',
    'Save As' : '另存为',
    'Save File As ...' : '另存为...',
    'Clear' : '清除',
    'Clear Files' : '清除所有文件',
    'Exit' : '退出',
    'About This Programm' : '关于本项目',
    'About Qt' : '关于Qt',
    'About Qt Engine' : '关于Qt引擎',
    'Relaod Tools' : '重载工具',
    'Reload Dictionaries' : '重载字典',
    'Remove' : '移除',
    'Remove Current File' : '移除当前文件',
    'New' : '新建',
    'Create a New File' : '新建文件',
    'Save All' : '全部保存',
    'Save All Files' : '保存所有文件',
    'Online' : '在线',
    'Online Mode' : '在线模式'
}
