import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from tanu import iAmMain
 
        iAmMain().iAmMenu()
 
 
 
elif bit == "32bit":
 
        from tanu import iAmMain
 
 
        iAmMain().iAmMenu()
 
 
 
