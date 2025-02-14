import threading
from django.dispatch import Signal

suspicious_traffic_detected_tac = Signal()

def alert_security_team(sender, **kwargs): 
    thread_id = threading.get_ident()
    print(f"Security team alerted from thread ID - {thread_id}")

    print("Alert has been sent - Suspicious traffic detected")

def analyze_network_traffic(packet_data): 
    thread_id = threading.get_ident()
    print(f"Analyzing network traffic from thread ID - {thread_id}")

    if packet_data["malicious"]:
        suspicious_traffic_detected_tac.send(sender=None)

suspicious_traffic_detected_tac.connect(alert_security_team)


packet_data = {"malicious": True}
analyze_network_traffic(packet_data)

