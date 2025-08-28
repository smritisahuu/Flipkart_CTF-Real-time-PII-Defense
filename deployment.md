# Overview

**The PII Redaction solution** detects and masks Personally Identifiable Information (PII) such as phone numbers, Aadhaar numbers, passport numbers, UPI IDs, and emails.
Instead of running inside the backend (server), it can be deployed as a **browser extension** that protects data directly in the **user’s browser**.

# Why Browser Extension?

**Client-side Protection**: Redacts PII before it even leaves the user’s computer.

**Low Latency**: No network delay because masking happens instantly in the browser.

**Ease of Use**: Users just install the extension once, no server changes needed.

**Visibility**: Users can visually confirm what data is being masked.

# How It Works

The browser extension listens for form submissions, text inputs, or API requests leaving the browser.

Before sending the request, it applies **regex-based PII detection** using the same patterns as in the Python script.

Sensitive values are masked/redacted in real-time.

The sanitized data is then sent to the server, ensuring PII never leaves the user’s device in raw form.

##  Quality and Practicality
The Browser Extension model is **practical** because it requires no changes to backend infrastructure.  
Users can simply install the extension, and PII redaction happens automatically inside the browser. This ensures data is sanitized before leaving the device.  

- Easy for end users to adopt (just install once).  
- Requires minimal developer effort compared to backend re-architecture.  
- Transparent masking builds trust and improves user confidence.  

---

##  Latency
- **Very low latency** because all redaction happens locally in the browser.  
- No network round trips are added (unlike API Gateway or centralized redaction services).  
- The impact on performance is negligible since regex matching is lightweight.  

---

## Cost
- **Cost-effective**: no servers or cloud infrastructure required.  
- Scaling is automatic: every browser handles its own redaction independently.  
- Maintenance costs are limited to updating regex rules and publishing extension updates.  

---

## Scale
- **Highly scalable** since each user’s browser is its own processing unit.  
- No central bottleneck or server overload, even if millions of users use the solution.  
- Extension updates can be pushed via Chrome Web Store/Firefox Add-ons for large-scale rollouts.  

---

## Creativity and Novelty
Most PII redaction solutions run at the **backend or network layer**.  
This proposal is **novel** because it brings **client-side redaction** directly into the user’s browser.  
It ensures maximum privacy since raw PII never leaves the device unprotected.  
This approach also empowers users by letting them see **exactly what gets masked** before submission.  

# Limitations

Works only for **browser-based applications** (not mobile apps or backend APIs).

Needs updates when regex rules or masking policies change.

Relies on users installing the extension.


## ✅ Conclusion
The Browser Extension deployment is **feasible, cost-effective, low-latency, and scalable**.  
It provides a unique client-side solution that complements traditional server-side protections, making it both **innovative and practical**.
