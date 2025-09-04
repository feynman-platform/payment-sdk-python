# PaymentOrderEntity

支付单

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**order_id** | **str** |  | [optional] 
**merchant_id** | **str** | 该支付单所属商户ID | [optional] 
**channel_id** | **str** | 支付链路ID，跟踪支付流程，记账的业务ID也用这个 | [optional] 
**type** | **int** | 0: Merchant to merchant, 1: Withdrawal | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**fee** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**order_status** | **int** | 0: UNPAID, 1: PAYING, 2: SUCCESS, 3: FAIL, 4: CLOSE, 20: REFUNDED | [optional] 
**prepayment_order_id** | **int** |  | [optional] 
**bill_id** | **int** | 存储最后一次的流水号 | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.payment_order_entity import PaymentOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOrderEntity from a JSON string
payment_order_entity_instance = PaymentOrderEntity.from_json(json)
# print the JSON string representation of the object
print(PaymentOrderEntity.to_json())

# convert the object into a dict
payment_order_entity_dict = payment_order_entity_instance.to_dict()
# create an instance of PaymentOrderEntity from a dict
payment_order_entity_from_dict = PaymentOrderEntity.from_dict(payment_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


