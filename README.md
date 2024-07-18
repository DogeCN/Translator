# Translator
**A simple locale translation tool at your service.**

### Backstory
 In my quest of *4000 Essential Words* , I grappled with unfamiliar terms that were hard to comprehend and summarize. Hence, the idea for this app blossomed.
 I recallimg the torturous dictionary loading phase but today, everything's smooth sailing: correcting errors, batch processing, even printing them out. A notable enhancement indeed!
 Along the way, countless words swimming around in my head——more than 300, to be precise. Thanks for sticking with me these past few months! And also supports from community.

### How to Use
 This project is mainly using PySide6 to create user interface.
 It primarily uses the local dictionary for English-Chinese translation, focusing on word translation, saving, and printing.
 For Chinese-English translation or online mode, we rely on Google Online Translate and Cloudfare (currently inaccessible in China).
 Translation prioritizes current document words, with different background colors for offline/online translations.
 Automatic saving off? Closing the program discards unsaved files. Remember to hit 'Save' often!
 Settings file is located at **%25 AppData\settings.tsf**. Delete to revert to defaults.
 Files are stored using pickle and zlib compression, with TVF (word book file) supporting parameter transfer startup and single-instance operation.
 A handful of sample plugins reside in the tools folder. The plugin system is comprehensive, allowing for Python files recognized by importlib to be loaded.
