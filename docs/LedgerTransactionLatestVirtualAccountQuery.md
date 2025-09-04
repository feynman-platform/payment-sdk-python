# LedgerTransactionLatestVirtualAccountQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**parent_merchant_id** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.ledger_transaction_latest_virtual_account_query import LedgerTransactionLatestVirtualAccountQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTransactionLatestVirtualAccountQuery from a JSON string
ledger_transaction_latest_virtual_account_query_instance = LedgerTransactionLatestVirtualAccountQuery.from_json(json)
# print the JSON string representation of the object
print(LedgerTransactionLatestVirtualAccountQuery.to_json())

# convert the object into a dict
ledger_transaction_latest_virtual_account_query_dict = ledger_transaction_latest_virtual_account_query_instance.to_dict()
# create an instance of LedgerTransactionLatestVirtualAccountQuery from a dict
ledger_transaction_latest_virtual_account_query_from_dict = LedgerTransactionLatestVirtualAccountQuery.from_dict(ledger_transaction_latest_virtual_account_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


