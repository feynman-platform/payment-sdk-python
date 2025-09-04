# BuyBtcResponseListMerchantWalletEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**List[MerchantWalletEntity]**](MerchantWalletEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseListMerchantWalletEntity from a JSON string
buy_btc_response_list_merchant_wallet_entity_instance = BuyBtcResponseListMerchantWalletEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseListMerchantWalletEntity.to_json())

# convert the object into a dict
buy_btc_response_list_merchant_wallet_entity_dict = buy_btc_response_list_merchant_wallet_entity_instance.to_dict()
# create an instance of BuyBtcResponseListMerchantWalletEntity from a dict
buy_btc_response_list_merchant_wallet_entity_from_dict = BuyBtcResponseListMerchantWalletEntity.from_dict(buy_btc_response_list_merchant_wallet_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


