alerts = []

def detect_threat(packet):

    suspicious_keywords = [

        "malware",
        "exploit",
        "trojan",
        "dns"
    ]

    for keyword in suspicious_keywords:

        if keyword in packet["summary"].lower():

            alerts.append({

                "severity": "HIGH",
                "message": packet["summary"]
            })