from buybtcpay.api.open_payout_api import OpenPayoutApi, OpenPayoutRequestDto
from buybtcpay.app.buybtc_api_client import BuyBtcApiClient
from buybtcpay.app.buybtc_payment_config import BuyBtcPaymentConfig
from buybtcpay.models.merchant_payout_request_dto import MerchantPayoutRequestDto
from buybtcpay.app.buybtc_sign_util import BuyBtcRequestBodyBase
from sonyflake import Sonyflake
import datetime


if __name__ == '__main__':
    start_time = datetime.datetime(2025, 1, 1, 0, 0, 0, 0, datetime.UTC)
    sf = Sonyflake(start_time=start_time, machine_id=1)

    PrivateKey = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCzr6Fn2BcCFCFKDH0k9bY3FEpRhVyTGO+GMPgHLaObMET3xPM19JPlHJSkGgbulJaJAutgIYnAKqmFi2m6z82MwcLT60gZ/f4tQcfDN9PfOlBFKcpVE/gDvZPUJS5qHfauzxhjNnbIh7zjtpmcImelljDbi+b7s18CX9sm3JMbu1jmgbuexx3+4fhhrtG0sx0CV3rc/OtOJox1OvSyuzhQi3w86KCTbwqVHMbHfM+X4/EZQghoCQPjrboqyNR7SKOth655OPevwDkBOPW95Piyt1kCx/9k2ruFz86A3owNx2TMvBX5Acr/rDitDpVmMVoUa460RmwDj7mo4vmq5xHNAgMBAAECggEAKBZ6qtWPuoe9rozPPbfw7WRiOUJI10uEorpZl5Zjzhtsg5+lyCeW+FJSSjNBUSiG1i33z9RjrGMIO5JRJhu25tySqB9xkFT1iGjI1cGmjAKxRmDusmD4X/NDYBzkeEnTj4gGD5pm0VHRPzdtmWMmnw99OnoBsC2COKAkn0yuKE0YtloYczMTVMc3DZy2U9jXpuaVv3NRi2y5rBgKvNKDXrm2Tvkj9SLH4cuh/onHpM/Z0FLMIK3PKdMCbTn67h4gvmOAeSYyvTRHmKGGragpVig1OxUIVkh+GU7Ys7sBSC/wvg3dlbL/zfUCdgGrvg86366lOPqFB1DuiqV+Tf9w2QKBgQD71oxN2EV+MBPsGOysbaTgcX36xQPfjeANzF90wdUJhER7wFHFSxqQiwkRBZP2KeHLi7WaaNfVxU2dWsf1HMao+C0lfeSUPSLVzhqLuZvrXhDR18afTQEg529YyI0HkzT47i2aYHp/AYJjfZCk8BJTxxF9VfvgQwi0jy8ogmWjVQKBgQC2p9Ql6y2Rim6uQsQHY5nFzvHVvvLIQCMbnH8yTz2ggAQ5DwHYVzH0GJLw68OLMdA3329iLKnZU2Sw6j3ufZtNximCMudhgGcR7y/h6L8zibgCEe6+OlYlWBWeU2qKq02/tK62yHYulU+hmH1cjVaaXLcmhWfpkACpAMB2rW6kmQKBgQCl6Wr1vg3KXJJDcQg7cOC2nQ6KL1Gl7io17PbWTPy1EFat0L4OZLRTlcWbWTlpa54+IwS5fWj0hM/lYvFpIlQe7aGQmagFoWFZyjbi5p06KvaZyLYqLOkZbF+G9lkzLGAxv3h7xCPvmGb2dLrebuskFnoHQKZ30LHjgpFm9sFPIQKBgH0bvULvr/mlQSRZFN4eyZ/knF6UeMTSsXljGviBsCt0I/BVKCVfrBaOkm80fW6lAwKSJz+uafQym6BWAW+OV0bROXM1nKh7A54UH87z1areZMv+LnHbkU/o4n3ckvhCV3G8t4L5EYHcwXtk8FDpem0mnkhjTgZ7nQglPK7NIiDZAoGBAI2tcYOJg0/FJmm40n/k38LjH+H+qEdFeq8bCUJA6oVjW1jowiHqXE8L23t5cM5pMn1YfU6wUfqa6eEnPuPCOa63nPd/I61JaIEsSc0KV7bla1x9J9xHFr2OF2YLp/sWNOIHevdT4ZlNeosUbtsAw/35IK079VEhoWIzTtaQfQPp"
    PublicKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs6+hZ9gXAhQhSgx9JPW2NxRKUYVckxjvhjD4By2jmzBE98TzNfST5RyUpBoG7pSWiQLrYCGJwCqphYtpus/NjMHC0+tIGf3+LUHHwzfT3zpQRSnKVRP4A72T1CUuah32rs8YYzZ2yIe847aZnCJnpZYw24vm+7NfAl/bJtyTG7tY5oG7nscd/uH4Ya7RtLMdAld63PzrTiaMdTr0srs4UIt8POigk28KlRzGx3zPl+PxGUIIaAkD4626KsjUe0ijrYeueTj3r8A5ATj1veT4srdZAsf/ZNq7hc/OgN6MDcdkzLwV+QHK/6w4rQ6VZjFaFGuOtEZsA4+5qOL5qucRzQIDAQAB"
    BuyBtcPublickKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn3LGfzlKDrsJlJoWN7+lPJMAEF64IKuhPDkZS0LpgyWdqhJewvomD+AWQEdhNAGh0yESKV28L+HjxQSKz1GnHxP/MhZEK5UyB/Hvgi/vLAZ4/f3m6QGowqog5yPDm2a4vL5d67mPajFNKgEF5arGyj+bIsnSof2iuc7KpibbKtmRsayz2Y23WmAZta1Jt/SnoniHw9jFVG3IoDL6P9NaK+u0W4eURFKARRpcDSFPJ9juDOa1d34Tru7LX25x0eKqPnGUrtxqG0adoHprQjKPYjy+6ShEqvMaB92jUgYWRNpxmsZJ/5t0eOzZ3x/9Lpt9N2Y6L0Y/lBpPhG8cLpGxYQIDAQAB";

    config = BuyBtcPaymentConfig(
        base_url="http://127.0.0.1:9030",
        merchant_id="P25082908293101004",
        private_key=PrivateKey,
        buy_btc_pay_public_key=BuyBtcPublickKey
    )
    api_client = BuyBtcApiClient(config)
    api = OpenPayoutApi(api_client)
    payload = BuyBtcRequestBodyBase.attach({
        "orderId": str(sf.next_id()),
        "title": "test payout",
        "description": "test payout",
        "payeeName": "zhang san",
        "payeeBankCode": "01050000",
        "payeeBankAccNo": "6217000000000000018",
        "amount": "100",
        "currency": "NGN",
        "notifyUrl": None,
        "remark": "test"
    }, True)
    dto = OpenPayoutRequestDto.from_dict(payload)

    if dto is not None:
        resp = api.payout1(dto)
        print(resp)

