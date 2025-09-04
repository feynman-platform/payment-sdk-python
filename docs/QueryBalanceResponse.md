# QueryBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp_code** | **str** |  | [optional] 
**resp_msg** | **str** |  | [optional] 
**data** | [**QueryBalanceData**](QueryBalanceData.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.query_balance_response import QueryBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBalanceResponse from a JSON string
query_balance_response_instance = QueryBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(QueryBalanceResponse.to_json())

# convert the object into a dict
query_balance_response_dict = query_balance_response_instance.to_dict()
# create an instance of QueryBalanceResponse from a dict
query_balance_response_from_dict = QueryBalanceResponse.from_dict(query_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


