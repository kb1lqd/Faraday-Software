import fcntl
import os
import select
import struct

TUNSETIFF = 0x400454ca
TUNSETOWNER = TUNSETIFF + 2
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# Open file corresponding to the TUN device.
tun = open('/dev/net/tun', 'r+b')
ifr = struct.pack('16sH', 'tun0', IFF_TUN | IFF_NO_PI)
fcntl.ioctl(tun, TUNSETIFF, ifr)
fcntl.ioctl(tun, TUNSETOWNER, 1000)


os.system('ip addr add 192.168.90.1/32 dev tun0')
os.system('ip link set dev tun0 up')
os.system('ip route add 192.168.90.2/32 dev tun0')

raw_input("press enter to continue")

tun_fd = tun.fileno()

while True:
    read, write, exc = select.select([tun_fd,], [tun_fd,], [])

    for s in read:
        print os.read(s, 1500)
