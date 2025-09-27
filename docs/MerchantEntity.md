# MerchantEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | **int** | 0: System manager, 1: Manager, 99: Merchant, 900: Merchant Open API, 999: Visitor | [optional] 
**merchant_status** | **int** | 0: NORMAL, 1: DISABLED | [optional] 
**palm_pay_virtual_account_no** | **str** | PalmPay虚拟账户 | [optional] 
**note** | **str** |  | [optional] 
**virtual_account_id** | **int** |  | [optional] 
**virtual_account_id_backup** | **int** |  | [optional] 
**tag** | **str** | 商户标签，可以为空 | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_entity import MerchantEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantEntity from a JSON string
merchant_entity_instance = MerchantEntity.from_json(json)
# print the JSON string representation of the object
print(MerchantEntity.to_json())

# convert the object into a dict
merchant_entity_dict = merchant_entity_instance.to_dict()
# create an instance of MerchantEntity from a dict
merchant_entity_from_dict = MerchantEntity.from_dict(merchant_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


