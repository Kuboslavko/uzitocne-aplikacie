@echo off
title kalkulacka
echo Vitej v kalkulacce. 
set /p prve=Zadaj prve cislo:
set /p druhe=Zadaj druhe cislo:
echo.
echo Dakujem za zadanie cisel. :-)
set /a sucet=%prve%+%druhe%
set /a rozdiel=%prve%-%druhe%
set /a sucin=%prve%*%druhe%
set /a podiel =%prve%/%druhe%
echo.
echo %prve%+%druhe% je %sucet%
echo %prve%-%druhe% je %rozdiel%
echo %prve%*%druhe% je %sucin%
echo %prve%/%druhe% je %podiel%
pause
exit