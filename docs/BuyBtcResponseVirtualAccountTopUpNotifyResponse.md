# BuyBtcResponseVirtualAccountTopUpNotifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**VirtualAccountTopUpNotifyResponse**](VirtualAccountTopUpNotifyResponse.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_virtual_account_top_up_notify_response import BuyBtcResponseVirtualAccountTopUpNotifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseVirtualAccountTopUpNotifyResponse from a JSON string
buy_btc_response_virtual_account_top_up_notify_response_instance = BuyBtcResponseVirtualAccountTopUpNotifyResponse.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseVirtualAccountTopUpNotifyResponse.to_json())

# convert the object into a dict
buy_btc_response_virtual_account_top_up_notify_response_dict = buy_btc_response_virtual_account_top_up_notify_response_instance.to_dict()
# create an instance of BuyBtcResponseVirtualAccountTopUpNotifyResponse from a dict
buy_btc_response_virtual_account_top_up_notify_response_from_dict = BuyBtcResponseVirtualAccountTopUpNotifyResponse.from_dict(buy_btc_response_virtual_account_top_up_notify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


