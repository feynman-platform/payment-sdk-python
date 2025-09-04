# PaginationQuery

代付请求分页查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**amount** | **List[str]** |  | [optional] 
**order_no** | **str** |  | [optional] 
**order_id** | **str** | 支付平台交易单号，不是商户自己填写的交易单号 | [optional] 
**order_ids** | **List[str]** | 支付平台交易单号列表，不是商户自己填写的交易单号 | [optional] 
**merchant_order_id** | **str** | 商户订单号 | [optional] 
**order_status** | **List[int]** | 订单状态列表 | [optional] 

## Example

```python
from buybtcpay.models.pagination_query import PaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationQuery from a JSON string
pagination_query_instance = PaginationQuery.from_json(json)
# print the JSON string representation of the object
print(PaginationQuery.to_json())

# convert the object into a dict
pagination_query_dict = pagination_query_instance.to_dict()
# create an instance of PaginationQuery from a dict
pagination_query_from_dict = PaginationQuery.from_dict(pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


