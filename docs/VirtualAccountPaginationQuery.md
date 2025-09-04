# VirtualAccountPaginationQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**merchant_ids** | **List[str]** | 商户ID列表 | [optional] 
**account_status** | **int** | 0: NORMAL, 1: DISABLED | [optional] 
**parent_merchant_id** | **str** | 父商户ID | [optional] 

## Example

```python
from buybtcpay.models.virtual_account_pagination_query import VirtualAccountPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountPaginationQuery from a JSON string
virtual_account_pagination_query_instance = VirtualAccountPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountPaginationQuery.to_json())

# convert the object into a dict
virtual_account_pagination_query_dict = virtual_account_pagination_query_instance.to_dict()
# create an instance of VirtualAccountPaginationQuery from a dict
virtual_account_pagination_query_from_dict = VirtualAccountPaginationQuery.from_dict(virtual_account_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


