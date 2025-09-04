class BuyBtcPaymentConfig:
    base_url: str
    merchant_id: str
    private_key: str
    buy_btc_pay_public_key: str

    def __init__(self, base_url: str, merchant_id: str, private_key: str, buy_btc_pay_public_key: str) -> None:
        self.base_url = base_url
        self.merchant_id = merchant_id
        self.private_key = private_key
        self.buy_btc_pay_public_key = buy_btc_pay_public_key