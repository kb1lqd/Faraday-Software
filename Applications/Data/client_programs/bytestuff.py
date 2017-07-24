framing_startbyte = chr(0x7b)
framing_stopbyte = chr(0x7c)
framing_escapebyte = chr(0x7d)

def byte_escape_fixed_length(startbyte, stopbyte, escapebyte, packet):
    """
    This function byte stuffs a simple byte escape framing protocol around a provided data packet.
    Byte framing and escaping allows data to safely traverse the transmission medium with defined
    packet start and stop boundries for parsing.

    This function inputs a packet and returns a packet with escaped bytes per protocol inserted.
    """
    #If escapebyte is located in the payload insert the escape byte prior (Escape must be first or it'll add more than needed)
    packet = packet.replace(escapebyte, escapebyte + escapebyte)
    #If startbyte is located in the payload insert the escape byte prior
    packet = packet.replace(startbyte, escapebyte + startbyte)
    #If stopbyte is located in the payload insert the escape byte prior
    packet = packet.replace(stopbyte, escapebyte + stopbyte)
    #Insert start byte to the front of the payload
    packet = startbyte + packet
    #Insert stop byte to the end of the payload
    packet = packet + stopbyte
    return packet
