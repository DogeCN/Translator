import os

prog_name = 'Translator'
version = 'v1.14.6'
data_dir = os.getenv('AppData') + os.sep + prog_name + os.sep
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
debug = data_dir + '.DEBUG'
running = data_dir + 'running'
tools = 'tools'
dicts = data_dir + 'dictionaries'
if not os.path.exists(dicts):
    os.mkdir(dicts)
lang_setting = 'res/lang/setting.qm'
lang_zh = 'res/lang/zh.qm'
root = './'
ext_dict = '.tdf'
ext_tvf = '.tvf'
ext_all_tvf = '*' + ext_tvf
ext_self_exe = '*.exe'
reg_ext = 'Software\\Classes\\' + ext_tvf
reg_cmd = 'shell\\open\\command'
url_repo = 'github.com/DogeCN/Translator'
url_trans = 'https://trans-api.hark2009lbf.workers.dev/translate_a/single?client=gtx&dt=t&sl=auto&tl=%s&q=%s'
htip_hint = '<html><body><p><span style=" font-size:11pt; font-weight:600;">%s</span style=" font-size:10pt"></p><p>%s</p></body></html>'
match_hint = '<html><body style=" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; "><p>%s</p></body></html>'
log = data_dir + 'latest.log'
setting = data_dir + 'setting.tsf'
temp = data_dir + 'temp'
nontr = ('暂无翻译', 'None Translations')

Tr = {
    'load' : ('载入单词表', 'Load Vocubulary File'),
    'save_as' : ('保存单词表', 'Save Vocubulary File'),
    'warning' : ('警告', 'Warning'),
    'translate_function_unavailable' : (
        '''无法加载字典
翻译功能不可用
但你可以浏览已有词汇''',
        '''Can't load dictionaries.
Although the translate function is unavailable,
you can read existed vocabularies.'''
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
    'Translator' : '翻译器',
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
    'Translation' : '翻译',
    'Top the Word' : '置顶单词',
    'Delete the Word' : '删除已选单词',
    'Detail' : '变形',
    'Infomation' : '信息',
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
    'Load File' : '加载文件',
    'Save As' : '另存为',
    'Save File As ...' : '另存为...',
    'Clear' : '清除',
    'Clear File' : '清除所有文件',
    'Exit' : '退出',
    'About This Programm' : '关于本项目',
    'About Qt' : '关于Qt',
    'About Qt Engine' : '关于Qt引擎',
    'Relaod Tool' : '重载工具',
    'Reload Dictionariy' : '重载字典',
    'Remove' : '移除',
    'Remove Current File' : '移除当前文件',
    'New' : '新建',
    'Create a New File' : '新建文件',
    'Save All' : '全部保存',
    'Save All File' : '保存所有文件',
    'Online' : '在线',
    'Online Mode' : '在线模式'
}