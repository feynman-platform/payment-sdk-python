# CreateTradePrepaymentOrderDto

创建交易业务预付单，冻结商户交易账户金额

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**Verification**](Verification.md) |  | [optional] 
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**business_id** | **str** | 第三方业务ID，由调用方生成，用于标识订单的唯一性 | 
**operator** | **str** | 发起交易的商户ID | 
**amount** | **str** | 预付金额，为方便前端调用，请传标准单位，比如想要转1.23元，直接传1.23即可，系统会将其转为最小单位：123分 | 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**wallet_id** | **str** | 如果不传，则会查找商户下的资金钱包 | [optional] 
**auto_choose_wallet** | **bool** | 如果指定的钱包余额不足，系统主动查找余额最多的钱包支付 | [optional] 

## Example

```python
from buybtcpay.models.create_trade_prepayment_order_dto import CreateTradePrepaymentOrderDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradePrepaymentOrderDto from a JSON string
create_trade_prepayment_order_dto_instance = CreateTradePrepaymentOrderDto.from_json(json)
# print the JSON string representation of the object
print(CreateTradePrepaymentOrderDto.to_json())

# convert the object into a dict
create_trade_prepayment_order_dto_dict = create_trade_prepayment_order_dto_instance.to_dict()
# create an instance of CreateTradePrepaymentOrderDto from a dict
create_trade_prepayment_order_dto_from_dict = CreateTradePrepaymentOrderDto.from_dict(create_trade_prepayment_order_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


