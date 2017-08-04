set txfilepath=test.txt
set /A fragmentsize = 56

txfile.py --filepath %txfilepath% | sendframe.py %fragmentsize%