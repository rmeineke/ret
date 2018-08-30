import requests

url = "https://www.sjretirement.com/sjfederated/PGWebMember.exe"
payload = {'username': 'robermeineke', 'password': 'nI2#^J$45p19xe'}
with requests.session() as s:
    # fetch the login page
    s.get(url)
    url1 = "https://www.sjretirement.com/sjfederated/PGWebMember.exe/login"

    # post to the login form
    r = s.post(url1, data=payload)
    print(r.text)
