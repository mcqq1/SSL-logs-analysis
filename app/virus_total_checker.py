import requests
import os
import json

from loguru import logger
from dotenv import load_dotenv


URLS_TO_CHECK = [
    # 'http://myetherevvalliet.com/'
    # "imperva.com"
    "filegear-sg.me"
]


def main():
    load_dotenv()

    urls = URLS_TO_CHECK

    headers = {
        "accept": "application/json",
        "x-apikey": os.getenv('virus_total_api_key'),
        "content-type": "application/x-www-form-urlencoded"
    }

    for url in urls:
        logger.info(f"Scanning {url}")

        data = { "url": url }

        try:
            response_scan = requests.post(
                url="https://www.virustotal.com/api/v3/urls",
                data=data,
                headers=headers
            )
            response_scan.raise_for_status()
            analysis = response_scan.json()
            analysis_id = analysis.get('data', {}).get('id')

            response = requests.get(
                url=f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
                headers=headers
            )
            response.raise_for_status()
            result = response.json()

        except Exception as e:
            logger.error(f"Failed to scan {url}. {str(e)}")
        
        else:
            stats = result.get('data', {}).get('attributes', {}).get('stats', {})
            opinions = result.get('data', {}).get('attributes', {}).get('results', {})

            print(json.dumps(stats, indent=4, default=str))
            print("========")
            print("")

            for company, opinion in opinions.items():
                category = opinion.get('category')
                if category not in ['harmless', 'undetected']:
                    print(company)
                    print(json.dumps(opinion, indent=4, default=str))
                    print("===============================")
                    print("")


if __name__ == "__main__":
    main()