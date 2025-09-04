# UpdatePrepaymentOrderAmountDto

更新预付订单金额请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_id** | **str** | 业务ID | 
**amount** | **str** | 金额，传对应币种的标准单位 | 

## Example

```python
from buybtcpay.models.update_prepayment_order_amount_dto import UpdatePrepaymentOrderAmountDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePrepaymentOrderAmountDto from a JSON string
update_prepayment_order_amount_dto_instance = UpdatePrepaymentOrderAmountDto.from_json(json)
# print the JSON string representation of the object
print(UpdatePrepaymentOrderAmountDto.to_json())

# convert the object into a dict
update_prepayment_order_amount_dto_dict = update_prepayment_order_amount_dto_instance.to_dict()
# create an instance of UpdatePrepaymentOrderAmountDto from a dict
update_prepayment_order_amount_dto_from_dict = UpdatePrepaymentOrderAmountDto.from_dict(update_prepayment_order_amount_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


