# 🪐 Death Star Security Audit (IaC Scanner)

![Terraform](https://img.shields.io/badge/Infrastructure-Terraform-purple)
![Security](https://img.shields.io/badge/Status-CRITICAL_VULNERABILITIES-red)
![Empire](https://img.shields.io/badge/Approved_By-Galactic_Empire-black)

**An Infrastructure-as-Code (IaC) security scanner designed to audit the Death Star's architectural plans and prevent "critical thermal exhaust" incidents.**

In the modern Galactic Empire, we don't just build battle stations; we secure them. This project demonstrates **DevSecOps** principles by shifting security left—scanning Terraform code for misconfigurations *before* the Rebellion finds them.

## 🏗️ Architecture
This tool mimics industry-standard scanners like **Checkov** or **Trivy**, but custom-built for Imperial compliance.

1.  **Infrastructure:** Defined in `infrastructure/death_star.tf` (Terraform HCL).
2.  **Policy Engine:** Custom Python logic (`src/security_droid.py`) that parses HCL against security rules.
3.  **Reporting:** Generates a prioritized vulnerability report for the ISB (Imperial Security Bureau).

## 🧪 Demo Walkthrough

Follow these steps to audit the station's security posture.

### Step 1: Clone the Plans
```bash
git clone [https://github.com/codyjkeller/death-star-iac-security.git](https://github.com/codyjkeller/death-star-iac-security.git)
cd death-star-iac-security
pip install -r requirements.txt
```

### Step 2: Run the Security Droid
Execute the scan to audit the current architecture:

```bash
python src/security_droid.py
```

### Step 3: Analyze Findings
The scanner will output a prioritized list of vulnerabilities. Look for **VULN-1138** (The Fatal Flaw).

**Expected Output:**
```text
🚨 ISB-01 SECURITY SCAN INITIATED 🚨
Scanning architectural plans for sabotage...

⚠️  SECURITY AUDIT FINDINGS
┏━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ID        ┃ Severity ┃ Resource             ┃ Finding                                         ┃
┡━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ VULN-1138 │ CRITICAL │ thermal_exhaust_port │ Thermal port unshielded. Risk of chain reaction.│
│ VULN-0021 │ HIGH     │ detention_block      │ Weak encryption (ROT13) detected.               │
│ VULN-0001 │ MEDIUM   │ imperial_superlaser  │ Superlaser missing MFA safety lock.             │
└───────────┴──────────┴──────────────────────┴─────────────────────────────────────────────────┘

RECOMMENDATION:
Immediate patch required for Sector 7-G.
Alert Lord Vader immediately.
```

## 🛡️ Policies Checked
* **Encrypted Storage:** Ensures detention blocks use AES-256, not ROT13.
* **Attack Surface Reduction:** Checks if thermal ports are ray-shielded AND particle-shielded.
* **Access Control:** Verifies MFA on superweapon triggers.

---
*Maintained by the Imperial Security Bureau (and [Cody Keller](https://github.com/codyjkeller))*
