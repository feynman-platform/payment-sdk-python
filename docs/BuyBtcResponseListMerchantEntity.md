# BuyBtcResponseListMerchantEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**List[MerchantEntity]**](MerchantEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_list_merchant_entity import BuyBtcResponseListMerchantEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseListMerchantEntity from a JSON string
buy_btc_response_list_merchant_entity_instance = BuyBtcResponseListMerchantEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseListMerchantEntity.to_json())

# convert the object into a dict
buy_btc_response_list_merchant_entity_dict = buy_btc_response_list_merchant_entity_instance.to_dict()
# create an instance of BuyBtcResponseListMerchantEntity from a dict
buy_btc_response_list_merchant_entity_from_dict = BuyBtcResponseListMerchantEntity.from_dict(buy_btc_response_list_merchant_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


