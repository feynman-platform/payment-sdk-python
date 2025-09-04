# MerchantEntityDto

商户信息

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**status** | **int** | 0: NORMAL, 1: DELETE | [optional] 
**merchant_id** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | **int** | 0: System manager, 1: Manager, 99: Merchant, 900: Merchant Open API, 999: Visitor | [optional] 
**merchant_status** | **int** | 0: NORMAL, 1: DISABLED | [optional] 
**palm_pay_virtual_account_no** | **str** | PalmPay虚拟账户 | [optional] 
**note** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**virtual_account_id** | **int** | 虚拟商户的ID | [optional] 

## Example

```python
from buybtcpay.models.merchant_entity_dto import MerchantEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantEntityDto from a JSON string
merchant_entity_dto_instance = MerchantEntityDto.from_json(json)
# print the JSON string representation of the object
print(MerchantEntityDto.to_json())

# convert the object into a dict
merchant_entity_dto_dict = merchant_entity_dto_instance.to_dict()
# create an instance of MerchantEntityDto from a dict
merchant_entity_dto_from_dict = MerchantEntityDto.from_dict(merchant_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


