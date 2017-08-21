# TUN/TAP Adapter Readme

Using TUN and TAP adapters is benificial to Faraday because it offers the opputunity for Faraday to interact with data streams as if it was a modem network interface. This allows Faraday to take advantage of already written protocols that expect a network interface and IP functionality.

A great example of this functionality is establishing a TCP link over Faraday utilizing OS tools already written.

Faraday likley only needs a TUN adapter (Layer 3) rather than a TAP adapter (Layer 2 / Ethernet).

## TunTest1 Program

This TUN adapter program provides a simple test to

* create a TUN