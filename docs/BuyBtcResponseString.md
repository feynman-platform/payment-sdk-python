# BuyBtcResponseString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_string import BuyBtcResponseString

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseString from a JSON string
buy_btc_response_string_instance = BuyBtcResponseString.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseString.to_json())

# convert the object into a dict
buy_btc_response_string_dict = buy_btc_response_string_instance.to_dict()
# create an instance of BuyBtcResponseString from a dict
buy_btc_response_string_from_dict = BuyBtcResponseString.from_dict(buy_btc_response_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


