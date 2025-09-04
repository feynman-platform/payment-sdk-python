# BuyBtcMoneyJsonValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_money_json_value import BuyBtcMoneyJsonValue

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcMoneyJsonValue from a JSON string
buy_btc_money_json_value_instance = BuyBtcMoneyJsonValue.from_json(json)
# print the JSON string representation of the object
print(BuyBtcMoneyJsonValue.to_json())

# convert the object into a dict
buy_btc_money_json_value_dict = buy_btc_money_json_value_instance.to_dict()
# create an instance of BuyBtcMoneyJsonValue from a dict
buy_btc_money_json_value_from_dict = BuyBtcMoneyJsonValue.from_dict(buy_btc_money_json_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


