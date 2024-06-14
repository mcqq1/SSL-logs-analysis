## SSL Logs Analysis
This project listens to SSL logs via certstream and is catching potential phishing websites, by comparing their domains to ones generated by dnstwister.
This project was written in Python 3.12.3.

## Installation
1. Clone the repo.
```shell
git clone https://github.com/mcqq1/SSL-logs-analysis.git
```

2. Create virtual environment and install dependencies.
```shell
cd SSL-logs-analysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
Files that are meant to be runned are:
1. ```run_client.py```
  This script activates the client (the one who takes url and checks it with 'is_phishing' function). When runned it should display ```Consumer is ready to receive data...```
2. ```run_server.py```
  This script activates the server (the one who sends urls fetched via certstream to client.). When runned with client activated, it should print current url it is sending.
3. ```scan.py```
  This is a helper script. It's just a simple Virus Total API integration, to further verificate potential phishing websites. If you wish to use it, you need to generate your own Virus Total API key via their official website https://docs.virustotal.com/reference/overview. We recommend parsing the API key via ```.env``` file and ```python-dotenv``` module. 

To run the code so it can look for potential phishing, you just run
```shell
python run_client.py # we are running client first
python run_server.py # this command in different terminal
```
Then we wait for client to print SSL's that returned 'True' when parsed to 'is_phishing' function.
