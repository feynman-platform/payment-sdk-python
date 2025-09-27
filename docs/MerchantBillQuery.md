# MerchantBillQuery

商户收支分页查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**from_channel** | **str** | 查询渠道 | [optional] 
**operator** | **str** | 发起查询的商户ID | [optional] 
**business_ids** | **List[str]** | 商户账单ID列表 | [optional] 
**business_id** | **str** | 业务ID | [optional] 
**channel_id** | **str** | 支付路ID | [optional] 
**merchant_id** | **List[str]** | 商户ID列表 | [optional] 
**business_type** | **List[int]** | 业务类型 | [optional] 
**account_type** | **List[int]** | 账户类型 | [optional] 
**counterparty_account_type** | **List[int]** | 交易对方账户类型 | [optional] 
**account_no** | **str** | 账户号码 | [optional] 
**counterparty_account_no** | **str** | 交易对方账户号码 | [optional] 
**direction** | **List[int]** | 交易方向 | [optional] 
**bill_status** | **List[int]** | 交易状态 | [optional] 
**currency** | **List[str]** | 币种 | [optional] 
**amount** | **List[str]** | 金额，需要与币种一起使用 | [optional] 
**wallet_type** | **str** | 钱包类型 | [optional] 
**wallet_id** | **List[str]** | 钱包ID | [optional] 

## Example

```python
from buybtcpay.models.merchant_bill_query import MerchantBillQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBillQuery from a JSON string
merchant_bill_query_instance = MerchantBillQuery.from_json(json)
# print the JSON string representation of the object
print(MerchantBillQuery.to_json())

# convert the object into a dict
merchant_bill_query_dict = merchant_bill_query_instance.to_dict()
# create an instance of MerchantBillQuery from a dict
merchant_bill_query_from_dict = MerchantBillQuery.from_dict(merchant_bill_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


