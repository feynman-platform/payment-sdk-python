# WalletPermissionQuery

钱包权限查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**wallet_id** | **List[str]** | 钱包ID列表 | [optional] 
**permissions** | **List[int]** | 钱包功能列表 | [optional] 
**merchant_id** | **List[str]** | 授权的商户ID列表 | [optional] 

## Example

```python
from buybtcpay.models.wallet_permission_query import WalletPermissionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPermissionQuery from a JSON string
wallet_permission_query_instance = WalletPermissionQuery.from_json(json)
# print the JSON string representation of the object
print(WalletPermissionQuery.to_json())

# convert the object into a dict
wallet_permission_query_dict = wallet_permission_query_instance.to_dict()
# create an instance of WalletPermissionQuery from a dict
wallet_permission_query_from_dict = WalletPermissionQuery.from_dict(wallet_permission_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


