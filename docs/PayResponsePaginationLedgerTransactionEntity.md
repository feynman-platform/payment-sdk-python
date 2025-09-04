# PayResponsePaginationLedgerTransactionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationLedgerTransactionEntity**](PayPaginationLedgerTransactionEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_ledger_transaction_entity import PayResponsePaginationLedgerTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationLedgerTransactionEntity from a JSON string
pay_response_pagination_ledger_transaction_entity_instance = PayResponsePaginationLedgerTransactionEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationLedgerTransactionEntity.to_json())

# convert the object into a dict
pay_response_pagination_ledger_transaction_entity_dict = pay_response_pagination_ledger_transaction_entity_instance.to_dict()
# create an instance of PayResponsePaginationLedgerTransactionEntity from a dict
pay_response_pagination_ledger_transaction_entity_from_dict = PayResponsePaginationLedgerTransactionEntity.from_dict(pay_response_pagination_ledger_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


