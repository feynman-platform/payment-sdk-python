# BuyBtcResponseApprovalEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**ApprovalEntity**](ApprovalEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseApprovalEntity from a JSON string
buy_btc_response_approval_entity_instance = BuyBtcResponseApprovalEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseApprovalEntity.to_json())

# convert the object into a dict
buy_btc_response_approval_entity_dict = buy_btc_response_approval_entity_instance.to_dict()
# create an instance of BuyBtcResponseApprovalEntity from a dict
buy_btc_response_approval_entity_from_dict = BuyBtcResponseApprovalEntity.from_dict(buy_btc_response_approval_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


