# WalletPermissionEntity

将钱包的使用权限授予指定的商户

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**wallet_id** | **int** | 钱包ID | [optional] 
**permission** | **int** | 1: Bulk transaction, 11: Merchant self service recharge, 12: Palmpay virtual account recharge, 2: Transfer in, 3: Transfer out, 100: Trade transfer in, 101: Trade transfer out, 4: Payout, 5: Withdrawal, 6: Currency exchange, 70: To merchant, 71: From merchant, 8: Fee, 9: Frozen, 10: Unfrozen, 20: Refund, 30: Reversal platform to wallet, 31: Reversal wallet to platform, 32: Reversal wallet to wallet | [optional] 
**merchant_id** | **str** | 授予给的商户ID | [optional] 

## Example

```python
from buybtcpay.models.wallet_permission_entity import WalletPermissionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WalletPermissionEntity from a JSON string
wallet_permission_entity_instance = WalletPermissionEntity.from_json(json)
# print the JSON string representation of the object
print(WalletPermissionEntity.to_json())

# convert the object into a dict
wallet_permission_entity_dict = wallet_permission_entity_instance.to_dict()
# create an instance of WalletPermissionEntity from a dict
wallet_permission_entity_from_dict = WalletPermissionEntity.from_dict(wallet_permission_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


