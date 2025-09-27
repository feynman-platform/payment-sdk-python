# PayPaginationMerchantWalletEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[MerchantWalletEntity]**](MerchantWalletEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_merchant_wallet_entity import PayPaginationMerchantWalletEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationMerchantWalletEntity from a JSON string
pay_pagination_merchant_wallet_entity_instance = PayPaginationMerchantWalletEntity.from_json(json)
# print the JSON string representation of the object
print(PayPaginationMerchantWalletEntity.to_json())

# convert the object into a dict
pay_pagination_merchant_wallet_entity_dict = pay_pagination_merchant_wallet_entity_instance.to_dict()
# create an instance of PayPaginationMerchantWalletEntity from a dict
pay_pagination_merchant_wallet_entity_from_dict = PayPaginationMerchantWalletEntity.from_dict(pay_pagination_merchant_wallet_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


