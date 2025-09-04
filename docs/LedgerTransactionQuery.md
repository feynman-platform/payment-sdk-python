# LedgerTransactionQuery

账本分页查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**business_type** | **List[int]** | 业务类型 | [optional] 
**account_type** | **List[int]** | 账户类型 | [optional] 
**account_no** | **str** |  | [optional] 
**parent_merchant_id** | **str** |  | [optional] 
**direction** | **List[int]** | 交易方向 | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 
**amount** | **List[str]** | 金额，需要与币种一起使用 | [optional] 
**balance** | **List[str]** | 余额，需要与币种一起使用 | [optional] 

## Example

```python
from buybtcpay.models.ledger_transaction_query import LedgerTransactionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTransactionQuery from a JSON string
ledger_transaction_query_instance = LedgerTransactionQuery.from_json(json)
# print the JSON string representation of the object
print(LedgerTransactionQuery.to_json())

# convert the object into a dict
ledger_transaction_query_dict = ledger_transaction_query_instance.to_dict()
# create an instance of LedgerTransactionQuery from a dict
ledger_transaction_query_from_dict = LedgerTransactionQuery.from_dict(ledger_transaction_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


