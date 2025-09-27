# MerchantTradeTransferByBusinessIdDto

基于预付单的商户到商户转账请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_merchant_id** | **str** | 收款方商户ID或邮箱，资金将会转入收款方的交易账户 | [optional] 
**payee_operator_id** | **str** | 谁在操作这笔交易，如果不传，则会使用钱包属性商户 | [optional] 

## Example

```python
from buybtcpay.models.merchant_trade_transfer_by_business_id_dto import MerchantTradeTransferByBusinessIdDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantTradeTransferByBusinessIdDto from a JSON string
merchant_trade_transfer_by_business_id_dto_instance = MerchantTradeTransferByBusinessIdDto.from_json(json)
# print the JSON string representation of the object
print(MerchantTradeTransferByBusinessIdDto.to_json())

# convert the object into a dict
merchant_trade_transfer_by_business_id_dto_dict = merchant_trade_transfer_by_business_id_dto_instance.to_dict()
# create an instance of MerchantTradeTransferByBusinessIdDto from a dict
merchant_trade_transfer_by_business_id_dto_from_dict = MerchantTradeTransferByBusinessIdDto.from_dict(merchant_trade_transfer_by_business_id_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


