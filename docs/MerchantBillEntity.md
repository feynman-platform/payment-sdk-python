# MerchantBillEntity

商户交易流水，记录商户的收入、支出相关信息，该账本只关注商户账户的出支，不关心冻结账户等中间账户

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**merchant_id** | **str** | 所属商户ID | [optional] 
**channel_id** | **str** | 支付链路ID，跟踪支付流程，记账的业务ID也用这个 | [optional] 
**business_type** | **int** | 1: Recharge, 10: Virtual account recharge, 2: Refund, 3: Transfer, 4: Frozen, 5: Fee, 6: Platform recharge, 7: Unfrozen, 8: Merchant to merchant, 81: Merchant to merchant different currency, 100: Reversal platform to merchant, 101: Reversal merchant to platform, 102: Reversal merchant to merchant | [optional] 
**account_type** | **int** | 1: Platform, 2: Merchant, 22: Virtual account, 21: Merchant Frozen, 3: Bank | [optional] 
**account_no** | **str** |  | [optional] 
**direction** | **int** | 1: Debit, 2: Credit | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**counterparty_account_type** | **int** | 1: Platform, 2: Merchant, 22: Virtual account, 21: Merchant Frozen, 3: Bank | [optional] 
**counterparty_account_no** | **str** | 交易对方账户号码 | [optional] 
**bill_status** | **int** | 0: Initiated, 1: Processing, 2: Success, 3: Failed, 4: Canceled, 5: Closed, 6: Refunded | [optional] 
**extra** | [**MerchantBillExtra**](MerchantBillExtra.md) |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_bill_entity import MerchantBillEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBillEntity from a JSON string
merchant_bill_entity_instance = MerchantBillEntity.from_json(json)
# print the JSON string representation of the object
print(MerchantBillEntity.to_json())

# convert the object into a dict
merchant_bill_entity_dict = merchant_bill_entity_instance.to_dict()
# create an instance of MerchantBillEntity from a dict
merchant_bill_entity_from_dict = MerchantBillEntity.from_dict(merchant_bill_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


