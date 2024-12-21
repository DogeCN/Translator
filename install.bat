@echo off
pyinstaller --noconfirm --onefile --windowed --icon ".source\icon.ico" --optimize "2" --disable-windowed-traceback  "main.py"
del "dist\Plume Lexicon.exe"
ren dist\main.exe "Plume Lexicon.exe"
echo 20000 INFO: Plume Lexicon.exe Completed.
