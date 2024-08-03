Translator = 'v1.14.5'
Tools = 'v0.27'

Readme_zh = fr'''
Translator(翻译器) {Translator}
这是一个简单的本地翻译系统

背景故事:
我之前读《4000 Essential Words》时遇到生词只能手抄，不仅难以归纳整理，意思也可能不全，所以就打算开发一个翻译器+单词本。
想起当初加载词典都要半天，到现在可以流畅翻译，修正勘误，批量操作，打印成册，我的开发能力也大大增强了。
我在反复测试程序中，不知不觉间积累了300多个词汇，感谢它和Python社区三个多月的陪伴！

用途说明:
本项目主要通过本地词典进行英译中，主要用于翻译单词，存入单词本并打印；
中译英或开启在线模式时通过Google在线翻译并由Cloudfare提供节点加速(不过在国内还是被墙了)。
翻译时会优先从当前文件的单词中查找，本地和在线翻译有背景色区分。
如无开启自动保存，未保存文件在关闭程序时将直接舍弃，请养成顺手保存的良好习惯。
设置文件在"%AppData%\setting.tsf"，删除可恢复默认设置。
所有文件都由pickle保存并由zlib压缩，tvf(单词本文件)支持传参启动，单实例运行。
tools文件夹中提供了一些示例插件，目前插件系统还算完善，可加载各类importlib能识别的Python文件。
程序如非正常退出，下一次可能启动失败，再次启动即可。

如出现Bug，请尽量复现并联系我。
也欢迎您提出宝贵的意见，或编写一些有趣的插件。
需要获得完整开发文件也请联系。
作者QQ: Doge(3269515690)
'''

Readme_en = fr'''
Translator {Translator}
Simple locale translation tool at your service.

Backstory:
In my quest of "4000 Essential Words," I grappled with unfamiliar terms that were hard to comprehend and summarize. Hence, the idea for this app blossomed.
I recallimg the torturous dictionary loading phase but today, everything's smooth sailing: correcting errors, batch processing, even printing them out. A notable enhancement indeed!
Along the way, countless words swimming around in my head—more than 300, to be precise. Thanks for sticking with me these past few months! And also supports from community.

How to Use:
This project primarily uses the local dictionary for English-Chinese translation, focusing on word translation, saving, and printing.
For Chinese-English translation or online mode, we rely on Google Online Translate and Cloudfare (currently inaccessible in China).
Translation prioritizes current document words, with different background colors for offline/online translations.
Automatic saving off? Closing the program discards unsaved files. Remember to hit 'Save' often!
Settings file is located at "%25 AppData\settings.tsf". Delete to revert to defaults.
Files are stored using pickle and zlib compression, with TVF (word book file) supporting parameter transfer startup and single-instance operation.
A handful of sample plugins reside in the tools folder. The plugin system is comprehensive, allowing for Python files recognized by importlib to be loaded.
Abnormal exit might result in failure to restart.

Bug reports are appreciated.
Feel free to suggest improvements or contribute your own plugins.
Requiments for a full view of the project files are also welcome.
Author's QQ: Doge(3269515690)
'''