import re
from sh import ip 
from sh import keybase

is_interface = re.compile(r'[1-9]: [a-z0-9]*:')

def list_network_interfaces():   
    for line in ip.addr().split('\n'):
        if is_interface.match(line):
            interface = line.split(':')[1].strip()
            yield interface
        elif line.strip().startswith('inet '):
            yield '**{ip}**'.format(ip=line.split()[1])

def get_ip(interface):
    return ip.addr.show(interface)

def main():
    edwin = "mcguffinn"
    result = get_ip('docker0')
    print(dir(result))

    # inspect cmd
    print(result.cmd, result.exit_code)


    keybase.chat.send(edwin, 'Interface docker0')
    keybase.chat.send(edwin, str(result))

    for line in list_network_interfaces():
        keybase.chat.send(edwin, line)


if __name__ == '__main__':
    main()