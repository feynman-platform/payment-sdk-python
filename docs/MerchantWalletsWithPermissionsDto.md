# MerchantWalletsWithPermissionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet** | [**MerchantWalletEntity**](MerchantWalletEntity.md) |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_wallets_with_permissions_dto import MerchantWalletsWithPermissionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWalletsWithPermissionsDto from a JSON string
merchant_wallets_with_permissions_dto_instance = MerchantWalletsWithPermissionsDto.from_json(json)
# print the JSON string representation of the object
print(MerchantWalletsWithPermissionsDto.to_json())

# convert the object into a dict
merchant_wallets_with_permissions_dto_dict = merchant_wallets_with_permissions_dto_instance.to_dict()
# create an instance of MerchantWalletsWithPermissionsDto from a dict
merchant_wallets_with_permissions_dto_from_dict = MerchantWalletsWithPermissionsDto.from_dict(merchant_wallets_with_permissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


