# MerchantRechargeCreateDto

创建商户充值审批单

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | 充值金额，需要*100，比如总值100，value应该为10000，最大金额为10000000000（实际金额为1亿） | 
**note** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_recharge_create_dto import MerchantRechargeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantRechargeCreateDto from a JSON string
merchant_recharge_create_dto_instance = MerchantRechargeCreateDto.from_json(json)
# print the JSON string representation of the object
print(MerchantRechargeCreateDto.to_json())

# convert the object into a dict
merchant_recharge_create_dto_dict = merchant_recharge_create_dto_instance.to_dict()
# create an instance of MerchantRechargeCreateDto from a dict
merchant_recharge_create_dto_from_dict = MerchantRechargeCreateDto.from_dict(merchant_recharge_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


