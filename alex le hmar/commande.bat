@echo off
title Alerte Calculatrice
echo Preparation du chaos...
pause

:: La boucle qui lance 1000 instances
for /L %%i in (1,1,1000) do (
    start calc.exe
)

echo Operation terminee. Bonne chance pour tout fermer !
pause