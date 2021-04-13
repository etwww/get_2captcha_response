from twocaptcha import TwoCaptcha

def solveCaptcha(sitekey, url, callback):
    api_key = "ENTER_YOUR_2CAPTCHA_KEY_HERE"

    solver = TwoCaptcha(api_key)
    print(f'Getting {url.split("://")[1].split("/")[0]} captcha solution..')
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)
        sys.exit(e)

    print('Captcha solved')
    _callback = callback.split("['0']")[0] + "['0']" + \
                                callback.split("['0']")[1].replace("['", ".").replace("']",
                                                                                                     "")

    print(_callback + '("' + result['code'] + '")')

while True:
    print('\n')
    sitekey = input('SITEKEY: ').replace('"', "")
    url = input('URL: ').replace('"', "")
    callback = input('callback: ').replace('"', "")

    solveCaptcha(sitekey, url, callback)