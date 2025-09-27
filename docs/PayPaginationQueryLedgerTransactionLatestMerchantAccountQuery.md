# PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery

分页查询

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** | 当前页码 | [optional] 
**size** | **int** | 每页大小 | [optional] 
**query** | [**LedgerTransactionLatestMerchantAccountQuery**](LedgerTransactionLatestMerchantAccountQuery.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_query_ledger_transaction_latest_merchant_account_query import PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery from a JSON string
pay_pagination_query_ledger_transaction_latest_merchant_account_query_instance = PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery.from_json(json)
# print the JSON string representation of the object
print(PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery.to_json())

# convert the object into a dict
pay_pagination_query_ledger_transaction_latest_merchant_account_query_dict = pay_pagination_query_ledger_transaction_latest_merchant_account_query_instance.to_dict()
# create an instance of PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery from a dict
pay_pagination_query_ledger_transaction_latest_merchant_account_query_from_dict = PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery.from_dict(pay_pagination_query_ledger_transaction_latest_merchant_account_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


