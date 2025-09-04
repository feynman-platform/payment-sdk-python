# BuyBtcResponseMerchantWalletEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantWalletEntity**](MerchantWalletEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_wallet_entity import BuyBtcResponseMerchantWalletEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantWalletEntity from a JSON string
buy_btc_response_merchant_wallet_entity_instance = BuyBtcResponseMerchantWalletEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantWalletEntity.to_json())

# convert the object into a dict
buy_btc_response_merchant_wallet_entity_dict = buy_btc_response_merchant_wallet_entity_instance.to_dict()
# create an instance of BuyBtcResponseMerchantWalletEntity from a dict
buy_btc_response_merchant_wallet_entity_from_dict = BuyBtcResponseMerchantWalletEntity.from_dict(buy_btc_response_merchant_wallet_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


