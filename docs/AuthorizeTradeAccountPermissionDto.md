# AuthorizeTradeAccountPermissionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_merchant_id** | **str** | 授权钱包的商户ID | 
**to_merchant_id** | **str** | 授予权限的商户ID | 

## Example

```python
from buybtcpay.models.authorize_trade_account_permission_dto import AuthorizeTradeAccountPermissionDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeTradeAccountPermissionDto from a JSON string
authorize_trade_account_permission_dto_instance = AuthorizeTradeAccountPermissionDto.from_json(json)
# print the JSON string representation of the object
print(AuthorizeTradeAccountPermissionDto.to_json())

# convert the object into a dict
authorize_trade_account_permission_dto_dict = authorize_trade_account_permission_dto_instance.to_dict()
# create an instance of AuthorizeTradeAccountPermissionDto from a dict
authorize_trade_account_permission_dto_from_dict = AuthorizeTradeAccountPermissionDto.from_dict(authorize_trade_account_permission_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


