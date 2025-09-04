# MerchantToMerchantTransactionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**payer_merchant_email** | **str** | 付款方商户ID | 
**payee_merchant_email** | **str** | 收款方商户ID | 
**amount** | **str** | 转账金额 | 
**currency** | **str** | 货币类型 | 
**note** | **str** | 转账备注 | [optional] 

## Example

```python
from buybtcpay.models.merchant_to_merchant_transaction_request_dto import MerchantToMerchantTransactionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantToMerchantTransactionRequestDto from a JSON string
merchant_to_merchant_transaction_request_dto_instance = MerchantToMerchantTransactionRequestDto.from_json(json)
# print the JSON string representation of the object
print(MerchantToMerchantTransactionRequestDto.to_json())

# convert the object into a dict
merchant_to_merchant_transaction_request_dto_dict = merchant_to_merchant_transaction_request_dto_instance.to_dict()
# create an instance of MerchantToMerchantTransactionRequestDto from a dict
merchant_to_merchant_transaction_request_dto_from_dict = MerchantToMerchantTransactionRequestDto.from_dict(merchant_to_merchant_transaction_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


