# MerchantTransactionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**payer_merchant_id** | **str** |  | [optional] 
**payee_merchant_id** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**transaction_status** | **int** | 0: NORMAL, 1: APPROVED, 2: REJECTED | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 
**message** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_transaction_entity import MerchantTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantTransactionEntity from a JSON string
merchant_transaction_entity_instance = MerchantTransactionEntity.from_json(json)
# print the JSON string representation of the object
print(MerchantTransactionEntity.to_json())

# convert the object into a dict
merchant_transaction_entity_dict = merchant_transaction_entity_instance.to_dict()
# create an instance of MerchantTransactionEntity from a dict
merchant_transaction_entity_from_dict = MerchantTransactionEntity.from_dict(merchant_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


