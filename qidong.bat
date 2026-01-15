@echo off
ping -n 1 www.hao123.com > nul 2>&1
if %errorlevel%==1 (
    echo 未检测到网络连接，尝试连接校园网...
    python C:\Users\ZHOU CHENDI\Desktop\py\电信网.py
) else (
    echo 网络连接正常，无需操作.
)