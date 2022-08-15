from requests import Session
from time import sleep


def get_response():
    with Session() as session:
        response = session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
            # params={
            #     "paramsname": "value"
            # }
            # headers={
            #     "Accept-Language": "ru"
            # 55555555555
            # }
        )
        # print(response.json())
        # print(response.text)
        # print(response.cookies)
        # print(response.headers)
        # print(response.url)
        sleep(3)
        print(response.status_code)

for i in range(10):
    get_response()
