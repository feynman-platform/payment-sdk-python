# PayoutRequestDto

商户发起代付请求时，按照此参数格式传递

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**order_id** | **str** | 商户唯一订单号，可用于查询交易结果 | 
**title** | **str** | 订单标题 | 
**description** | **str** | 订单描述 | [optional] 
**payee_name** | **str** | 收款方姓名（如果不传，默认为值是&#39;unknow&#39;） | [optional] 
**payee_bank_code** | **str** | 收款方银行或MMO编码 | 
**payee_bank_acc_no** | **str** | 为纯数字，不能带空格或特殊符号，取值见系统中的银行列表 | 
**amount** | **str** | 交易金额(标准单位计量) | 
**notify_url** | **str** | 接收代付结果通知url | [optional] 
**remark** | **str** | 备注信息 | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 

## Example

```python
from buybtcpay.models.payout_request_dto import PayoutRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutRequestDto from a JSON string
payout_request_dto_instance = PayoutRequestDto.from_json(json)
# print the JSON string representation of the object
print(PayoutRequestDto.to_json())

# convert the object into a dict
payout_request_dto_dict = payout_request_dto_instance.to_dict()
# create an instance of PayoutRequestDto from a dict
payout_request_dto_from_dict = PayoutRequestDto.from_dict(payout_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


