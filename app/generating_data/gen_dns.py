import json
import dnstwist

MY_DOMAINS = ['facebook.com', 
              'chat.openai.com', 
              'twitter.com', 
              'youtube.com',
              'yahoo.com',
              'google.com']

if __name__ == "__main__":
    variations = {}

    for domain in MY_DOMAINS:
        print("working on:", domain)
        data = dnstwist.run(domain=domain, registered=True, format='null')
        variations[domain] = data

    with open('data.json', 'w') as f:
        json.dump(variations, f, default=str, indent=4)