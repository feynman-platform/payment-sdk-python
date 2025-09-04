# BuyBtcResponseMerchantEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantEntity**](MerchantEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_entity import BuyBtcResponseMerchantEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantEntity from a JSON string
buy_btc_response_merchant_entity_instance = BuyBtcResponseMerchantEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantEntity.to_json())

# convert the object into a dict
buy_btc_response_merchant_entity_dict = buy_btc_response_merchant_entity_instance.to_dict()
# create an instance of BuyBtcResponseMerchantEntity from a dict
buy_btc_response_merchant_entity_from_dict = BuyBtcResponseMerchantEntity.from_dict(buy_btc_response_merchant_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


