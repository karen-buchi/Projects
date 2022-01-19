import socket
import termcolor

def scan(target, port1, port2):
    print(termcolor.colored(f"\n Starting Scan For {target}", 'green'))
    diff = port2-port1
    if diff >= 30:
        print(termcolor.colored("Note: No output means all port scanned are closed", "green"))
        for port in range(port1, port2 + 1):
            scan_port(target, port)
    else:
        for port in range(port1, port2 + 1):
            scan2_port(target, port)



def scan_port(ipaddress, port):

    try:
        sock = socket.socket() #this is calling the socket function from the socket library
        sock.connect((ipaddress,port))
        print((f"[+] Port {port} is Opened"))
        sock.close()
    except :
        pass
        # print("Note: No output means all port scanned are closed")


def scan2_port(ipaddress, port):

    try:
        sock = socket.socket() #this is calling the socket function from the socket library
        sock.connect((ipaddress,port))
        print((f"[+] Port {port} is Opened"))
        sock.close()
    except :
        print(f'Port {port} is closed')

target = input('[*} Enter Target To Scan: ')
while True:
    pat_port = input('To Scan a Particular Port, Please Input "A", To Scan a Range of Ports, Please Input "B": ')
    if pat_port.upper() == "A":
        port = input('Please Input The Port To Scan: ')
        a = scan2_port(target, int(port.strip(" ")))
        break
    elif pat_port.upper() == "B":
        while True:
            ran = input('Please Input the range and separate by a "-": ')
            try:
                port_range = ran.split("-")
                range1 = int(port_range[0])
                range2 = int(port_range[1])
                scan(target, range1, range2)
                break
            except: continue
        break
    else:
        continue

# ports = int(input("[*] Enter How Many Ports You Want To Scan: "))


