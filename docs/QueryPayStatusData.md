# QueryPayStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**fee** | [**Fee**](Fee.md) |  | [optional] 
**order_no** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_status** | **int** |  | [optional] 
**session_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**error_msg** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**completed_time** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.query_pay_status_data import QueryPayStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPayStatusData from a JSON string
query_pay_status_data_instance = QueryPayStatusData.from_json(json)
# print the JSON string representation of the object
print(QueryPayStatusData.to_json())

# convert the object into a dict
query_pay_status_data_dict = query_pay_status_data_instance.to_dict()
# create an instance of QueryPayStatusData from a dict
query_pay_status_data_from_dict = QueryPayStatusData.from_dict(query_pay_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


