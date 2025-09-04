# BuyBtcResponsePayPaginationLedgerTransactionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayPaginationLedgerTransactionEntity**](PayPaginationLedgerTransactionEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_pay_pagination_ledger_transaction_entity import BuyBtcResponsePayPaginationLedgerTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayPaginationLedgerTransactionEntity from a JSON string
buy_btc_response_pay_pagination_ledger_transaction_entity_instance = BuyBtcResponsePayPaginationLedgerTransactionEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayPaginationLedgerTransactionEntity.to_json())

# convert the object into a dict
buy_btc_response_pay_pagination_ledger_transaction_entity_dict = buy_btc_response_pay_pagination_ledger_transaction_entity_instance.to_dict()
# create an instance of BuyBtcResponsePayPaginationLedgerTransactionEntity from a dict
buy_btc_response_pay_pagination_ledger_transaction_entity_from_dict = BuyBtcResponsePayPaginationLedgerTransactionEntity.from_dict(buy_btc_response_pay_pagination_ledger_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


