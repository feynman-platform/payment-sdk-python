# BuyBtcResponseVirtualAccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**VirtualAccountData**](VirtualAccountData.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_virtual_account_data import BuyBtcResponseVirtualAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseVirtualAccountData from a JSON string
buy_btc_response_virtual_account_data_instance = BuyBtcResponseVirtualAccountData.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseVirtualAccountData.to_json())

# convert the object into a dict
buy_btc_response_virtual_account_data_dict = buy_btc_response_virtual_account_data_instance.to_dict()
# create an instance of BuyBtcResponseVirtualAccountData from a dict
buy_btc_response_virtual_account_data_from_dict = BuyBtcResponseVirtualAccountData.from_dict(buy_btc_response_virtual_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


