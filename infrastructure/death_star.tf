# IMPERIAL INFRASTRUCTURE MANIFEST
# Project: DS-1 Orbital Battle Station
# Architect: Galen Erso

resource "imperial_superlaser" "primary_weapon" {
  name             = "Planet Killer"
  power_output     = "1000000_terawatts"
  safety_lock      = false  # VIOLATION: No 2FA on firing mechanism
  cooling_system   = "liquid_vacuum"
}

resource "thermal_exhaust_port" "sector_7_g" {
  id               = "target_area"
  width_meters     = 2.0
  shielding        = "ray_shielded" 
  proton_torpedo_protection = false  # CRITICAL VULNERABILITY
  leads_to         = "reactor_core"
}

resource "detention_block" "aa_23" {
  occupancy        = "princess_leia"
  security_cameras = "enabled"
  encryption       = "rot13"  # VIOLATION: Weak encryption standard
}

resource "tractor_beam" "docking_bay_327" {
  status           = "active"
  power_source     = "main_reactor"
  manual_override  = true # VIOLATION: Physical access allows bypass (Obi-Wan risk)
}
