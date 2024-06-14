import zmq
import json
import os

from .phishing import is_phishing

def main():
    # Set up ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:5555")

    print("Consumer is ready to receive data...")

    my_data = []
    data = {}
    with open(os.path.join(os.path.dirname(__file__), 'potential_phishing.json'), 'r') as f:
        data = json.load(f)
    
    for domain, variations in data.items():
        for varation in variations:
            if varation.get('fuzzer') != 'original':
                my_data.append(varation.get('domain'))


    while True:
        # Receive the data from the server
        domain_data = socket.recv_string()
        domain_info = json.loads(domain_data)
        
        is_phishing_bool, phishing_reason = is_phishing(domain_info, my_data)
        if is_phishing_bool:
            domain_info['phishing_reason'] = phishing_reason
            print(json.dumps(domain_info, indent=4, default=str))
