# Design-and-Implementation-of-a-Secure-Company-Network-System


# 🌐 Cytonn Innovation Ltd – Cloud-Driven Transformation

**Cytonn Innovation Ltd** is a dynamic and forward-thinking company specializing in providing **innovative cloud solutions** to clients worldwide. Leveraging **cutting-edge technology** and a team of highly skilled professionals, Cytonn Innovation focuses on developing and implementing **cloud-based solutions** tailored to the evolving needs of businesses across various industries.

With a strong emphasis on:

- ✨ Creativity  
- ⚡ Agility  
- 👥 Customer-centricity  

Cytonn Innovation empowers organizations to enhance their:

- Operational Efficiency  
- Scalability  
- Competitiveness in today’s digital landscape  

---

## 🏢 Company Expansion & Infrastructure Design

With a growing **workforce of 600 staff**, Cytonn Innovation Ltd is preparing to move into a **new three-story building**, which will house the following departments:

- 📈 Sales & Marketing  
- 🧑‍💼 Human Resources & Logistics  
- 💰 Finance & Accounts  
- 🏛️ Administration & Public Relations  
- 💻 ICT Department  
- 🖥️ Server Room  

### 🧑‍💻 ICT Department Roles

The ICT department consists of:

- Software Developers  
- Cloud Engineers  
- Cybersecurity Engineers  
- Network Engineers  
- System Administrators  
- IT Support Specialists  
- Business Analysts  
- Project Managers  

---

## 🔐 Network Design & Security Architecture

A new network service will be designed and implemented with **robust security measures** to safeguard from both **internal** and **external** threats.

### 🧱 Firewall Security Zones

- **Outside Zone** – Public-facing network  
- **Inside Zone** – Internal and trusted network  
- **DMZ (Demilitarized Zone)** – Semi-trusted zone for externally accessible servers  

### 📁 Server Placement Overview

| Server Type                     | Zone         |
|--------------------------------|--------------|
| Active Directory (AD)          | Inside       |
| DHCP, DNS, RADIUS              | Inside       |
| FTP, Web, Email, App, NAS      | DMZ          |

> ✅ This zoning ensures a secure, segmented network where internal resources are protected and only necessary services are exposed.

---

## 🏫 Main Campus Server Farm (DMZ)

The **Main Campus** hosts the centralized **Server Farm**, commonly referred to as the **DMZ**. It includes:

- 📡 DHCP  
- 🌐 DNS  
- 📁 FTP  
- 🕸️ Web  
- ✉️ Email  
- 📤 SMTP  

Users at the **Branch Campus** securely connect to these centralized services. This **protected connectivity** ensures reliable access to:

- 📘 Educational Resources  
- 💬 Communication Tools  
- 📊 Information Systems  

> 🔒 Secure resource access is enforced across all campuses, ensuring continuity and protection regardless of user location.

---

## ✅ Conclusion

Cytonn Innovation Ltd is positioning itself at the forefront of cloud and infrastructure transformation by:

- Building a **secure, scalable network**
- Enabling **seamless multi-department collaboration**
- Delivering **cloud-powered solutions** to clients across the globe

> 💼 With a strategic focus on innovation, security, and operational excellence, Cytonn is ready to thrive in the digital future.

---
As an integral part of the University's ICT infrastructure, the following components have been strategically incorporated to ensure high availability, scalability, and security across campuses:

---

## 🌐 Internet Services Provider (ISP)

- The university maintains active subscriptions with **two ISPs**:
  - **SEACOM**
  - **Safaricom**

> 🔁 This dual setup ensures **redundant internet connectivity** for uninterrupted access.

---

## 🔐 Network Security

- Two **Cisco ASA 5500-X Series Firewalls** have been deployed.
- These firewalls provide:
  - Advanced threat protection  
  - High availability  
  - Redundancy in network security

---

## 🧭 Network Routing

- **Routing functionality** is implemented using:
  - The Cisco ASA firewalls  
  - Core switches  
- ❌ No dedicated router is used, reducing hardware dependencies.

---

## 🔀 Switching Infrastructure

- For each campus:
  - **2 × Cisco Catalyst 3850** 48-Port Switches
- Additional access layer:
  - **Cisco Catalyst 2960** 48-Port Switches

> ⚙️ This setup ensures robust **local network connectivity** and smooth traffic handling.

---

## 🖥️ Server Hardware & Virtualization

- **2 Physical Servers** support virtualization via **hypervisor technology**.
- Multiple **Virtual Machines (VMs)** are created to deliver essential services.
- To ensure **redundancy and high availability**:
  - Two **DHCP servers** run concurrently.

---

## 📡 Wireless Infrastructure

- Centralized wireless management via:
  - **2 Cisco Wireless LAN Controllers (WLCs)**
- Supported by:
  - Multiple **Lightweight Access Points (LAPs)**

> 📶 Ensures efficient, scalable, and centralized wireless access across all campuses.

---

## 📞 VoIP / IP Telephony

- **VoIP (Voice over IP)** or **IP Phones** will be integrated for seamless internal and external communication across departments and offices.

---

# ☁️ Cloud-Driven Network Design Proposal

Cloud computing, as a pivotal technology, enables seamless connectivity between clients worldwide and the company's services and resources. Therefore, the **proposed network** must ensure secure, scalable, and efficient access to these resources.

---

## 🧑‍💻 Your Role: Network Design Lead

As a **key member of the Networks Team**, you have been tasked with designing the **logical network architecture** for the new company building.

This design must address:

- 🚀 **Top-tier performance**
- 🔁 **Redundancy**
- 📈 **Scalability**
- ⏱️ **High availability**

The objective is to build a **future-proof** and **business-aligned** network infrastructure.

---

## 🧠 Logical Network Design Objectives

The logical network should:

- Ensure seamless access to cloud-based services
- Support department-level segmentation
- Centralize management and monitoring
- Include appropriate security zones
- Be adaptable for future expansion

---

## 🧩 IP Addressing Scheme

To support the network segmentation and various service layers, the following **IP ranges** have been allocated:

| **Network Segment** | **Purpose**                          | **IP Range**            |
|---------------------|--------------------------------------|-------------------------|
| 🛠️ Management       | Device & network management          | `192.168.10.0/24`       |
| 📶 WLAN             | Wireless client access               | `10.20.0.0/16`          |
| 🖧 LAN              | Wired local area network             | `172.16.0.0/16`         |
| 📞 VoIP             | IP telephony and communication       | `172.30.0.0/16`         |
| 🔒 DMZ              | Public-facing services (semi-trusted)| `10.11.11.0/27`         |
| 🌍 Public IPs       | External connectivity via ISPs       | `105.100.50.0/30` (SEACOM)  
|                     |                                      | `197.200.100.0/30` (Safaricom) |

---

## 🧱 Key Design Considerations

1. **Redundancy**  
   Dual firewalls, switches, and ISP connections for high availability.

2. **Segmentation**  
   Separate subnets for different departments and services (LAN, WLAN, VoIP, DMZ).

3. **Scalability**  
   IP address ranges are large enough to accommodate future growth.

4. **Performance Optimization**  
   VLANs, QoS (for VoIP), and efficient routing protocols.

5. **Security**  
   DMZ zone for public services, ACLs, and firewall rules for traffic control.

---

## ✅ Outcome

The network design will empower the company to:

- Enhance **operational efficiency**
- Ensure **secure global connectivity**
- Achieve **business continuity**
- Prepare for **future technological advancements**

> 🧩 This logical design serves as the foundation for the implementation phase, aligning IT infrastructure with core business objectives.

---
# 🛠️ Technologies Implemented

Below are the core technologies and strategies utilized in designing and implementing the network solution:

---

## 1️⃣ Design Tool – Cisco Packet Tracer

- 🧪 **Cisco Packet Tracer** is used for the **design, simulation, and validation** of the network.
- Allows modeling of real-world scenarios to ensure configuration accuracy before deployment.

---

## 2️⃣ Hierarchical Network Design

- 🏛️ Follows a **three-tier hierarchical model**:
  - **Core Layer** – High-speed backbone connectivity
  - **Distribution Layer** – Policy-based routing, VLAN management
  - **Access Layer** – User and endpoint connectivity
- 🔁 Implements **redundancy** at key points to improve **network resilience** and **availability**.

---

## 3️⃣ ISP Integration

- 🌐 Establishes direct **connectivity to an Airtel ISP Router**.
- Ensures reliable **external access** to internet services and cloud-based resources.

---

## 4️⃣ Wireless LAN Infrastructure (WLC + WAPs)

- 📶 Each department is equipped with **Wireless Access Points (WAPs)** to offer Wi-Fi services to:
  - Employees
  - Corporate users
  - External auditors
  - Guests
- 🧠 All WAPs are **centrally managed** using a **Cisco Wireless LAN Controller (WLC)**, providing:
  - Centralized configuration
  - Security policy enforcement
  - Seamless roaming across access points

## 5️⃣ VoIP – Voice over IP Communication

- ☎️ Deploy **IP phones** across all departments to facilitate **VoIP-based communication**.
- Reduces reliance on traditional telephony and integrates with the existing network infrastructure.
- Enables cost-effective internal calling and scalable telephony features.

---

## 6️⃣ VLAN Configuration

- 🔀 Implement **Virtual LANs (VLANs)** to logically segment the network for better performance and security.

| VLAN ID | Purpose          |
|---------|------------------|
| 10      | Management       |
| 20      | LAN (Wired users)|
| 50      | WLAN (Wireless)  |
| 70      | VoIP             |
| 199     | Blackhole (Unused ports) |

> 🚫 **VLAN 199 (Blackhole)** ensures that **all unused switch ports** are isolated, reducing the attack surface and preventing unauthorized access.

---

## 7️⃣ EtherChannel – Link Aggregation with LACP

- 🔗 Configure **EtherChannel** using the **Link Aggregation Control Protocol (LACP)**.
- Bundles multiple physical links into a single logical link for:
  - 🚀 Increased **bandwidth**
  - ✅ Enhanced **redundancy**
  - ⚙️ Improved **load balancing**

> 🔐 EtherChannel ensures fault tolerance and efficient utilization of switch uplinks in the core and distribution layers.

## 8️⃣ STP Enhancements – PortFast & BPDU Guard

- 🧷 Configure **Spanning Tree Protocol (STP)** with:
  - **PortFast** to reduce port transition delays (from blocking to forwarding)
  - **BPDU Guard** to prevent rogue switches from compromising the network

> 🔐 Enhances Layer 2 security and minimizes boot-time disruptions.

---

## 9️⃣ Subnetting – Efficient IP Allocation

- 📊 Use **subnetting techniques** to allocate the right number of IP addresses to each department or network group.
- Promotes efficient IP space management and network segmentation.

---

## 🔟 Basic Device Settings

- 🔧 Apply essential configurations to all networking devices:
  - Hostnames  
  - Console and enable passwords  
  - Login banners  
  - Password encryption  
  - Disable IP domain lookup

> 🛡️ These foundational settings enhance device identity, security, and user experience.

---

## 1️⃣1️⃣ Inter-VLAN Routing

- 🌐 Configure **Inter-VLAN routing** on **multilayer switches** to enable communication between devices in different VLANs.

> ✅ Ensures full Layer 3 connectivity across all departments.

---

## 1️⃣2️⃣ Core Switch Configuration

- 🧠 Assign **IP addresses** to multilayer switches to enable both:
  - **Layer 2 switching**
  - **Layer 3 routing**

> 🛠️ This hybrid approach optimizes performance and central control.

---

## 1️⃣3️⃣ DHCP Server Integration

- 📥 Devices receive **dynamic IP addresses** from centralized DHCP servers located at the **server farm**.
- Simplifies IP management across multiple network segments.

---

## 1️⃣4️⃣ HSRP – High Availability

- 🚨 Implement **Hot Standby Router Protocol (HSRP)** for:
  - Redundancy  
  - Load balancing  
  - Automatic failover

> 🟢 Guarantees continuous network availability and smooth failover during outages.

---

## 1️⃣5️⃣ Static IP Addressing

- 🔒 Assign **static IPs** to critical devices in the **server room** for:
  - Consistency  
  - Easy management  
  - Improved reliability

---

## 1️⃣6️⃣ Routing Protocol – OSPF

- 🧭 Use **Open Shortest Path First (OSPF)** to advertise routes across:
  - Cisco ASA Firewall  
  - Routers  
  - Multilayer switches

> 🚀 Enables dynamic, efficient, and scalable routing decisions.

---

## 1️⃣7️⃣ Standard ACL for SSH

- 🔐 Apply a **standard Access Control List (ACL)** on **VTY lines** to:
  - Allow SSH access only from the **Senior Network Security Engineer’s PC**
  - Block all other unauthorized remote access attempts

---

## 1️⃣8️⃣ Cisco ASA Firewall Configuration

- 🔥 Configure the **Cisco ASA Firewall** with:
  - Default static routes  
  - Hostname and password settings  
  - Security levels and zones  
  - Access Control Policies

> 🎯 Provides perimeter defense and enforces security policies across network zones.

---

## 1️⃣9️⃣ Final Testing & Validation

- 🧪 Conduct **comprehensive testing** to ensure:
  - Inter-department communication  
  - Internet access  
  - DHCP lease distribution  
  - Routing protocol convergence  
  - Firewall enforcement

> ✅ Validates that all configurations work as intended before going live.

---

> 🚀 With these implementations, the proposed network ensures **scalability, redundancy, security, and performance**, meeting current needs and supporting future growth.







