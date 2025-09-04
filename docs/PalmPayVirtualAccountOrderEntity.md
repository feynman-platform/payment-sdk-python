# PalmPayVirtualAccountOrderEntity

PalmPay虚拟账户订单

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**order_no** | **str** | PalmPay订单号 | [optional] 
**order_status** | **int** | 0: Init, 1: Success(Only this status will receive pay in order notifications), 2: Failed, 3: Processing, 4: Closed, 5: Refunded, 999: Unknown | [optional] 
**order_created_time** | **datetime** | 订单创建时间 | [optional] 
**order_update_time** | **datetime** | 订单修改时间 | [optional] 
**order_amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**payer_account_no** | **str** | 付款方账户号码 | [optional] 
**payer_account_name** | **str** | 付款方账户名称 | [optional] 
**payer_bank_name** | **str** | 付款方银行 | [optional] 
**virtual_account_no** | **str** | 只有向虚拟账号入金才会返回，向商户主账户入金不会返回 | [optional] 
**virtual_account_name** | **str** | 只有向虚拟账号入金才会返回，向商户主账户入金不会返回 | [optional] 
**account_reference** | **str** | 虚拟账户备注字段 | [optional] 
**session_id** | **str** | 渠道响应参数 | [optional] 
**sign** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_virtual_account_order_entity import PalmPayVirtualAccountOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayVirtualAccountOrderEntity from a JSON string
palm_pay_virtual_account_order_entity_instance = PalmPayVirtualAccountOrderEntity.from_json(json)
# print the JSON string representation of the object
print(PalmPayVirtualAccountOrderEntity.to_json())

# convert the object into a dict
palm_pay_virtual_account_order_entity_dict = palm_pay_virtual_account_order_entity_instance.to_dict()
# create an instance of PalmPayVirtualAccountOrderEntity from a dict
palm_pay_virtual_account_order_entity_from_dict = PalmPayVirtualAccountOrderEntity.from_dict(palm_pay_virtual_account_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


