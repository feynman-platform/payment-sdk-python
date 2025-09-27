# BuyBtcResponseListMerchantWalletsWithPermissionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**List[MerchantWalletsWithPermissionsDto]**](MerchantWalletsWithPermissionsDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_list_merchant_wallets_with_permissions_dto import BuyBtcResponseListMerchantWalletsWithPermissionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseListMerchantWalletsWithPermissionsDto from a JSON string
buy_btc_response_list_merchant_wallets_with_permissions_dto_instance = BuyBtcResponseListMerchantWalletsWithPermissionsDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseListMerchantWalletsWithPermissionsDto.to_json())

# convert the object into a dict
buy_btc_response_list_merchant_wallets_with_permissions_dto_dict = buy_btc_response_list_merchant_wallets_with_permissions_dto_instance.to_dict()
# create an instance of BuyBtcResponseListMerchantWalletsWithPermissionsDto from a dict
buy_btc_response_list_merchant_wallets_with_permissions_dto_from_dict = BuyBtcResponseListMerchantWalletsWithPermissionsDto.from_dict(buy_btc_response_list_merchant_wallets_with_permissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


