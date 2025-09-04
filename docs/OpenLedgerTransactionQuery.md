# OpenLedgerTransactionQuery

商户账本查询

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**business_id** | **str** | 交易发生的业务ID，比如交易单号、充值单号等 | [optional] 
**channel_id** | **str** | 查询整个支付链路的交易记录 | [optional] 
**business_type** | **List[int]** | 交易类型，比如充值、提现、交易等 | [optional] 
**account_type** | **List[int]** | 账户类型，比如商户、商户冻结账户等 | [optional] 
**direction** | **List[int]** | 借：账户余额增加，贷：账户余额减少 | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 
**amount** | **List[str]** | 交易金额区间 | [optional] 
**balance** | **List[str]** |  | [optional] 

## Example

```python
from buybtcpay.models.open_ledger_transaction_query import OpenLedgerTransactionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OpenLedgerTransactionQuery from a JSON string
open_ledger_transaction_query_instance = OpenLedgerTransactionQuery.from_json(json)
# print the JSON string representation of the object
print(OpenLedgerTransactionQuery.to_json())

# convert the object into a dict
open_ledger_transaction_query_dict = open_ledger_transaction_query_instance.to_dict()
# create an instance of OpenLedgerTransactionQuery from a dict
open_ledger_transaction_query_from_dict = OpenLedgerTransactionQuery.from_dict(open_ledger_transaction_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


