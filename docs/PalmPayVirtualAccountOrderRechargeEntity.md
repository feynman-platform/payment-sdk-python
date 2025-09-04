# PalmPayVirtualAccountOrderRechargeEntity

虚拟账户充值订单关联平台充值

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**order_no** | **str** | 订单号 | [optional] 
**order_amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**recharge_merchant_id** | **str** | 平台充值商户ID | [optional] 
**recharge_business_id** | **str** | 平台充值业务ID，一般为审批单ID | [optional] 
**recharge_amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**recharge_status** | **int** | 0: Init, 1: Success, 2: Failed, 3: Closed, 4: Refunded | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_virtual_account_order_recharge_entity import PalmPayVirtualAccountOrderRechargeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayVirtualAccountOrderRechargeEntity from a JSON string
palm_pay_virtual_account_order_recharge_entity_instance = PalmPayVirtualAccountOrderRechargeEntity.from_json(json)
# print the JSON string representation of the object
print(PalmPayVirtualAccountOrderRechargeEntity.to_json())

# convert the object into a dict
palm_pay_virtual_account_order_recharge_entity_dict = palm_pay_virtual_account_order_recharge_entity_instance.to_dict()
# create an instance of PalmPayVirtualAccountOrderRechargeEntity from a dict
palm_pay_virtual_account_order_recharge_entity_from_dict = PalmPayVirtualAccountOrderRechargeEntity.from_dict(palm_pay_virtual_account_order_recharge_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


