# BuyBtcResponsePalmPayNotifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PalmPayNotifyResponse**](PalmPayNotifyResponse.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_palm_pay_notify_response import BuyBtcResponsePalmPayNotifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePalmPayNotifyResponse from a JSON string
buy_btc_response_palm_pay_notify_response_instance = BuyBtcResponsePalmPayNotifyResponse.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePalmPayNotifyResponse.to_json())

# convert the object into a dict
buy_btc_response_palm_pay_notify_response_dict = buy_btc_response_palm_pay_notify_response_instance.to_dict()
# create an instance of BuyBtcResponsePalmPayNotifyResponse from a dict
buy_btc_response_palm_pay_notify_response_from_dict = BuyBtcResponsePalmPayNotifyResponse.from_dict(buy_btc_response_palm_pay_notify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


