from urllib.parse import urlparse
import ipaddress

url = input("Enter URL: ").strip()
if "://" not in url:
    url = "http://" + url

parsed = urlparse(url)
host = (parsed.hostname or "").lower()
flags = []

keywords = ["login", "verify", "password", "secure", "account", "update", "wallet"]
if any(word in url.lower() for word in keywords):
    flags.append("Suspicious keyword present")

try:
    ipaddress.ip_address(host)
    flags.append("IP address used as host")
except ValueError:
    pass

if host and len(host.split(".")) > 4:
    flags.append("Excessive subdomains")

if "@" in parsed.netloc:
    flags.append("URL authority contains @")

if flags:
    print("Potentially suspicious URL")
    for flag in flags:
        print("-", flag)
else:
    print("No checked indicators detected")

print("Indicators are not proof of phishing; verify URLs using trusted methods.")
