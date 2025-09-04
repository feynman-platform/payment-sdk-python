# BuyBtcResponseListPlatformAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**List[PlatformAccountEntity]**](PlatformAccountEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_list_platform_account_entity import BuyBtcResponseListPlatformAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseListPlatformAccountEntity from a JSON string
buy_btc_response_list_platform_account_entity_instance = BuyBtcResponseListPlatformAccountEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseListPlatformAccountEntity.to_json())

# convert the object into a dict
buy_btc_response_list_platform_account_entity_dict = buy_btc_response_list_platform_account_entity_instance.to_dict()
# create an instance of BuyBtcResponseListPlatformAccountEntity from a dict
buy_btc_response_list_platform_account_entity_from_dict = BuyBtcResponseListPlatformAccountEntity.from_dict(buy_btc_response_list_platform_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


