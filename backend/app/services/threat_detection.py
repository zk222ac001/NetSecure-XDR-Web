suspicious_patterns = [
    "malware",
    "trojan",
    "powershell",
    "mimikatz",
    "beacon"
]

def analyze_packet(packet):
    alerts = []

    for pattern in suspicious_patterns:
        if pattern in packet.lower():
            alerts.append({
                "severity": "HIGH",
                "pattern": pattern
            })
                        
    return alerts