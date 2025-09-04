# CreatePrepaymentOrderDto

创建预付订单请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**business_id** | **str** | 第三方业务ID，由调用方生成，用于标识订单的唯一性 | 
**merchant_id** | **str** | 代付平台的商户ID，可以是商户ID，也可以是子商户ID | 
**type** | **int** | 0: Merchant to merchant, 1: Withdrawal | [optional] 
**amount** | **str** | 预付金额，为方便前端调用，请传标准单位，比如想要转1.23元，直接传1.23即可，系统会将其转为最小单位：123分 | 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 

## Example

```python
from buybtcpay.models.create_prepayment_order_dto import CreatePrepaymentOrderDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrepaymentOrderDto from a JSON string
create_prepayment_order_dto_instance = CreatePrepaymentOrderDto.from_json(json)
# print the JSON string representation of the object
print(CreatePrepaymentOrderDto.to_json())

# convert the object into a dict
create_prepayment_order_dto_dict = create_prepayment_order_dto_instance.to_dict()
# create an instance of CreatePrepaymentOrderDto from a dict
create_prepayment_order_dto_from_dict = CreatePrepaymentOrderDto.from_dict(create_prepayment_order_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


