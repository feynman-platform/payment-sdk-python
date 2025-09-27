# BuyBtcResponsePayPaginationWalletPermissionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayPaginationWalletPermissionEntity**](PayPaginationWalletPermissionEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_pay_pagination_wallet_permission_entity import BuyBtcResponsePayPaginationWalletPermissionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayPaginationWalletPermissionEntity from a JSON string
buy_btc_response_pay_pagination_wallet_permission_entity_instance = BuyBtcResponsePayPaginationWalletPermissionEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayPaginationWalletPermissionEntity.to_json())

# convert the object into a dict
buy_btc_response_pay_pagination_wallet_permission_entity_dict = buy_btc_response_pay_pagination_wallet_permission_entity_instance.to_dict()
# create an instance of BuyBtcResponsePayPaginationWalletPermissionEntity from a dict
buy_btc_response_pay_pagination_wallet_permission_entity_from_dict = BuyBtcResponsePayPaginationWalletPermissionEntity.from_dict(buy_btc_response_pay_pagination_wallet_permission_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


