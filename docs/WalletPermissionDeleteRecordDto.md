# WalletPermissionDeleteRecordDto

删除钱包权限

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | 钱包ID | 
**merchant_id** | **str** | 商户ID | 
**permissions** | **List[int]** | 如果不传或者为空，则删除所有权限 | [optional] 

## Example

```python
from buybtcpay.models.wallet_permission_delete_record_dto import WalletPermissionDeleteRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPermissionDeleteRecordDto from a JSON string
wallet_permission_delete_record_dto_instance = WalletPermissionDeleteRecordDto.from_json(json)
# print the JSON string representation of the object
print(WalletPermissionDeleteRecordDto.to_json())

# convert the object into a dict
wallet_permission_delete_record_dto_dict = wallet_permission_delete_record_dto_instance.to_dict()
# create an instance of WalletPermissionDeleteRecordDto from a dict
wallet_permission_delete_record_dto_from_dict = WalletPermissionDeleteRecordDto.from_dict(wallet_permission_delete_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


