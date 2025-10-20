```md
# Pypacker Documentation

Pypacker is a comprehensive pure Python library for packet creation, manipulation, and parsing. It supports a wide variety of network protocols and provides tools for easy packet crafting, dissecting captured packets, and network analysis tasks. Pypacker is designed for developers and researchers working with network protocols, penetration testing, and traffic analysis.

---

## Conceptual Introduction

### Domain Concepts

- **Packet Crafting and Parsing:** Pypacker enables the creation, modification, and decoding of network packets across multiple protocol layers.
- **Protocol Stack Layers:** Supports multiple protocols such as Ethernet, IP (IPv4/IPv6), TCP, UDP, ARP, DNS, DHCP, MPLS, and many others, offering a layered packet construction.
- **Packet Dissection:** Decoding raw packet data into structured protocol fields for inspection or modification.
- **Serialization/Deserialization:** Converting packet objects into raw bytes for transmission and vice versa.
- **Network Protocol Abstractions:** Representation of protocols as Python classes and objects, each encapsulating protocol-specific fields and logic.
- **Asynchronous and Synchronous Interfaces:** Flexibility to operate in different network programming contexts.
- **Packet Capture and Replay:** Integration for capturing live packets and optionally replaying them.
- **Extension and Custom Protocols:** Ability to create user-defined protocols by extending the base classes.

### Mapping to API Terms

- The core of the library organizes protocols as classes derived from `pypacker.Packet`.
- Protocol layers can be stacked or nested by assigning layers to each other's payload fields.
- Methods like `.bin()` serialize packets to bytes; `.unpack()` parses raw bytes back to packet objects.
- Field accessors provide easy reading and setting of protocol header fields.
- Utilities for checksums calculation, address conversion, and packet injection support network programming workflows.
- Supports both low-level raw byte handling and high-level packet manipulation.

---

## Execution Facts

### Core Classes and Methods

| API Element                            | Inputs                                          | Outputs                                      | Errors / Side Effects                               | Defaults / Constraints                              |
|--------------------------------------|------------------------------------------------|----------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| `pypacker.Packet`                    | Initialization with optional raw data bytes    | Packet object representing protocol instance | Parsing errors raised on malformed data             | Abstract base for all protocols                      |
| `.unpack(buff)`                     | `buff: bytes`                                  | Packet instance populated with data          | Raises exceptions on parse failure                   | Buff must contain valid bytes for the protocol      |
| `.bin()`                           | None                                           | Serialized bytes of the packet                | None                                                | Recalculates dependent fields like checksums       |
| `.copy()`                          | None                                           | Deep copy of the packet object                | None                                                | Preserves full state                                 |
| `.nextlayer()`                    | None                                           | The payload (next protocol layer)             | None                                                | Returns None if no further layers                    |
| `.add_pack(layer)`                 | Instance of Packet (a protocol layer)          | None                                           | None                                                | Appends payload layer to current packet             |

### Notable Protocol Classes

- `pypacker.layer12.ethernet.Ethernet`
- `pypacker.layer3.ip.IP` and `pypacker.layer3.ip6.IP6`
- `pypacker.layer4.tcp.TCP`
- `pypacker.layer4.udp.UDP`
- `pypacker.layer3.arp.ARP`
- `pypacker.layer7.dns.DNS`
- `pypacker.layer7.dhcp.DHCP`
- Others include MPLS, SCTP, GRE, ICMP, and more.

### Utilities and Tools

- Checksum calculation methods, e.g., `.auto_checksum()`.
- Address conversion helpers: MAC and IP address formatting and parsing.
- Packet capture integration via external libraries (e.g., pcap).
- Logging and debugging support to inspect packet internals.

### Constraints and Environmental Notes

- Pure Python, no external C dependencies required.
- Tested primarily on Linux but runs on most platforms supporting Python.
- Performance adequate for many use cases but not optimized for high-throughput production.
- Requires Python 3.x.
- Certain protocols depend on correct payload chaining for full functionality.

---

## API Usage Patterns

### Pattern 1: Crafting a Packet from Scratch

#### What the code does

Creates an Ethernet frame with an IPv4 packet containing a TCP segment, sets header fields, and serializes for sending.

#### How it does it

- Instantiate each protocol layer as objects (`Ethernet()`, `IP()`, `TCP()`).
- Set relevant fields (addresses, ports, flags) on these objects.
- Attach layers using `.add_pack()` to form the protocol stack.
- Call `.bin()` on the top-level packet to serialize the entire frame.

#### Why it’s structured that way

- Reflects the OSI layered model clearly for clarity and modularity.
- Allows easy modifications of individual protocol headers before sending.
- Provides flexibility to build arbitrary protocol stacks dynamically.

#### Variation Points

- Switch IP to IPv6 by using `IP6` in place of `IP`.
- Add application layer protocols supported by pypacker.
- Modify field values or insert custom payload data.

---

### Pattern 2: Parsing and Inspecting Raw Packets

#### What the code does

Processes raw bytes captured from the network, unpacks them into protocol objects, and accesses header fields.

#### How it does it

- Use `Packet().unpack(raw_bytes)` to decode bytes.
- Check packet layers with `.nextlayer()` or by directly accessing fields.
- Inspect protocol-specific fields like IP addresses, TCP ports, flags.

#### Why it’s structured that way

- Allows developers to process incoming traffic in a structured form.
- Simplifies analysis scripts and intrusion detection applications.
- Supports extension for decoding proprietary or new protocols.

#### Variation Points

- Handle errors or corrupted packets gracefully.
- Chain filters or callbacks on parsed packets.
- Modify and re-inject processed packets after inspection.

---

### Pattern 3: Extending Protocol Support with Custom Layers

#### What the code does

Defines a new protocol layer by subclassing `pypacker.Packet` and specifying its fields and parsing logic.

#### How it does it

- Create a class with `_fields` and `__hdr__` defining the protocol structure.
- Implement `unpack` and `bin` methods as necessary.
- Use the new protocol in packet stacks and parsing routines.

#### Why it’s structured that way

- Provides flexibility to handle niche or proprietary protocols.
- Integrates seamlessly with existing pypacker parsing and crafting workflows.

#### Variation Points

- Support variable-length fields or options.
- Add computed properties for protocol-specific flags.
- Overload parsing to support protocol extensions.

---

## Example Pattern: Crafting an Ethernet/IPv4/TCP Packet

```python
from pypacker.layer12.ethernet import Ethernet
from pypacker.layer3.ip import IP
from pypacker.layer4.tcp import TCP

# Create Ethernet layer
eth = Ethernet(dst_s="00:11:22:33:44:55", src_s="66:77:88:99:aa:bb")

# Create IP layer
ip = IP(dst_s="192.168.1.1", src_s="192.168.1.2")

# Create TCP layer
tcp = TCP(dport=80, sport=12345, flags="S")

# Stack layers
eth.add_pack(ip)
ip.add_pack(tcp)

# Serialize packet to bytes
packet_bytes = eth.bin()

print(f"Packet length: {len(packet_bytes)} bytes")
```

- **What:** Creates a layered network packet with Ethernet, IPv4, and TCP SYN.
- **How:** Instantiates protocol objects, sets fields, and attaches them in hierarchical order.
- **Why:** Illustrates the packet crafting workflow and layer stacking for custom packets.
- **Variation:** Modify IP addresses, TCP flags, or add payload data to tcp.

---

## Additional Developer Notes

- Pypacker has numerous protocol layer modules under the `layer12`, `layer3`, `layer4`, and `layer7` namespaces.
- The library supports both raw sockets and packet capture libraries for advanced usage though some features need root privileges.
- Refer to the extensive unit tests and example scripts in the repository for complex use cases.
- The API is designed for ease of extension, allowing new protocols and tools to integrate naturally.
- Great for educational purposes, prototyping network tools, and security research.

---

This documentation incorporates domain concepts, execution facts, and usage patterns to build a robust understanding for developers aiming to use Pypacker for network packet crafting, parsing, and analysis using Python.
```
