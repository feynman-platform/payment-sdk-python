# LedgerTransactionLatestMerchantAccountQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**tag** | **List[str]** |  | [optional] 
**currency** | **str** | 货币类型 | [optional] 

## Example

```python
from buybtcpay.models.ledger_transaction_latest_merchant_account_query import LedgerTransactionLatestMerchantAccountQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTransactionLatestMerchantAccountQuery from a JSON string
ledger_transaction_latest_merchant_account_query_instance = LedgerTransactionLatestMerchantAccountQuery.from_json(json)
# print the JSON string representation of the object
print(LedgerTransactionLatestMerchantAccountQuery.to_json())

# convert the object into a dict
ledger_transaction_latest_merchant_account_query_dict = ledger_transaction_latest_merchant_account_query_instance.to_dict()
# create an instance of LedgerTransactionLatestMerchantAccountQuery from a dict
ledger_transaction_latest_merchant_account_query_from_dict = LedgerTransactionLatestMerchantAccountQuery.from_dict(ledger_transaction_latest_merchant_account_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


