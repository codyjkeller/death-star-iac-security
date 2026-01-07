import re
import os
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class ImperialSecurityDroid:
    """
    ISB-01 Security Scanner
    Audits Terraform infrastructure for critical vulnerabilities.
    """
    def __init__(self, tf_file_path="infrastructure/death_star.tf"):
        self.tf_file_path = tf_file_path
        self.vulnerabilities = []

    def load_infrastructure(self):
        # Fallback path logic
        if not os.path.exists(self.tf_file_path):
            self.tf_file_path = "../" + self.tf_file_path
        
        with open(self.tf_file_path, 'r') as f:
            return f.read()

    def scan(self):
        console.rule("[bold red]🚨 ISB-01 SECURITY SCAN INITIATED 🚨[/bold red]")
        console.print("[dim]Scanning architectural plans for sabotage...[/dim]\n")
        time.sleep(1.5) # Suspense...

        tf_content = self.load_infrastructure()

        # --- RULE 1: CHECK EXHAUST PORT SHIELDING ---
        if 'proton_torpedo_protection = false' in tf_content:
            self.vulnerabilities.append({
                "id": "VULN-1138",
                "severity": "CRITICAL",
                "resource": "thermal_exhaust_port",
                "message": "Thermal port unshielded against proton torpedoes. Risk of chain reaction."
            })

        # --- RULE 2: CHECK ENCRYPTION STANDARDS ---
        if 'encryption = "rot13"' in tf_content:
            self.vulnerabilities.append({
                "id": "VULN-0021",
                "severity": "HIGH",
                "resource": "detention_block",
                "message": "Weak encryption (ROT13) detected. Rebel slicers can decrypt communications."
            })

        # --- RULE 3: CHECK SUPERLASER SAFETY ---
        if 'safety_lock = false' in tf_content:
            self.vulnerabilities.append({
                "id": "VULN-0001",
                "severity": "MEDIUM",
                "resource": "imperial_superlaser",
                "message": "Superlaser missing MFA (Multi-Force Authentication)."
            })

        self.report()

    def report(self):
        if not self.vulnerabilities:
            console.print("[green]✅ No weakness detected. The station is fully operational.[/green]")
            return

        table = Table(title="⚠️  SECURITY AUDIT FINDINGS", border_style="red")
        table.add_column("ID", style="dim")
        table.add_column("Severity", style="bold red")
        table.add_column("Resource", style="yellow")
        table.add_column("Finding", style="white")

        for vuln in self.vulnerabilities:
            table.add_row(vuln['id'], vuln['severity'], vuln['resource'], vuln['message'])

        console.print(table)
        console.print(Panel(
            "[bold red]RECOMMENDATION:[/bold red] \nImmediate patch required for Sector 7-G.\n"
            "Alert Lord Vader immediately.",
            border_style="red"
        ))

if __name__ == "__main__":
    droid = ImperialSecurityDroid()
    droid.scan()
