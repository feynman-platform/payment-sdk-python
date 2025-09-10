# MerchantToMerchantParams

商户间支付参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**Verification**](Verification.md) |  | [optional] 
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**payer** | **str** | 付款方，邮箱或merchantId | 
**payee** | **str** | 收款方，邮箱或merchantId | 
**time_id** | **str** | 汇率timeId，交易发生时使用的汇率记录 | 
**currency** | **str** | 货币类型 | 

## Example

```python
from buybtcpay.models.merchant_to_merchant_params import MerchantToMerchantParams

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantToMerchantParams from a JSON string
merchant_to_merchant_params_instance = MerchantToMerchantParams.from_json(json)
# print the JSON string representation of the object
print(MerchantToMerchantParams.to_json())

# convert the object into a dict
merchant_to_merchant_params_dict = merchant_to_merchant_params_instance.to_dict()
# create an instance of MerchantToMerchantParams from a dict
merchant_to_merchant_params_from_dict = MerchantToMerchantParams.from_dict(merchant_to_merchant_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


