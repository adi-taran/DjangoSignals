import time
from django.dispatch import signal

suspicious_activity = signal(providing_args=["data"])

def alert_security_team(sender, data):
    print(f"Alerting: Suspicious traffic detected from {data['source_ip']} to {data['destination_ip']}")  
 
def analyze_network_traffic(data):
    if data['packet_data'] == 'malicious_packet':
        suspicious_activity.send(sender="suspicious activity detected", data=data)

data = {
    'source_ip': '192.168.1.100',
    'destination_ip': '8.8.8.8',
    'packet_data': 'malicious_packet'
}

analyze_network_traffic(data)







