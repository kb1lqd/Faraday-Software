# TUN/TAP Adapter Readme

Using TUN and TAP adapters is benificial to Faraday because it offers the opputunity for Faraday to interact with data streams as if it was a modem network interface. This allows Faraday to take advantage of already written protocols that expect a network interface and IP functionality.

A great example of this functionality is establishing a TCP link over Faraday utilizing OS tools already written.

Faraday likley only needs a TUN adapter (Layer 3) rather than a TAP adapter (Layer 2 / Ethernet).

## faradaytunserver.py

This TUN adapter program server when run connects to a local faraday device over the 'faraday-proxy' socket server. It uses the socket server functionality as a simple "wire" that replaces the Ethernet layer and is presented as a network adapter.

The TUN server utilizes 'faraday_send_tun.py' and 'faraday_receive_tun.py' to send and receive data to proxy socket.

### Basic Examples

### UDP

To send a quick text string and recieve it AS SENT through two Farsday's:
* Start the Faraday TUN server
* Run 'faraday_receive_tun.py' in a seperate terminal (it will print data)

``` bash
echo "Testing 0123456789" > /dev/udp/'192.168.90.2'/8000
```

This produces the output on the receiver as:

``` bash
brent@brent-VirtualBox:~/Documents/github_brent_faraday_software/tunadapter/Faraday-Software/Applications/Data/TUN_ADAPTER$ python faraday_receive_tun.py 
E/�&@@SC��Z��Z��@�Testing 0123456789

```

This clearly shows the udp packet that was transmitted through Faraday when comparing to hte UDP expected frame format.

#### TCP

Using the simple python socket client example that tries to establish a TCP connection to a server through tun0 (192.168.90.2):

```bash
brent@brent-VirtualBox:~/Documents/github_brent_faraday_software/tunadapter/Faraday-Software/Applications/Data/TUN_ADAPTER$ python tcp_tun_test.py 
connecting to 192.168.90.2 port 10000
```

Although I have not yet established a connection through Faraday I can see the RAW TCP data trying to connect! This means that it will be possible to use TCP as a transport layer protocol!

Farday is actually transmitting and receiving these packets.

(Note that I changed the print output to use repr() below...)

``` bash
brent@brent-VirtualBox:~/Documents/github_brent_faraday_software/tunadapter/Faraday-Software/Applications/Data/TUN_ADAPTER$ python faraday_receive_tun.py 
"E\x00\x00<L\x80@\x00@\x06\xb8\xe7\xc0\xa8Z\x01\xc0\xa8Z\x02\xea\x8a'\x10\xc3\xed\xf9\xbd\x00\x00\x00\x00\xa0\x02\x14\x00\x83\xbd\x00"
'\x00\x02\x04\x01\x00\x04\x02\x08\n$c\x8b\xf8\x00\x00\x00\x00\x01\x03\x03\x07'
"E\x00\x00<L\x81@\x00@\x06\xb8\xe6\xc0\xa8Z\x01\xc0\xa8Z\x02\xea\x8a'\x10\xc3\xed\xf9\xbd\x00\x00\x00\x00\xa0\x02\x14\x00\x81\xc5\x00"
'\x00\x02\x04\x01\x00\x04\x02\x08\n$c\x8d\xf0\x00\x00\x00\x00\x01\x03\x03\x07'
"E\x00\x00<L\x82@\x00@\x06\xb8\xe5\xc0\xa8Z\x01\xc0\xa8Z\x02\xea\x8a'\x10\xc3\xed\xf9\xbd\x00\x00\x00\x00\xa0\x02\x14\x00}\xbd\x00"
'\x00\x02\x04\x01\x00\x04\x02\x08\n$c\x91\xf8\x00\x00\x00\x00\x01\x03\x03\x07'
```