import json
import dnstwist

MY_DOMAINS = ['facebook.com', 'pornhub.com', 'twitter.com', 'youtube.com']

if __name__ == "__main__":
    variations = {}

    for domain in MY_DOMAINS:
        data = dnstwist.run(domain=domain, registered=True, format='null')
        variations[domain] = data

    with open('data.json', 'w') as f:
        json.dump(variations, f, default=str, indent=4)