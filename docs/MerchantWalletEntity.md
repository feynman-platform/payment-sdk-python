# MerchantWalletEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**available** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**frozen** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_wallet_entity import MerchantWalletEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWalletEntity from a JSON string
merchant_wallet_entity_instance = MerchantWalletEntity.from_json(json)
# print the JSON string representation of the object
print(MerchantWalletEntity.to_json())

# convert the object into a dict
merchant_wallet_entity_dict = merchant_wallet_entity_instance.to_dict()
# create an instance of MerchantWalletEntity from a dict
merchant_wallet_entity_from_dict = MerchantWalletEntity.from_dict(merchant_wallet_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


