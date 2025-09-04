import json
from buybtcpay.api_client import ApiClient
from buybtcpay.app.buybtc_payment_config import BuyBtcPaymentConfig
from buybtcpay import rest
from buybtcpay.configuration import Configuration
from buybtcpay.app.buybtc_rsa import normalize_dict_to_content, sign_with_rsa


class BuyBtcApiClient(ApiClient):
    _config: BuyBtcPaymentConfig

    def __init__(self, config: BuyBtcPaymentConfig) -> None:
        configuration = Configuration(host = config.base_url)
        super().__init__(configuration=configuration)
        self._config = config

    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ) -> rest.RESTResponse:
        body_dict = {}
        if isinstance(body, dict):
            body_dict = body
        elif isinstance(body, str):
            body_dict = json.loads(body)
        else:
            body_dict = {}
        
        body_str = normalize_dict_to_content(body_dict)
        signature = sign_with_rsa(body_str, self._config.private_key)

        if header_params is None:
            header_params = {}

        header_params['Merchant-Id'] = self._config.merchant_id
        header_params['Signature'] = signature

        return super().call_api(method=method, url=url, 
                                header_params=header_params, 
                                body=body, post_params=post_params, 
                                _request_timeout=_request_timeout)