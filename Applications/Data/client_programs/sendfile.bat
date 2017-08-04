set txfilepath=faraday.jpeg
set /A fragmentsize = 56

txfile.py --filepath %txfilepath% | sendframe.py %fragmentsize%