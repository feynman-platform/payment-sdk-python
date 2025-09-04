# EnumDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**proto** | [**EnumDescriptorProto**](EnumDescriptorProto.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**containing_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**values** | [**List[EnumValueDescriptor]**](EnumValueDescriptor.md) |  | [optional] 
**closed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**EnumOptions**](EnumOptions.md) |  | [optional] 

## Example

```python
from buybtcpay.models.enum_descriptor import EnumDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of EnumDescriptor from a JSON string
enum_descriptor_instance = EnumDescriptor.from_json(json)
# print the JSON string representation of the object
print(EnumDescriptor.to_json())

# convert the object into a dict
enum_descriptor_dict = enum_descriptor_instance.to_dict()
# create an instance of EnumDescriptor from a dict
enum_descriptor_from_dict = EnumDescriptor.from_dict(enum_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


