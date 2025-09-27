# BuyBtcResponseInteger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_integer import BuyBtcResponseInteger

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseInteger from a JSON string
buy_btc_response_integer_instance = BuyBtcResponseInteger.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseInteger.to_json())

# convert the object into a dict
buy_btc_response_integer_dict = buy_btc_response_integer_instance.to_dict()
# create an instance of BuyBtcResponseInteger from a dict
buy_btc_response_integer_from_dict = BuyBtcResponseInteger.from_dict(buy_btc_response_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


