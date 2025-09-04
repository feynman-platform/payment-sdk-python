# PrepaymentOrderEntity

预付单

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**business_id** | **str** | 业务ID，全局唯一，作为是否重复支付的依据 | [optional] 
**channel_id** | **str** | 支付链路ID，跟踪支付流程，记账的业务ID也用这个 | [optional] 
**merchant_id** | **str** | 该预付单所属商户ID | [optional] 
**type** | **int** | 0: Merchant to merchant, 1: Withdrawal | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**fee** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**order_status** | **int** | 0: Frozen, 1: Closed, 2: Paying, 3: Paid, 4: Failed | [optional] 
**payment_order_id** | **int** | 最后一次支付关联的支付单id | [optional] 
**bill_id** | **int** | 预付单可能修改金额，流水号会变动，存储最后一次的流水号 | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.prepayment_order_entity import PrepaymentOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PrepaymentOrderEntity from a JSON string
prepayment_order_entity_instance = PrepaymentOrderEntity.from_json(json)
# print the JSON string representation of the object
print(PrepaymentOrderEntity.to_json())

# convert the object into a dict
prepayment_order_entity_dict = prepayment_order_entity_instance.to_dict()
# create an instance of PrepaymentOrderEntity from a dict
prepayment_order_entity_from_dict = PrepaymentOrderEntity.from_dict(prepayment_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


