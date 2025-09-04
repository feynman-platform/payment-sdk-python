# BuyBtcResponseQueryPayStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**QueryPayStatusResponse**](QueryPayStatusResponse.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_query_pay_status_response import BuyBtcResponseQueryPayStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseQueryPayStatusResponse from a JSON string
buy_btc_response_query_pay_status_response_instance = BuyBtcResponseQueryPayStatusResponse.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseQueryPayStatusResponse.to_json())

# convert the object into a dict
buy_btc_response_query_pay_status_response_dict = buy_btc_response_query_pay_status_response_instance.to_dict()
# create an instance of BuyBtcResponseQueryPayStatusResponse from a dict
buy_btc_response_query_pay_status_response_from_dict = BuyBtcResponseQueryPayStatusResponse.from_dict(buy_btc_response_query_pay_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


