# BuyBtcResponseVirtualAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**VirtualAccountEntity**](VirtualAccountEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_virtual_account_entity import BuyBtcResponseVirtualAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseVirtualAccountEntity from a JSON string
buy_btc_response_virtual_account_entity_instance = BuyBtcResponseVirtualAccountEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseVirtualAccountEntity.to_json())

# convert the object into a dict
buy_btc_response_virtual_account_entity_dict = buy_btc_response_virtual_account_entity_instance.to_dict()
# create an instance of BuyBtcResponseVirtualAccountEntity from a dict
buy_btc_response_virtual_account_entity_from_dict = BuyBtcResponseVirtualAccountEntity.from_dict(buy_btc_response_virtual_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


