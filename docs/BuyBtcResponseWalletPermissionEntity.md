# BuyBtcResponseWalletPermissionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**WalletPermissionEntity**](WalletPermissionEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_wallet_permission_entity import BuyBtcResponseWalletPermissionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseWalletPermissionEntity from a JSON string
buy_btc_response_wallet_permission_entity_instance = BuyBtcResponseWalletPermissionEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseWalletPermissionEntity.to_json())

# convert the object into a dict
buy_btc_response_wallet_permission_entity_dict = buy_btc_response_wallet_permission_entity_instance.to_dict()
# create an instance of BuyBtcResponseWalletPermissionEntity from a dict
buy_btc_response_wallet_permission_entity_from_dict = BuyBtcResponseWalletPermissionEntity.from_dict(buy_btc_response_wallet_permission_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


