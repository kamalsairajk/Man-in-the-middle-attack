# Man-in-the-middle-attack

The technique we have used for performing man in the middle attack is ARP poisoning
which is one of the most effective strategy to perform man in the middle attack. The
insecure nature of the ARP protocol is used in poisoning . Devices using ARP will
accept updates at any time which is disadvantageous as unlike protocols such as DNS
that can be configured to only accept secured dynamic updates. This simply means
that any device can send an ARP reply packet to another host and force that host to
update its ARP cache with the new value. Sending a gratuitous ARP means sending
an ARP reply when no request has been generated . Few well placed gratuitous ARP packets 
which are present with malicious intent would result in hosts who think they
are communicating with one host, but in reality are communicating with a listening
attacker. An attempt which is undetectable to the user is an effective ARP poisoning
attempt. ARP poisoning is very effective against wireless networks. By starting an
ARP poisoning attack which can further lead to being man in the middle attack,
hackers can steal highly-sensitive data from the targeted computers In this attack
attackers machine send ARP spoofed packets to victims machine using python scapy
script, IP address and the network gateway of the wireless interface, which makes the
victim think that attacker machine is the router and also send ARP spoof packets to
router to make it think that the attacker machine is the victim. This poisons the ARP
table of the victims machine and router. After the script is run then attacker can use
packet capturing tools like Wireshark to capture any packet of the victim.
