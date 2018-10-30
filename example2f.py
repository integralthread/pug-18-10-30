import re
from sh import curl
from sh import keybase 
from sh import rsync
from sh import mkdir 
from sh import eog #eye of gnome

edwin = "mcguffinn"

def public_ip():
    ip = str(curl('wtfismyip.com/text')).strip()
    keybase.chat.send(edwin, 'My Public IP: {}'.format(ip))

def cache_jpg():
    cache_dir = "/home/mt/dev/integralthread/pug-18-10-30/cache"
    mkdir('-p', cache_dir)
    rsync('-avm', '--include="*.jpg"',"/home/mt/Pictures", cache_dir)
    keybase.chat.send(edwin, "done caching jpgs")

def guido():
    g = '/home/mt/Pictures/guido.jpg'
    keybase.chat.upload('--title', 'GUIDO', '--exploding-lifetime', '30s', edwin, g)

def main():
    public_ip()    
    cache_jpg()
    guido()

if __name__ == '__main__':
    main()