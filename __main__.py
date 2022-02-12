import aero
import asyncio
import threading
import base64
import random
import os

# current modules:
# aero.scrape.cookies(proxy)
# aero.scrape.fingerprint(proxy)
# aero.mail.get(proxy)
# aero.mail.read(proxy, token)
# aero.mail.wait(proxy, token)
# aero.mail.read_id(proxy, token, id)
# aero.captcha.solve(proxy, api_key)
# aero.discord.register(proxy, cookies, fingerprint, email, username, password, captcha_key)

# demo (unverified token gen)

proxy = '127.0.0.1:24001'
api_key = 'ed57845c4f8cfc04fed1aa427d98642d'
sim_key = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzA3NjM5NjYsImlhdCI6MTYzOTIyNzk2NiwicmF5IjoiYWMwYTAxNWE1MzA3NWVmNDQ1ZmY0OGM1MTA5MjA2NTciLCJzdWIiOjgyNzIzMH0.aKUxFQLAXVF_w1SXZiiDjcqSsPrdlamUdCx9_Yxy5NOXN1i2tIpKqGN-cZGmZmaIpr1pPSZ9pLIyIAUQ7gIhU-ui2yhUak539b1bprLbeXYuWAZqfiYkVaBCkhvw0_dOw_72zsXnyufsRmctlIjnOzWaLrmAFMYMnCNPV2limmMJ4Y7HxAbSSU1DERVItCGCdvHNdMh_88PCcZ3jV_8E13tb6iw51ngapPh_wWhS3Ijq4wXsnxMUkAvoGruXnaLPbggwEeyXYMc-Av2uPmAzUCHhRJ1LYHeJG1yREfYQj-16O_ArtJ7KpRClKb14WwT0GzqH4GyN9E08gapvrnbphg'

#country = input('🌍  Country? ')
#operator = input('🛫  Operator? ')

def main(textfile, country, operator):
    print('🔃 Solving Captcha...')
    captcha = aero.captcha.solve(proxy, api_key)
    print('🍪 Fetching Cookies...')
    cookies = aero.scrape.cookies(proxy)
    print('🍃 Fetching Fingerprint...')
    fingerprint = aero.scrape.fingerprint(proxy)
    print('📧 Fetching Mail...')
    email, password = aero.mail.get(proxy)
    print('😊 Registering...')
    with open('username.txt', 'r') as f: names = f.read().splitlines(); username = random.choice(names)
    token = aero.discord.register(proxy, cookies, fingerprint, username, captcha)
    token, discriminator = aero.discord.claim_mail(proxy, cookies, fingerprint, token, email, password)

    def phone_verification():
        print('📲 Buying Phone...')
        phone, id = aero.phone.buy(proxy, sim_key, country, operator, 'discord')
        print('🔃 Solving Captcha...')
        captcha = aero.captcha.solve(proxy, api_key)
        print('💻 Sending code to phone...')
        aero.discord.get_code(proxy, cookies, fingerprint, token, phone, captcha)
        print('💭 Waiting for SMS...')
        code = aero.phone.wait(proxy, id, sim_key)
        print('🔒 Sending Code to Discord... [{}]'.format(code))
        phone_token = aero.discord.send_code(proxy, cookies, fingerprint, token, phone, code)
        print('🔒 Sending Password to Discord... [{}]'.format(password))
        aero.discord.send_password(proxy, cookies, fingerprint, token, phone_token, password)
        print('📲 Finishing Order...')
        aero.phone.finish(proxy, id, sim_key)
        return(phone)

    def email_verification():
        print('📧 Waiting for email...')
        read = aero.mail.wait(proxy, email)
        link = read[0]['body_text'].split('\n\nVerify email: ')[1].split('\n\n')[0]
        print('📧 Reading email...')
        #read = aero.mail.read_id(proxy, etoken, id))['text']; link = read.split('\n\nVerify email: ')[1]
        verify_token = aero.discord.extract_token(proxy, link); verify_token = verify_token.split('#token=')[1].split('">')[0]
        print('🔃 Solving Captcha...')
        captcha = aero.captcha.solve(proxy, api_key)
        print('🔒 Verifying account...')
        aero.discord.verify(proxy, cookies, fingerprint, token, verify_token, captcha)

    def set_pfp():
        image = random.choice(os.listdir("image"))
        aero.discord.set_pfp(proxy, cookies, fingerprint, token, base64.b64encode(open('image/'+str(image), 'rb').read()).decode('utf-8'))
    def set_bio():
        with open('bio.txt', 'r') as f: bio = random.choice(f.readlines())
        aero.discord.set_bio(proxy, cookies, fingerprint, token, bio)

    #email_verification()
    threading.Thread(target = email_verification).start()
    phone = phone_verification()
    print('👤 Setting profile picture...')
    set_pfp()
    print('👤 Setting bio...')
    set_bio()
    with open(textfile, 'a') as f: f.write(f"""Token: {token}
Username: {username}#{discriminator}
Email: {email}
Phone: {phone}
Password: {password}
--------------------------------------------------
""")

def funny_spam(textfile):
    captcha = aero.captcha.solve(proxy, api_key)
    cookies = aero.scrape.cookies(proxy)
    fingerprint = aero.scrape.fingerprint(proxy)
    email, password = aero.mail.get(proxy)
    with open('username.txt', 'r') as f: names = f.read().splitlines(); username = random.choice(names)
    token, discriminator = aero.discord.register(proxy, cookies, fingerprint, username, captcha)
    with open(textfile, 'a') as f: f.write(f"Token: {token} | Username: {username}#{discriminator} | Password: {password}\n")

#threads = input('🚪  How many threads? ')
#textfile = input('📄  Text file? ')
textfile = 'lol.txt'
funny_spam(textfile)
