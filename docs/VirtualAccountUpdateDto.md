# VirtualAccountUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**status** | **str** | 商户状态 | 

## Example

```python
from buybtcpay.models.virtual_account_update_dto import VirtualAccountUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountUpdateDto from a JSON string
virtual_account_update_dto_instance = VirtualAccountUpdateDto.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountUpdateDto.to_json())

# convert the object into a dict
virtual_account_update_dto_dict = virtual_account_update_dto_instance.to_dict()
# create an instance of VirtualAccountUpdateDto from a dict
virtual_account_update_dto_from_dict = VirtualAccountUpdateDto.from_dict(virtual_account_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


