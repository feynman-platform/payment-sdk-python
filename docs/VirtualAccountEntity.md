# VirtualAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**account_merchant** | [**MerchantEntity**](MerchantEntity.md) |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**parent_merchant_id** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.virtual_account_entity import VirtualAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountEntity from a JSON string
virtual_account_entity_instance = VirtualAccountEntity.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountEntity.to_json())

# convert the object into a dict
virtual_account_entity_dict = virtual_account_entity_instance.to_dict()
# create an instance of VirtualAccountEntity from a dict
virtual_account_entity_from_dict = VirtualAccountEntity.from_dict(virtual_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


