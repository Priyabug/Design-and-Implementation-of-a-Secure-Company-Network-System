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
# 🏫 University ICT Infrastructure Overview

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

> 🛠️ This well-orchestrated infrastructure ensures the University ICT environment remains **resilient**, **secure**, and **future-ready**.


