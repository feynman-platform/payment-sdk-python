# LedgerTransactionAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PayPaginationLedgerTransactionEntity**](PayPaginationLedgerTransactionEntity.md) |  | [optional] 
**total_amount** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.ledger_transaction_aggregation import LedgerTransactionAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTransactionAggregation from a JSON string
ledger_transaction_aggregation_instance = LedgerTransactionAggregation.from_json(json)
# print the JSON string representation of the object
print(LedgerTransactionAggregation.to_json())

# convert the object into a dict
ledger_transaction_aggregation_dict = ledger_transaction_aggregation_instance.to_dict()
# create an instance of LedgerTransactionAggregation from a dict
ledger_transaction_aggregation_from_dict = LedgerTransactionAggregation.from_dict(ledger_transaction_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


