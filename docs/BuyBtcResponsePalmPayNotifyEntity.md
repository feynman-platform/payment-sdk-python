# BuyBtcResponsePalmPayNotifyEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PalmPayNotifyEntity**](PalmPayNotifyEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_palm_pay_notify_entity import BuyBtcResponsePalmPayNotifyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePalmPayNotifyEntity from a JSON string
buy_btc_response_palm_pay_notify_entity_instance = BuyBtcResponsePalmPayNotifyEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePalmPayNotifyEntity.to_json())

# convert the object into a dict
buy_btc_response_palm_pay_notify_entity_dict = buy_btc_response_palm_pay_notify_entity_instance.to_dict()
# create an instance of BuyBtcResponsePalmPayNotifyEntity from a dict
buy_btc_response_palm_pay_notify_entity_from_dict = BuyBtcResponsePalmPayNotifyEntity.from_dict(buy_btc_response_palm_pay_notify_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


