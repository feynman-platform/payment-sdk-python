# MerchantPayoutRequestDto

注册商户支付请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_name** | **str** | 收款方姓名（如果不传，默认为值是unknown） | [optional] 
**payee_bank_code** | **str** | 收款方银行或MMO编码 | 
**payee_bank_acc_no** | **str** | 收款方银行账户或MoMo账户账号为纯数字，不能带空格或特殊符号 | 
**amount** | **str** | 交易金额(标准单位计量) | 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**remark** | **str** | 备注信息 | 

## Example

```python
from buybtcpay.models.merchant_payout_request_dto import MerchantPayoutRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPayoutRequestDto from a JSON string
merchant_payout_request_dto_instance = MerchantPayoutRequestDto.from_json(json)
# print the JSON string representation of the object
print(MerchantPayoutRequestDto.to_json())

# convert the object into a dict
merchant_payout_request_dto_dict = merchant_payout_request_dto_instance.to_dict()
# create an instance of MerchantPayoutRequestDto from a dict
merchant_payout_request_dto_from_dict = MerchantPayoutRequestDto.from_dict(merchant_payout_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


