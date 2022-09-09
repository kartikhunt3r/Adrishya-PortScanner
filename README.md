# Adrishya-PortScanner
A fast port scanner with proxy support. written in python.

![Logo](https://github.com/kartikhunt3r/MacChanger/blob/main/logo.gif)

## Features

- proxy support which protacts your identity while scanning the host
- customizable threading options
- faster than Nmap scan
- customizable scanning options: 
     - 1:Scan PORT 1-1024
     - 2:Scan PORT 1-48128
     - 3:Scan Only Important Port(Fast Scanning)
     - 4:Custom(Range)
     - 5:Custom(Specific) PORT
     - 6:Full Scan(All Ports)
- verbose output 

## Demo:



## Installation:


```bash
git clone https://github.com/kartikhunt3r/Adrishya-PortScanner.git

cd Adrishya-PortScanner

chmod +x *

pip install -r requirements.txt

python3 portscanner.py -h
```


## Use:


```bash
python3 portscanner.py -t scanme.nmap.org -m 1 -T 30      

```

## Options:


```bash

Usage: portscanner.py [options]

Options:
  -h, --help            show this help message and exit
  -t TARGET, --target=TARGET
                        target/host to scan
  -p PROXY_IP, --proxy=PROXY_IP
                        proxy ip address and port number
  -m MODE, --mode=MODE  Enter the scanning mode: [1]:Scan PORT 1-1024,
                        [2]:Scan PORT 1-48128, [3]:Scan Only Important
                        Port(Fast Scanning), [4]:Custom(Range),
                        [5]:Custom(Specific) PORT, [6]:Full Scan(All Ports)
  -T THREADS, --threads=THREADS
                        number of threads
  -V, --verbose mode    print all results
  
    
```


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://kartiksavaliya.tech/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/kartikhunt3r)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/kartikhunt3r)

[![youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCqUKMBA2UPqKOYbSa9FnC-Q)
















