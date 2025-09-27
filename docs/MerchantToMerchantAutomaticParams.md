# MerchantToMerchantAutomaticParams

商户到商户转账，不需要提前创建预付单

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**Verification**](Verification.md) |  | [optional] 
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**payer** | **str** | 付款方商户ID或邮箱 | 
**payee** | **str** | 收款方商户ID或邮箱 | 
**payee_operator_id** | **str** | 如果不传，就使用钱包的拥有者 | [optional] 
**amount** | **str** | 转账金额 | 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 

## Example

```python
from buybtcpay.models.merchant_to_merchant_automatic_params import MerchantToMerchantAutomaticParams

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantToMerchantAutomaticParams from a JSON string
merchant_to_merchant_automatic_params_instance = MerchantToMerchantAutomaticParams.from_json(json)
# print the JSON string representation of the object
print(MerchantToMerchantAutomaticParams.to_json())

# convert the object into a dict
merchant_to_merchant_automatic_params_dict = merchant_to_merchant_automatic_params_instance.to_dict()
# create an instance of MerchantToMerchantAutomaticParams from a dict
merchant_to_merchant_automatic_params_from_dict = MerchantToMerchantAutomaticParams.from_dict(merchant_to_merchant_automatic_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


