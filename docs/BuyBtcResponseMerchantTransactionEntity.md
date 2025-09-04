# BuyBtcResponseMerchantTransactionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantTransactionEntity**](MerchantTransactionEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_transaction_entity import BuyBtcResponseMerchantTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantTransactionEntity from a JSON string
buy_btc_response_merchant_transaction_entity_instance = BuyBtcResponseMerchantTransactionEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantTransactionEntity.to_json())

# convert the object into a dict
buy_btc_response_merchant_transaction_entity_dict = buy_btc_response_merchant_transaction_entity_instance.to_dict()
# create an instance of BuyBtcResponseMerchantTransactionEntity from a dict
buy_btc_response_merchant_transaction_entity_from_dict = BuyBtcResponseMerchantTransactionEntity.from_dict(buy_btc_response_merchant_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


