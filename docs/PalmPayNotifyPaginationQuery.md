# PalmPayNotifyPaginationQuery

PalmPay通知分页查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**currency** | **str** | 货币类型 | [optional] 
**order_status** | **int** |  | [optional] 
**complete_time** | **List[str]** | 查询开始时间区间 | [optional] 
**amount** | **List[str]** | 金额区间 | [optional] 
**payer_bank_code** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_notify_pagination_query import PalmPayNotifyPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayNotifyPaginationQuery from a JSON string
palm_pay_notify_pagination_query_instance = PalmPayNotifyPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(PalmPayNotifyPaginationQuery.to_json())

# convert the object into a dict
palm_pay_notify_pagination_query_dict = palm_pay_notify_pagination_query_instance.to_dict()
# create an instance of PalmPayNotifyPaginationQuery from a dict
palm_pay_notify_pagination_query_from_dict = PalmPayNotifyPaginationQuery.from_dict(palm_pay_notify_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


