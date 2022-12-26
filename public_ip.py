import requests


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return 'Unable to fetch public IP address.'
    except requests.RequestException:
        return 'Unable to fetch public IP address.'
