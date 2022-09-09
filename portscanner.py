from queue import Queue
import socket
import threading
from IPy import IP
import optparse
import time
import sys
import os



class colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKORANGE = '\033[38;5;208m'

# target = input("Enter Target:")
# proxy_ip = input("Enter a Proxy IP:")#'94.245.56.147'

def getarguments():

    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target" ,help="target/host to scan")
    parser.add_option("-p", "--proxy", dest="proxy_ip" ,help="proxy ip address and port number")
    parser.add_option("-m", "--mode", dest="mode" ,type="int" ,help="Enter the scanning mode: [1]:Scan PORT 1-1024, [2]:Scan PORT 1-48128, [3]:Scan Only Important Port(Fast Scanning), [4]:Custom(Range), [5]:Custom(Specific) PORT, [6]:Full Scan(All Ports)")
    parser.add_option("-T", "--threads", dest="threads" ,type="int" ,help="number of threads")
    parser.add_option("-V", "--verbose mode", dest="verbose",action="store_true",help="print all results")
    (option, argument) = parser.parse_args()
    if not option.target:
        parser.error(colors.WARNING+"[-] Please specify the target ip or host name. use --help for more information."+colors.ENDC)
    # elif not option.proxy_ip:
    #     parser.error(colors.WARNING+"[-] Please specify proxy ip. use --help for more information."+colors.ENDC)
    elif not option.mode:
        parser.error(colors.WARNING+"[-] Please specify scanning mode. use --help for more information."+colors.ENDC)
    elif not option.threads:
        parser.error(colors.WARNING+"[-] Please specify number of threads. use --help for more information."+colors.ENDC)
    
    else:
        return option

print(colors.OKGREEN,colors.BOLD,"""
 
░█████╗░██████╗░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║░░██║╚██╗░██╔╝██╔══██╗
███████║██║░░██║██████╔╝██║╚█████╗░███████║░╚████╔╝░███████║
██╔══██║██║░░██║██╔══██╗██║░╚═══██╗██╔══██║░░╚██╔╝░░██╔══██║
██║░░██║██████╔╝██║░░██║██║██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

████████████████████████████████████████████████████████████████████████
█▄─▄▄─█─▄▄─█▄─▄▄▀█─▄─▄─███─▄▄▄▄█─▄▄▄─██▀▄─██▄─▀█▄─▄█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀█
██─▄▄▄█─██─██─▄─▄███─█████▄▄▄▄─█─███▀██─▀─███─█▄▀─███─█▄▀─███─▄█▀██─▄─▄█
▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
                                                                
                                                         @kartikhunt3r


""",colors.ENDC)

queue = Queue()
open_ports = []

option = getarguments()

def get_banner(s):
    s.recv(1024)

def check_ip(ip):
    try:
        IP(ip)
        target = ip
        return target
    except ValueError:
        target = socket.gethostbyname(ip)
        return target

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((check_ip(target), port))
        # sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        # sock.sendto(("Host: " + proxy_ip + "\r\n\r\n").encode('ascii'), (target, port))
        return sock
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range(1, 1025):
            queue.put(port)
       
    elif mode == 2:
        for port in range(1, 48129):
            queue.put(port)
       
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
       

    elif mode == 4:
        start = int(input(colors.OKBLUE+"Enter starting port: "+colors.ENDC))
        end = int(input(colors.OKBLUE+"Enter ending port: "+colors.ENDC))
        for port in range(start, end):
            queue.put(port)
  

    elif mode == 5:
        ports = input(colors.OKBLUE+"Enter your ports (seperate by blank): "+colors.ENDC)
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)
      
    
    elif mode == 6:
        for port in range(1, 65535):
            queue.put(port)
      
        

def worker():
    while not queue.empty():
        port = queue.get()
        config = portscan(port)
        if config:
            # try:
            #     banner = get_banner(config)
            #     print(colors.OKORANGE,colors.BOLD,"[+] Port {} is open!".format(port)+' : '+str(banner.decode().stip('\n')))
             
            # except:
            print(colors.OKORANGE,colors.BOLD,"[+] Port {} is open!".format(port))
            open_ports.append(port)
        else:
            if verbose:
                print(colors.FAIL,colors.BOLD,"[-] Port {} is closed!".format(port))

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for thread in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(colors.OKGREEN,"[+] Open ports are:", open_ports)


mode = option.mode
threads = option.threads
target=option.target
proxy_ip=option.proxy_ip
verbose=option.verbose
run_scanner(threads, mode)



