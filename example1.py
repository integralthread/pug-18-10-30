import re
from sh import ip 
is_interface = re.compile(r'[1-9]: [a-z0-9]*:')

def list_network_interfaces():
    print(ip.addr())   

def get_ip(interface):
    return ip.addr.show(interface)

def main():
    pass

if __name__ == '__main__':
    main()