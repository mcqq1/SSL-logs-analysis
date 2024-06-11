import zmq
import json

from phishing import is_phishing

def main():
    # Set up ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:5555")

    print("Consumer is ready to receive data...")

    my_data = []
    data = {}
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    for domain, variations in data.items():
        for varation in variations:
            if varation.get('fuzzer') != 'original':
                my_data.append(varation.get('domain'))

    with open('potential_phishings.json', 'w') as f:
        while True:
            # Receive the data from the producer
            domain_data = socket.recv_string()
            domain_info = json.loads(domain_data)
            
            is_phishing_bool, phishing_reason = is_phishing(domain_info, my_data)
            if is_phishing_bool:
                domain_info['phishing_reason'] = phishing_reason
                print(domain_info, phishing_reason)
                # json.dump(domain_info, f, indent=4, default=str)


if __name__ == '__main__':
    main()