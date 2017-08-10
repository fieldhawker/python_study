rem ココカラ
@echo off
::: 実行前の準備
set EXEC_DIR=%~dp0

::: python
PATH=C:\Users\bp-takano\AppData\Local\Programs\Python\Python36-32;C:\Users\bp-takano\AppData\Local\Programs\Python\Python36-32\Scripts;%PATH%

cd %EXEC_DIR%
PROMPT #$S

%ComSpec%
rem ココマデ