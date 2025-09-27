# WalletAuthorizationParam

钱包授权参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | 钱包ID | 
**merchant_id** | **str** | 授权的商户ID | 
**permissions** | **List[int]** | 钱包功能列表 | 

## Example

```python
from buybtcpay.models.wallet_authorization_param import WalletAuthorizationParam

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAuthorizationParam from a JSON string
wallet_authorization_param_instance = WalletAuthorizationParam.from_json(json)
# print the JSON string representation of the object
print(WalletAuthorizationParam.to_json())

# convert the object into a dict
wallet_authorization_param_dict = wallet_authorization_param_instance.to_dict()
# create an instance of WalletAuthorizationParam from a dict
wallet_authorization_param_from_dict = WalletAuthorizationParam.from_dict(wallet_authorization_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


