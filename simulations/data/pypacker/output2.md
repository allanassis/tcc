```md
# Pypacker Documentation

Pypacker is a Python library designed for fast and easy packet creation, parsing, and manipulation. It provides a flexible and modular framework to work with network protocols and packet structures, aiming to simplify packet crafting, reading and modifying network packets across a wide variety of protocols.

---

## Conceptual Introduction

### Domain Concepts

- **Packet Parsing and Crafting:** The process of analyzing raw network data into structured protocol layers and constructing packets from structured protocol data.
- **Protocol Layers:** Network protocols are represented as layers stacked together (e.g., Ethernet, IP, TCP), each with its own fields and semantics.
- **Packet Injection and Sniffing:** Sending crafted packets out to networks and capturing network traffic for inspection.
- **Layered Protocol Stack:** Pypacker models each protocol as a separate layer object that can be combined and nested to represent encapsulated network traffic.
- **Protocol Fields:** Attributes within a protocol layer representing headers and payload data.
- **PCAP File Support:** Reading and writing captured packet files.

### Mapping to API Terms

- **Modules and Classes:** Pypacker contains modules that define protocols such as Ethernet, IP, TCP, UDP, ICMP, IPv6, ARP, etc.
- The core class for packet manipulation is usually `Packet`, which can hold nested protocol layers.
- Parsing raw bytes into layered protocols is handled via `unpack` methods.
- Packet building is done by creating protocol instances and setting fields, then calling `bin()` to convert back to raw bytes.
- PCAP files are handled by specific classes to read and write packet captures.
- Sniffing and injecting packets uses pypacker’s wrappers over common OS-level packet injection/sniffing tools.

---

## Execution Facts

### Core Classes and Methods

| API Element                  | Inputs                                | Outputs                          | Errors / Side Effects                                        | Defaults / Constraints                            |
|-----------------------------|-------------------------------------|---------------------------------|-------------------------------------------------------------|--------------------------------------------------|
| `Packet`                    | Protocol layers as attributes        | Packet object                   | Can raise parsing errors if raw data does not conform       | Supports building layered packets                 |
| `Packet.bin()`              | None (operates on instance fields)  | Raw bytes of the packet         | Serializes packet into binary format                         | Produces correct byte encoding per protocol       |
| `Packet.unpack(raw_bytes)` | Raw byte string                     | Packet object with layers       | Raises exceptions on malformed data                          | Returns highest-level unpacked protocol layer     |
| `pcap.Reader()`             | File path or file-like object        | Iterator over unpacked packets  | Raises IOError if file is invalid                            | Supports standard pcap format                      |
| `pcap.Writer()`             | File path or file-like object        | Write interface for packets    | May raise IOError on write failures                          | Writes standard pcap capture files                 |
| `inject()`                  | Raw bytes or packet object            | Transmits packet on network    | Requires appropriate OS permissions (root/admin)            | Blocking call; depends on underlying OS support   |
| `sniff()`                  | Timeout, count, filters                | Generator yielding packets     | May raise exceptions for interface errors                   | Uses OS packet capture system (libpcap or similar) |

### Common Protocol Modules

- `pypacker.layer3.ip.IP`: Supports IPv4 packet manipulation.
- `pypacker.layer3.ipv6.IP6`: Provides IPv6 manipulation capabilities.
- `pypacker.layer4.tcp.TCP`: TCP protocol layer for connection-oriented data.
- `pypacker.layer4.udp.UDP`: UDP protocol layer for connectionless data.
- `pypacker.layer2.ethernet.Ethernet`: Ethernet frame handling.
- `pypacker.layer3.arp.ARP`: Address Resolution Protocol layer support.
- `pypacker.layer4.icmp.ICMP`: Internet Control Message Protocol manipulation.

### Constraints

- Works best on Linux systems; some features may require elevated permissions.
- Packet injection and sniffing depend on system network interface and permissions.
- Parsing expects packets to be complete and well-formed; partial data can cause errors.
- PCAP reading/writing compatible with libpcap format.

---

## API Usage Patterns

### Pattern 1: Constructing and Sending a Custom Packet

#### What the code does

Creates layered packet structure starting from Ethernet, encapsulating IP and TCP layers, then sends it over the network.

#### How it does it

- Instantiate Ethernet layer and set MAC addresses.
- Create an IP layer nested inside Ethernet with source and destination IPs.
- Add a TCP layer with port information inside IP.
- Call `bin()` to serialize to bytes.
- Use `inject()` function to send the raw bytes over the network interface.

#### Why it’s structured that way

- Separates concerns by layering protocols for clarity and reuse.
- Allows detailed control over each protocol header field.
- Uses native OS methods to send raw packets.

#### Variation Points

- Customize protocol headers (flags, options).
- Use UDP instead of TCP by swapping protocol layers.
- Add payload data by extending the lower layer’s payload.

---

### Pattern 2: Parsing Packets from PCAP File

#### What the code does

Reads packets from a PCAP capture file and parses packet contents into protocol layers.

#### How it does it

- Open a PCAP file with `pcap.Reader`.
- Iterate over captured packets using the reader’s iterator.
- Call `Packet.unpack()` to parse raw bytes into structured layers.
- Access protocol fields via layer attributes.

#### Why it’s structured that way

- Streamlines parsing of offline captured traffic for analysis.
- Abstracts binary packet details into user-friendly objects.
- Efficient iteration without loading entire file in memory.

#### Variation Points

- Filter packets by protocol type during iteration.
- Extract and analyze specific fields (e.g., IP addresses, ports).

---

### Pattern 3: Sniffing Live Network Traffic

#### What the code does

Captures live packets from a network interface and processes each in real-time.

#### How it does it

- Call `sniff()` with interface name, packet count, timeout, or filtering rules.
- Receive parsed packets as they arrive.
- Process each packet’s layers to inspect or modify data.

#### Why it’s structured that way

- Provides real-time traffic analysis.
- Uses OS packet capture for efficiency.
- Offers flexibility with filter expressions.

#### Variation Points

- Use BPF filters to restrict captured traffic.
- Save sniffed packets to a PCAP file for offline analysis.

---

## Example Pattern: Creating, Serializing, and Sending a TCP Packet

```python
from pypacker.layer2.ethernet import Ethernet
from pypacker.layer3.ip import IP
from pypacker.layer4.tcp import TCP
from pypacker import inject

# Build Ethernet frame
eth = Ethernet(src_s="00:11:22:33:44:55", dst_s="66:77:88:99:aa:bb")

# Build IP layer
ip = IP(src="192.168.1.10", dst="192.168.1.20")

# Build TCP layer
tcp = TCP(sport=1234, dport=80, flags="S")  # SYN flag

# Nest layers
eth.payload = ip
ip.payload = tcp

# Serialize packet to raw bytes
packet_data = eth.bin()

# Send packet out over the network
inject(packet_data)

print("Packet sent.")
```

- **What:** Constructs a SYN TCP packet wrapped in IP and Ethernet layers.
- **How:** Creates each layer with appropriate fields, nests them, serializes to bytes, and injects on the wire.
- **Why:** Demonstrates Pypacker’s layered approach to packet crafting and network transmission.
- **Variation:** Modify source/destination addresses, ports, or flags to customize behavior.

---

## Additional Developer Notes

- Use root or administrator privileges to send or capture raw packets.
- For performance, prefer working on raw packets directly with minimal Python overhead.
- Check `pypacker` GitLab repository for additional protocol modules and examples.
- PCAP support eases integration with existing network analysis tools.
- Exception handling is important during parsing to handle corrupt or incomplete packets gracefully.

---

This documentation provides a comprehensive foundation combining domain concepts, execution facts, and practical usage patterns to empower developers to leverage Pypacker for robust and flexible network packet manipulation in Python.
```

