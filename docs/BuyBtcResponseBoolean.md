# BuyBtcResponseBoolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_boolean import BuyBtcResponseBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseBoolean from a JSON string
buy_btc_response_boolean_instance = BuyBtcResponseBoolean.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseBoolean.to_json())

# convert the object into a dict
buy_btc_response_boolean_dict = buy_btc_response_boolean_instance.to_dict()
# create an instance of BuyBtcResponseBoolean from a dict
buy_btc_response_boolean_from_dict = BuyBtcResponseBoolean.from_dict(buy_btc_response_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


