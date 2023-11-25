import requests
import fake_useragent
from bs4 import BeautifulSoup

sessions = requests.Session()
link = 'https://github.com/session'
user_agent = fake_useragent.UserAgent().random

headers = {
    'User-Agent': user_agent
}

data = {
    'login': 'your_username',
    'password': 'your_password'
}

response = sessions.post(link, data=data, headers=headers, allow_redirects=False)

if response.status_code == 302:
    redirect_url = response.headers['Location']
    profile_response = sessions.get(redirect_url, headers=headers).text
    print(profile_response)
else:
    print("Login failed")

cookies_dict = [
    {"domain": kay.domain, "name": kay.name, "path": kay.path, "value": kay.value}
    for kay in sessions.cookies
]

session2 = requests.Session()


for cookie in cookies_dict:
    session2.cookies.set(**cookie)

resp = session2.get("https://github.com/kozhydlo", headers=headers)
print(resp.text)
