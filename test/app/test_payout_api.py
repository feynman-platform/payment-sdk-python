from buybtcpay.api.open_payout_api import OpenPayoutApi, OpenPayoutRequestDto
from buybtcpay.app.buybtc_api_client import BuyBtcApiClient
from buybtcpay.app.buybtc_payment_config import BuyBtcPaymentConfig
from buybtcpay.app.buybtc_sign_util import BuyBtcRequestBodyBase
from sonyflake import Sonyflake
import datetime


if __name__ == '__main__':
    start_time = datetime.datetime(2025, 1, 1, 0, 0, 0, 0, datetime.UTC)
    sf = Sonyflake(start_time=start_time, machine_id=1)
    PrivateKey = "your merchant private key"
    PublicKey = "your merchant public key"
    BuyBtcPublickKey = "buybtc payment public key"
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

