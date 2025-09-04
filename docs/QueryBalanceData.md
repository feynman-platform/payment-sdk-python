# QueryBalanceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | **int** |  | [optional] 
**frozen_balance** | **int** |  | [optional] 
**current_balance** | **int** |  | [optional] 
**un_settle_balance** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.query_balance_data import QueryBalanceData

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBalanceData from a JSON string
query_balance_data_instance = QueryBalanceData.from_json(json)
# print the JSON string representation of the object
print(QueryBalanceData.to_json())

# convert the object into a dict
query_balance_data_dict = query_balance_data_instance.to_dict()
# create an instance of QueryBalanceData from a dict
query_balance_data_from_dict = QueryBalanceData.from_dict(query_balance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


