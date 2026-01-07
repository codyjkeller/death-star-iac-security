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

## 🚀 Usage

### 1. Clone the Plans
```bash
git clone [https://github.com/codyjkeller/death-star-iac-security.git](https://github.com/codyjkeller/death-star-iac-security.git)
cd death-star-iac-security
pip install -r requirements.txt
