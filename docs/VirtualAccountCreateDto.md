# VirtualAccountCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | 
**external_id** | **str** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.virtual_account_create_dto import VirtualAccountCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountCreateDto from a JSON string
virtual_account_create_dto_instance = VirtualAccountCreateDto.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountCreateDto.to_json())

# convert the object into a dict
virtual_account_create_dto_dict = virtual_account_create_dto_instance.to_dict()
# create an instance of VirtualAccountCreateDto from a dict
virtual_account_create_dto_from_dict = VirtualAccountCreateDto.from_dict(virtual_account_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


