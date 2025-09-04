# PayoutEntityDto

代付信息

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**status** | **int** | 0: NORMAL, 1: DELETE | [optional] 
**merchant_id** | **str** | 代付记录所属商户 | [optional] 
**merchant_order_id** | **str** | 商户交易ID | [optional] 
**order_id** | **str** | 订单ID | [optional] 
**title** | **str** | 标题 | [optional] 
**description** | **str** | 描述 | [optional] 
**payee_name** | **str** | 收款人 | [optional] 
**payee_bank_code** | **str** | 收款人银行编码 | [optional] 
**payee_bank_acc_no** | **str** | 收款人银行卡号 | [optional] 
**payee_phone_no** | **str** | 收款人电话号码 | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**merchant_fee** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**refund** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**notify_url** | **str** | 通知地址 | [optional] 
**remark** | **str** | 备注 | [optional] 
**order_status** | **int** | 0: UNPAID, 1: PAYING, 2: SUCCESS, 3: FAIL, 4: CLOSE, 20: REFUNDED | [optional] 

## Example

```python
from buybtcpay.models.payout_entity_dto import PayoutEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutEntityDto from a JSON string
payout_entity_dto_instance = PayoutEntityDto.from_json(json)
# print the JSON string representation of the object
print(PayoutEntityDto.to_json())

# convert the object into a dict
payout_entity_dto_dict = payout_entity_dto_instance.to_dict()
# create an instance of PayoutEntityDto from a dict
payout_entity_dto_from_dict = PayoutEntityDto.from_dict(payout_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


