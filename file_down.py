import sys
import urllib.request
import ssl
import hashlib
import certifi

if len(sys.argv) != 4:
    exit(1)

url = sys.argv[1]
expected_hash = sys.argv[2]

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl_context.check_hostname = True
ssl_context.verify_mode = ssl.CERT_REQUIRED

with urllib.request.urlopen(url, context=ssl_context) as response:
    file_data = response.read()

calculated_hash = hashlib.sha256(file_data).hexdigest()

if calculated_hash != expected_hash:
    raise ValueError("Downloaded file has been tampered with")

with open(sys.argv[3], "wb") as f:
    f.write(file_data)
