# Packet sniffer (Back under development)

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

## Consideration #3 (Downloads)



# - https://npcap.com/

![](https://media.discordapp.net/attachments/922264436767588352/1316943232331939930/image.png?ex=675ce276&is=675b90f6&hm=f080d9c9b029a58ae3bbca21dfdea51ef74542737a5e6e4a6a3651f5cf73ba51&=&format=webp&quality=lossless&width=752&height=671 "download page from npcaps website")

"Npcap is able to sniff loopback packets (transmissions between services on the same machine) by using the Windows Filtering Platform (WFP)."

In simpler terms to understand this is what we're going to use to help capture the information to output.

Please ensure that Scapy and Npcap is downloaded prior to operating this program.

# - Installing scapy
![Alt text](https://media.discordapp.net/attachments/1190043394395873412/1316945836810174535/image.png?ex=675ce4e3&is=675b9363&hm=6afe068067f3309c91738de3c3696e45d6e60bc2a44aec836e8aa57783b62f59&=&format=webp&quality=lossless "Screenshot of me downloading (already downloaded) scapy" )

Enter this command into terminal, ```pip install scapy``` (ensure python 3.12+ is installed and added to path)

