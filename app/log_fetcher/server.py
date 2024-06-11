import certstream
import zmq
import json

def certstream_callback(message, context):
    
    data = message['data']
    if 'leaf_cert' in data:
        all_domains = data['leaf_cert']['all_domains']
        
        for domain in all_domains:
            domain_data = json.dumps({"domain": domain})
            
            # SEND TO CLIENT
            socket.send_string(json.dumps(data))
            print(f"Sent domain: {domain}")


if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:5555")

    print("Starting CertStream listener...")
    certstream.listen_for_events(certstream_callback, url='wss://certstream.calidog.io/')