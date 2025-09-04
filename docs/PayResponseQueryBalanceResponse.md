# PayResponseQueryBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**QueryBalanceResponse**](QueryBalanceResponse.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_query_balance_response import PayResponseQueryBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponseQueryBalanceResponse from a JSON string
pay_response_query_balance_response_instance = PayResponseQueryBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(PayResponseQueryBalanceResponse.to_json())

# convert the object into a dict
pay_response_query_balance_response_dict = pay_response_query_balance_response_instance.to_dict()
# create an instance of PayResponseQueryBalanceResponse from a dict
pay_response_query_balance_response_from_dict = PayResponseQueryBalanceResponse.from_dict(pay_response_query_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


