@echo off
:: Windows batch wrapper for password generator
:: Usage: passgen.bat [-n NUM] [-l LENGTH] [-s]

python "%~dp0password_gen.py" %*
