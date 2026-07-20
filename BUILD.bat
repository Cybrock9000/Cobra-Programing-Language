@echo off
REM ===== Build Language with Nuitka =====

python -m nuitka --onefile --windows-disable-console compiler.py --enable-plugin=tk-inter

echo.
echo Build finished!
pause
