import requests

cookie = {'visit-month': 'February'}
response = requests.get('https://rahulshettyacademy.com',
                        allow_redirects=False,
                        cookies=cookie,
                        timeout=2)
print(response.history)  # shows redirection and should return 301 status code
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'})
resp = se.get('https://httpbin.org/cookies',
              cookies={'visit-year': '2022'},
              allow_redirects=False,
              timeout=1)
print(resp.history)
print(resp.text)
