# ✔️ Cookie Scraping
# ✔️ Fingerprint Scraping
# ✔️ Mail Wrapper (mail.tm)
# ✔️ Captcha func.
# ✔️ Discord Wrapper (discord.com)
# ❌ Realistic Usernames
# ❌ Profile Picture

import httpx, random, string
from time import sleep
import asyncio

class header():

    def get(cookie, fingerprint, referer, auth):

        return {
            "Host": "discord.com",
            "Connection": "keep-alive",
            "accept": "*/*",
            "cache-control": "no-cache",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": auth,
            "content-type": "application/json",
            "cookie": cookie,
            "origin": "https://discord.com",
            "referer": "https://discord.com/" + referer,
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-GB",
            "x-fingerprint": fingerprint,
            "x-track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC4xMTAgU2FmYXJpLzUzNy4zNiBFZGcvOTYuMC4xMDU0LjYyIiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjExMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5OTk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }




class scrape():

    def cookies(proxy):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __cookies__ = __httpx__.get('https://discord.com/api/v9/experiments')
        dcf = __cookies__.headers['set-cookie'].split(';')[0].split('=')[1]
        sdc = __cookies__.headers['set-cookie'].split('__sdcfduid=')[1].split(';')[0]
        return f"__dcfduid={dcf}; __sdcfduid={sdc}; locale=en-US"


    def fingerprint(proxy):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __fingerprint__ = __httpx__.get('https://discord.com/api/v9/experiments')
        return __fingerprint__.json()['fingerprint']

class mail():

    def get(proxy):
#
    #    # Get Domain
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        #__header__ = {'accept': 'application/json', 'content-type': 'application/json'}
        #__domain__ = __httpx__.get('https://api.mail.tm/domains?page=1', headers=__header__); __domain__ = __domain__.json()[0]['domain']
        __random_email__ = 'FetixRules_' + ''.join(random.choice(string.ascii_lowercase) for i in range(8)) 
        __password__ = ''.join(random.choice(string.punctuation + string.ascii_letters + string.digits) for i in range(16))
        #__data__ = {'address': __random_email__ + '@alilot.com', 'password': __password__}
        #await __httpx__.post(f'https://api.mail.tm/accounts', headers=__header__, json=__data__)
        #__token__ = __httpx__.post(f'https://api.mail.tm/token', headers=__header__, json=__data__); __token__ = __token__.json()['token']
        #return __random_email__+'@'+__domain__, __password__, __token__

        __data__ = {"name": __random_email__}
        __request__ = __httpx__.post('https://api.internal.temp-mail.io/api/v3/email/new', json=__data__)
        __email__ = __request__.json()['email']
        return __email__, __password__
            

    def read(proxy, email):
        import json
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
    #   __header__ = {'accept': 'application/json', 'Content-Type': 'application/json', 'authorization': 'Bearer ' + token}
    #   __res__ = __httpx__.get('https://api.mail.tm/messages', headers=__header__)
    #   return __res__.json()
        __request__ = __httpx__.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages')
        return json.dumps(__request__.json(), indent=4)

    def wait(proxy, email):
        import json
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
    #   __header__ = {'accept': 'application/json', 'Content-Type': 'application/json', 'authorization': 'Bearer ' + token}
    #   __res__ = __httpx__.get('https://api.mail.tm/messages', headers=__header__); __res__ = __res__.json()
    #   while __res__ == []:
    #       __res__ = __httpx__.get('https://api.mail.tm/messages', headers=__header__); __res__ = __res__.json()
    #       sleep(6)
    #   return __res__
        __request__ = __httpx__.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages'); __request__ = __request__
        while __request__.json() == []:
            __request__ = __httpx__.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages'); __request__ = __request__
            sleep(6)
        return(__request__.json())

    def read_id(proxy, token, id):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = {'accept': 'application/json', 'Content-Type': 'application/json', 'authorization': 'Bearer ' + token}
        __res__ = __httpx__.get('https://api.mail.tm/messages/' + id, headers=__header__)
        return __res__.json()



class captcha():

    def solve(proxy, api_key):
        from capmonster_python import HCaptchaTask

        __cap__ = HCaptchaTask(api_key)
        __prox__ = proxy.split(':')
        __proxy__ = __cap__.set_proxy('http', __prox__[0], int(__prox__[1]))
        __useragent__ = __cap__.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
        __task_id__ = __cap__.create_task('https://discord.com', 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34')
        __join_task__ = __cap__.join_task_result(__task_id__)
        return __join_task__.get('gRecaptchaResponse')

class discord():

    def register(proxy, cookies, fingerprint, username, captcha_key):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookies, fingerprint, '', '')
        payload = {"captcha_key": captcha_key, "username": username, "invite": "uE2ZpFZ6"}
        try: __register__ = __httpx__.post('https://discord.com/api/v9/auth/register', headers=__header__, json=payload); return(__register__.json()['token'])
        except Exception as e: print(__register__.text); exit()

    def claim_mail(proxy, cookies, fingerprint, token, email, password):
        __header__ = header.get(cookies, fingerprint, 'channels/@me', token)
        payload = {"email": email, "password": password}
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __claim__ = __httpx__.post('https://discord.com/api/v9/users/@me', headers=__header__, json=payload)
        return __claim__.json()['token'], __claim__.json()['discriminator']

    def extract_token(proxy, url):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __res__ = __httpx__.get(url)
        return __res__.text

    def verify(proxy, cookie, fingerprint, token, etoken, captcha_key):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'verify', token)
        payload = {"captcha_key": captcha_key, "token": etoken}
        __httpx__.post('https://discord.com/api/v9/auth/verify', headers=__header__, json=payload)

    def get_code(proxy, cookie, fingerprint, token, phone_number, captcha_key):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'verify', token)
        payload = {"captcha_key": captcha_key, "phone": phone_number, "change_phone_reason": "user_action_required"}
        bro = __httpx__.post('https://discord.com/api/v9/users/@me/phone', headers=__header__, json=payload)
        if "Valid" in bro.text:
            exit()
            

    def send_code(proxy, cookie, fingerprint, atoken, phone_number, phone_code):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'channels/@me', atoken)
        __payload__ = {"code": str(phone_code), "phone": str(phone_number)}
        __token__ = __httpx__.post('https://discord.com/api/v9/phone-verifications/verify', headers=__header__, json=__payload__)
        __token__ = __token__.json()['token']
        return __token__

    def send_password(proxy, cookie, fingerprint, token, phone_token, password):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'channels/@me', token)
        payload = {"password": password, "phone_token": phone_token, "change_phone_reason": "user_action_required"}
        __token__ = __httpx__.post('https://discord.com/api/v9/users/@me/phone', headers=__header__, json=payload)

    def set_pfp(proxy, cookie, fingerprint, token, pfp):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'channels/@me', token)
        payload = {"avatar": 'data:image/png;base64,' + pfp}
        __httpx__.patch('https://discord.com/api/v9/users/@me', headers=__header__, json=payload)

    def set_bio(proxy, cookie, fingerprint, token, bio):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'channels/@me', token)
        payload = {"bio": bio}
        __httpx__.patch('https://discord.com/api/v9/users/@me', headers=__header__, json=payload)

    def change_username(proxy, cookie, fingerprint, token, username, password):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'channels/@me', token)
        payload = {"password": password, "username": username}
        __httpx__.patch('https://discord.com/api/v9/users/@me', headers=__header__, json=payload)

    def set_status(proxy, cookie, fingerprint, token, text):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = header.get(cookie, fingerprint, 'channels/@me', token)
        payload = {"status": text}
        __httpx__.patch('https://discord.com/api/v9/users/@me', headers=__header__, json=payload)

class phone():

    def buy(proxy, apikey, country, operator, service):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = {"Authorization": f"Bearer {apikey}", "Accept": "application/json"}
        try: __res__ = __httpx__.get(f'https://5sim.net/v1/user/buy/activation/{country}/{operator}/{service}', headers=__header__); return __res__.json()['phone'],  __res__.json()['id']
        except Exception as e: print(__res__.text); print(e); exit()
            
            

    def wait(proxy, id, apikey):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = {"Authorization": f"Bearer {apikey}", "Accept": "application/json"}
        __res__ = __httpx__.get(f'https://5sim.net/v1/user/check/{id}', headers=__header__)
        while __res__.json()['sms'] == []: __res__ = __httpx__.get(f'https://5sim.net/v1/user/check/{id}', headers=__header__); sleep(5)
        return __res__.json()['sms'][0]['code']

    def finish(proxy, id, apikey):
        __httpx__ = httpx.Client(proxies=f'http://{proxy}')
        __header__ = {"Authorization": f"Bearer {apikey}", "Accept": "application/json"}
        __httpx__.get(f'https://5sim.net/v1/user/finish/{id}', headers=__header__)