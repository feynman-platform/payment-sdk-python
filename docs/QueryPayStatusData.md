# QueryPayStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**amount** | **int** | 订单金额(最小单位计量) 只有当status&#x3D;1时才会有值 | [optional] 
**fee** | [**Fee**](Fee.md) |  | [optional] 
**order_no** | **str** | PalmPay返回的订单号 | [optional] 
**order_id** | **str** | 商户原始订单号 | [optional] 
**order_status** | **int** | 订单状态(见订单状态) | [optional] 
**session_id** | **str** | 渠道响应参数，注：大部分非NIBSS通道不返回sessionId，此类订单若有问题需提供订单号找PalmPay和银行确认用户实际到账情况 | [optional] 
**message** | **str** | 订单状态描述信息 | [optional] 
**error_msg** | **str** | 错误信息 | [optional] 
**create_time** | **int** | 订单创建时间 | [optional] 
**completed_time** | **int** | 订单完成时间 | [optional] 

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


