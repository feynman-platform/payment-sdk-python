# BuyBtcResponseMerchantWalletCountVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantWalletCountVo**](MerchantWalletCountVo.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_wallet_count_vo import BuyBtcResponseMerchantWalletCountVo

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantWalletCountVo from a JSON string
buy_btc_response_merchant_wallet_count_vo_instance = BuyBtcResponseMerchantWalletCountVo.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantWalletCountVo.to_json())

# convert the object into a dict
buy_btc_response_merchant_wallet_count_vo_dict = buy_btc_response_merchant_wallet_count_vo_instance.to_dict()
# create an instance of BuyBtcResponseMerchantWalletCountVo from a dict
buy_btc_response_merchant_wallet_count_vo_from_dict = BuyBtcResponseMerchantWalletCountVo.from_dict(buy_btc_response_merchant_wallet_count_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


