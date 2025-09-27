# PayResponsePaginationMerchantWalletEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationMerchantWalletEntity**](PayPaginationMerchantWalletEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_merchant_wallet_entity import PayResponsePaginationMerchantWalletEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationMerchantWalletEntity from a JSON string
pay_response_pagination_merchant_wallet_entity_instance = PayResponsePaginationMerchantWalletEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationMerchantWalletEntity.to_json())

# convert the object into a dict
pay_response_pagination_merchant_wallet_entity_dict = pay_response_pagination_merchant_wallet_entity_instance.to_dict()
# create an instance of PayResponsePaginationMerchantWalletEntity from a dict
pay_response_pagination_merchant_wallet_entity_from_dict = PayResponsePaginationMerchantWalletEntity.from_dict(pay_response_pagination_merchant_wallet_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


