```md
# Pypacker Documentation

Pypacker is a Python library designed for crafting, parsing, and analyzing network packets. It supports a variety of network protocols and provides a flexible and efficient framework for handling raw packet data, making it a valuable tool for network engineers, researchers, and developers involved in network programming and security.

---

## Conceptual Introduction

### Domain Concepts

- **Network Packet:** A formatted unit of data carried by a packet-switched network. Pypacker allows creation, parsing, and manipulation of these packets.
- **Protocols Supported:** Pypacker supports multiple network protocols including Ethernet, IP (IPv4/IPv6), TCP, UDP, ICMP, ARP, and many others.
- **Packet Layers:** Network packets have layered structures (e.g., Ethernet frame containing an IP packet which contains a TCP segment). Pypacker models these layers as Python classes that can be stacked or nested.
- **Parsing:** Conversion of raw byte streams into structured packet objects.
- **Crafting:** Building packet objects from scratch or partial data and serializing them to bytes for transmission.
- **Sniffing & Injection:** Capabilities for capturing network traffic and injecting crafted packets into the network (where privileges and environment permit).

### Mapping to API Terms

- Each supported protocol is represented as a Python class (e.g., `Ethernet`, `IP`, `TCP`).
- Packet parsing is performed via constructors that accept raw data bytes and produce layered packet objects.
- Packet construction is done by instantiating packet layers, setting fields, and serializing.
- Utility functions are provided for tasks such as checksum calculation and field guessing.
- Sniffing and injection APIs wrap OS-level packet capture and sending functionality.

---

## Execution Facts

### Core Classes and Functions

| API Element           | Inputs                                      | Outputs                        | Errors / Side Effects                                       | Defaults / Constraints                      |
|-----------------------|---------------------------------------------|--------------------------------|-------------------------------------------------------------|---------------------------------------------|
| `Ethernet(raw_bytes=None, payload=None)`  | Raw bytes or payload layer         | Ethernet layer object            | Parses Ethernet frame; throws on malformed data              | Defaults empty header; auto-calculates fields|
| `IP(raw_bytes=None, payload=None)`        | Raw bytes or payload layer         | IPv4 packet object               | Parses IPv4 header, validates checksum; errors if invalid    | Supports options like fragmentation fields  |
| `TCP(raw_bytes=None, payload=None)`       | Raw bytes or payload layer         | TCP segment object              | Parses TCP header; validates ports and flags                  | Handles options and flags                     |
| `UDP(raw_bytes=None, payload=None)`       | Raw bytes or payload layer         | UDP datagram object            | Parses UDP header; minimal validation                         | Minimal header size; checksum optional       |
| `parse_packet(raw_bytes)`                  | Raw bytes                        | Fully layered packet object    | Entry point for parsing raw packet bytes into nested layers   | Auto-detects protocols if possible           |
| `serialize(packet_obj)`                     | Packet object                    | Raw bytes                     | Serializes packet object including all layers into bytes      | Handles proper byte order and padding         |

### Sniffing and Injection

| API Element               | Inputs                      | Outputs                    | Errors / Side Effects                                   | Constraints / Notes                         |
|---------------------------|-----------------------------|----------------------------|--------------------------------------------------------|---------------------------------------------|
| `sniff(iface, count, timeout, filter)` | Interface name, packet count, timeout, BPF filter string | Generator of parsed packet objects | Captures live packets from network interface | Requires privileges; depends on libpcap/tcpdump |
| `inject(packet_obj, iface)`              | Packet object and interface | None                       | Sends raw packet bytes on network interface             | Requires root/admin privileges               |

### Utility Functions

- `calc_checksum(packet_layer)`: Calculates and returns checksum for a given protocol layer.
- `guess_packet_type(raw_bytes)`: Attempts to identify packet type from raw bytes for parsing guidance.

### Constraints

- Works primarily on Linux and UNIX-like systems; limited Windows support.
- Requires appropriate permissions (usually root/admin) for sniffing and injection.
- Packet crafting requires careful understanding of protocol details for validity.
- Performance depends on packet sizes and counts, suitable for moderate use.

---

## API Usage Patterns

### Pattern 1: Parsing Raw Packets

#### What the Code Does

Converts raw packet bytes captured from a network or file into a structured, layered Python object reflecting each protocol layer.

#### How it Does It

- Uses `parse_packet` function to analyze raw bytes.
- Recursively decomposes packet data into nested protocol layer objects.
- Validates and decodes fields such as addresses, ports, flags.

#### Why It’s Structured That Way

- Provides an intuitive object representation to access and manipulate packet data.
- Decouples raw data from protocol logic for modularity.
- Supports easy inspection and modification.

#### Variation Points

- Use specific protocol class constructors directly for partial or crafted packets.
- Customize parsing behavior with options for incomplete packets or non-standard headers.

---

### Pattern 2: Crafting and Sending Packets

#### What the Code Does

 Constructs a multi-layered packet from protocol objects, serializes it, and sends it on a network interface.

#### How it Does It

- Instantiate layer classes (`Ethernet`, `IP`, `TCP` etc.), setting desired fields.
- Nest payload layers as attributes.
- Serialize entire packet into bytes.
- Inject bytes into network using sniffing/injection APIs.

#### Why It's Structured That Way

- Enables fine-grained control over network packet composition.
- Abstracts byte-level complexity within protocol classes.
- Supports testing, simulation, and attack scenarios (e.g., pen testing).

#### Variation Points

- Change header field values to simulate different traffic.
- Use different protocols or omit layers for custom packets.
- Combine with sniffing to reply or monitor traffic.

---

### Pattern 3: Sniffing Network Traffic

#### What the Code Does

Captures live network packets from a given interface, parses and yields them for analysis.

#### How it Does It

- Calls `sniff` function with interface and filter criteria.
- Uses underlying OS tools and libpcap to capture packets.
- Parses packets into layered objects for consumption.

#### Why It’s Structured That Way

- Provides a high-level interface to packet capture functionality.
- Enables real-time network traffic analysis and monitoring.
- Supports BPF filtering for performance and relevance.

#### Variation Points

- Customize BPF filters to focus on specific protocols or hosts.
- Limit capture count or timeout for controlled operation.
- Process packets asynchronously or in callbacks.

---

## Example Pattern: Craft and Send TCP SYN Packet

```python
from pypacker.layer12 import ethernet
from pypacker.layer3 import ip
from pypacker.layer4 import tcp
from pypacker import packer

# Build TCP SYN packet
eth = ethernet.Ethernet()
eth.src_s = '00:11:22:33:44:55'  # Source MAC address
eth.dst_s = '66:77:88:99:aa:bb'  # Destination MAC address

ip_pkt = ip.IP(src_s='192.168.1.100', dst_s='192.168.1.1')
tcp_pkt = tcp.TCP(sport=12345, dport=80, flags="S")  # SYN flag set

# Nest protocols
ip_pkt.payload = tcp_pkt
eth.payload = ip_pkt

# Serialize packet to bytes
raw_bytes = eth.bin()

# Inject packet on interface 'eth0'
import pypacker.pypacker as pypacker_module
pypacker_module.inject(eth, iface='eth0')
```

- **What:** Constructs a TCP SYN packet encapsulated in IP and Ethernet headers, sets addresses and ports, and sends it on a network interface.
- **How:** Builds layered packet objects, nests them, serializes to bytes, and uses injection function to send.
- **Why:** Demonstrates precise crafting of network packets for connection attempts, testing, or scanning.
- **Variation:** Change flags to "A" for ACK, change IP/MAC for target devices, or add additional layers (e.g., VLAN).

---

## Additional Developer Notes

- Field assignment is string or integer based depending on layer; IP and MAC addresses have string representations.
- Calling `.bin()` on a packet layer serializes it including child layers.
- You can modify any header field before serialization.
- Use exception handling for parsing unpredictable or malformed packets.
- Combining sniffing and injection enables interactive traffic manipulation.
- Consult source code for detailed protocol support as custom layers can be added.

---

This documentation presents Pypacker’s domain concepts of network protocol layering, core execution facts covering parsing and crafting APIs, and usage patterns demonstrating practical application scenarios for robust understanding and effective utilization of the library.
```
