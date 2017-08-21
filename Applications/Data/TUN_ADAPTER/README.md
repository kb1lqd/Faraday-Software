# TUN/TAP Adapter Readme

Using TUN and TAP adapters is benificial to Faraday because it offers the opputunity for Faraday to interact with data streams as if it was a modem network interface. This allows Faraday to take advantage of already written protocols that expect a network interface and IP functionality.

A great example of this functionality is establishing a TCP link over Faraday utilizing OS tools already written.

Faraday likley only needs a TUN adapter (Layer 3) rather than a TAP adapter (Layer 2 / Ethernet).

## faradaytunserver.py

This TUN adapter program server when run connects to a local faraday device over the 'faraday-proxy' socket server. It uses the socket server functionality as a simple "wire" that replaces the Ethernet layer and is presented as a network adapter.

The TUN server utilizes 'faraday_send_tun.py' and 'faraday_receive_tun.py' to send and receive data to proxy socket.

### Basic Examples



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

This clearly shows the udp packet that was transmitted through Faraday