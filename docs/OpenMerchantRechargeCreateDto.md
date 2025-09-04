# OpenMerchantRechargeCreateDto

开放接口创建充值审批单

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | 充值金额，需要*100，比如总值100，value应该为10000，最大金额为10000000000（实际金额为1亿） | 
**note** | **str** |  | [optional] 
**merchant_id** | **str** | 要充值的商户ID | 

## Example

```python
from buybtcpay.models.open_merchant_recharge_create_dto import OpenMerchantRechargeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenMerchantRechargeCreateDto from a JSON string
open_merchant_recharge_create_dto_instance = OpenMerchantRechargeCreateDto.from_json(json)
# print the JSON string representation of the object
print(OpenMerchantRechargeCreateDto.to_json())

# convert the object into a dict
open_merchant_recharge_create_dto_dict = open_merchant_recharge_create_dto_instance.to_dict()
# create an instance of OpenMerchantRechargeCreateDto from a dict
open_merchant_recharge_create_dto_from_dict = OpenMerchantRechargeCreateDto.from_dict(open_merchant_recharge_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


