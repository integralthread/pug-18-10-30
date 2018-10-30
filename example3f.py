import errno
from sh import curl
from sh import keybase 
from sh import tail #eye of gnome
from sh import logger

edwin = "mcguffinn"
upload = keybase.bake('chat', 'upload', '--exploding-lifetime', '30s', '--title')
send   = keybase.bake('chat', 'send', '--exploding-lifetime', '30s')

def guido_baked():
    g = '/home/mt/Pictures/guido.jpg'
    upload('GUIDO Baked', edwin, g)

def tailer():
    for line in tail("-f", "/var/log/syslog", _iter=True):
        send(edwin, line)
        
def main():
    guido_baked()
    tailer()

if __name__ == '__main__':
    main()