# LedgerTransactionEntity

记账本，采用复式记账的分录方式

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**channel_id** | **str** | 支付链路ID，跟踪支付流程，为了兼容旧数据，此字段可以为空 | [optional] 
**business_type** | **int** | 1: Bulk transaction, 10: Virtual account recharge, 11: Merchant self service recharge, 12: Palmpay virtual account recharge, 2: Refund, 3: Payout, 200: Transfer, 202: Withdrawal, 203: Trade transfer, 4: Frozen, 5: Fee, 6: Platform recharge, 7: Unfrozen, 8: Merchant to merchant, 81: Currency exchange, 300: Reversal platform to wallet, 301: Reversal wallet to platform, 302: Reversal wallet to wallet, 103: Reversal platform to bank, 100: Reversal platform to merchant, 101: Reversal merchant to platform, 102: Reversal merchant to merchant | [optional] 
**account_type** | **int** | 1: Platform, 2: Merchant, 22: Virtual account, 21: Merchant Frozen, 3: Bank | [optional] 
**account_no** | **str** |  | [optional] 
**direction** | **int** | 1: Debit, 2: Credit | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**balance** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**wallet_id** | **str** | 钱包ID | [optional] 
**wallet_type** | **str** | 钱包类型 | [optional] 
**counterparty_account_type** | **int** | 1: Platform, 2: Merchant, 22: Virtual account, 21: Merchant Frozen, 3: Bank | [optional] 
**counterparty_account_no** | **str** | 交易对方账户号码 | [optional] 
**counterparty_wallet_id** | **str** | 交易对方钱包ID | [optional] 
**extra** | **Dict[str, object]** | 交易附加信息，比如转账备注、跨币种交易汇率、值附加信息等 | [optional] 

## Example

```python
from buybtcpay.models.ledger_transaction_entity import LedgerTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTransactionEntity from a JSON string
ledger_transaction_entity_instance = LedgerTransactionEntity.from_json(json)
# print the JSON string representation of the object
print(LedgerTransactionEntity.to_json())

# convert the object into a dict
ledger_transaction_entity_dict = ledger_transaction_entity_instance.to_dict()
# create an instance of LedgerTransactionEntity from a dict
ledger_transaction_entity_from_dict = LedgerTransactionEntity.from_dict(ledger_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


