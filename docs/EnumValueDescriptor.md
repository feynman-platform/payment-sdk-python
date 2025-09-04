# EnumValueDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**proto** | [**EnumValueDescriptorProto**](EnumValueDescriptorProto.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**type** | [**EnumDescriptor**](EnumDescriptor.md) |  | [optional] 
**name** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**number** | **int** |  | [optional] 
**options** | [**EnumValueOptions**](EnumValueOptions.md) |  | [optional] 

## Example

```python
from buybtcpay.models.enum_value_descriptor import EnumValueDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of EnumValueDescriptor from a JSON string
enum_value_descriptor_instance = EnumValueDescriptor.from_json(json)
# print the JSON string representation of the object
print(EnumValueDescriptor.to_json())

# convert the object into a dict
enum_value_descriptor_dict = enum_value_descriptor_instance.to_dict()
# create an instance of EnumValueDescriptor from a dict
enum_value_descriptor_from_dict = EnumValueDescriptor.from_dict(enum_value_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


