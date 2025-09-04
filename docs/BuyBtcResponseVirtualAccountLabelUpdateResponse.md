# BuyBtcResponseVirtualAccountLabelUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**VirtualAccountLabelUpdateResponse**](VirtualAccountLabelUpdateResponse.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_virtual_account_label_update_response import BuyBtcResponseVirtualAccountLabelUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseVirtualAccountLabelUpdateResponse from a JSON string
buy_btc_response_virtual_account_label_update_response_instance = BuyBtcResponseVirtualAccountLabelUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseVirtualAccountLabelUpdateResponse.to_json())

# convert the object into a dict
buy_btc_response_virtual_account_label_update_response_dict = buy_btc_response_virtual_account_label_update_response_instance.to_dict()
# create an instance of BuyBtcResponseVirtualAccountLabelUpdateResponse from a dict
buy_btc_response_virtual_account_label_update_response_from_dict = BuyBtcResponseVirtualAccountLabelUpdateResponse.from_dict(buy_btc_response_virtual_account_label_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


