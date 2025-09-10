# QueryPayStatusResponse

PalmPay查询支付状态响应

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp_code** | **str** |  | [optional] 
**resp_msg** | **str** |  | [optional] 
**data** | [**QueryPayStatusData**](QueryPayStatusData.md) |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.query_pay_status_response import QueryPayStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPayStatusResponse from a JSON string
query_pay_status_response_instance = QueryPayStatusResponse.from_json(json)
# print the JSON string representation of the object
print(QueryPayStatusResponse.to_json())

# convert the object into a dict
query_pay_status_response_dict = query_pay_status_response_instance.to_dict()
# create an instance of QueryPayStatusResponse from a dict
query_pay_status_response_from_dict = QueryPayStatusResponse.from_dict(query_pay_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


