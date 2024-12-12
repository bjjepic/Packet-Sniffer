# Packet sniffer

## What is this program?
This program was a tool I created after looking at a CyberSecOps roadmap and became interested, after using wireshark a few years back I decided to recap and centre this programs formatting to be a much lighter and bare bones version of wireshark.

Now, this program  catches, records and outputs network traffic (through the inputted network identifier)

Ideally, a end user should run this code and be met with all the traffic on their network, however there are a couple of things they might need to do in advance.


# Considerations

## Consideration #1
Change the network interface on the ``` sniffing('') ```

- ``` sniffing('Wi-fi') ```
- ``` sniffing('eth0') ```
- ``` sniffing('ethernet') ```

```
37 ┃      
38 ┃ # Calling the sniffing tool
39 ┃ sniffing('Enter Network Interface')

```


## Consideration #2

This script located in "Scapy test", is used to return to the user all the different network interfaces on the system

```
for iface in get_if_list():
    print(f"Interface: {iface}, MAC Address: {get_if_hwaddr(iface)}")
```
This is what a potential output will look like, you should take into consideration that any interface with the output "00:00:00:00:00:00" as the MAC address would be considered as a dud.

This means the only 2 addresses in this example are the first 2.
```
Interface: \Device\NPF_{xyz-xyz-xyz-xyz-xyz}, MAC Address: ue:93:30:12:d0:83 <--- ✓
Interface: \Device\NPF_{xyz-xyz-xyz-xyz-xyz}, MAC Address: lp:65:01:jp:l2:07 <--- ✓ 
Interface: \Device\NPF_{3A33F111-6464-4EF4-B26C-33AF7FA0AEE7}, MAC Address: 0a:00:00:00:00:00 <--- X
```

Once this is done take this passage of string and input it into the ```sniffing()``` with the letter "r" before the opening speech mark. 
```
sniffing(r'\Device\NPF_{xyz-xyz-xyz-xyz-xyz},')
```

