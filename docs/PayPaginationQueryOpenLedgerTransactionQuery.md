# PayPaginationQueryOpenLedgerTransactionQuery

分页查询

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** | 当前页码 | [optional] 
**size** | **int** | 每页大小 | [optional] 
**query** | [**OpenLedgerTransactionQuery**](OpenLedgerTransactionQuery.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_query_open_ledger_transaction_query import PayPaginationQueryOpenLedgerTransactionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationQueryOpenLedgerTransactionQuery from a JSON string
pay_pagination_query_open_ledger_transaction_query_instance = PayPaginationQueryOpenLedgerTransactionQuery.from_json(json)
# print the JSON string representation of the object
print(PayPaginationQueryOpenLedgerTransactionQuery.to_json())

# convert the object into a dict
pay_pagination_query_open_ledger_transaction_query_dict = pay_pagination_query_open_ledger_transaction_query_instance.to_dict()
# create an instance of PayPaginationQueryOpenLedgerTransactionQuery from a dict
pay_pagination_query_open_ledger_transaction_query_from_dict = PayPaginationQueryOpenLedgerTransactionQuery.from_dict(pay_pagination_query_open_ledger_transaction_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


