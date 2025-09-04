# FieldDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**proto** | [**FieldDescriptorProto**](FieldDescriptorProto.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**json_name** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**extension_scope** | [**Descriptor**](Descriptor.md) |  | [optional] 
**type** | **str** |  | [optional] 
**containing_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**message_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**containing_oneof** | [**OneofDescriptor**](OneofDescriptor.md) |  | [optional] 
**enum_type** | [**EnumDescriptor**](EnumDescriptor.md) |  | [optional] 
**default_value** | **object** |  | [optional] 
**extension** | **bool** |  | [optional] 
**lite_java_type** | **str** |  | [optional] 
**lite_type** | **str** |  | [optional] 
**packed** | **bool** |  | [optional] 
**packable** | **bool** |  | [optional] 
**real_containing_oneof** | [**OneofDescriptor**](OneofDescriptor.md) |  | [optional] 
**java_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**required** | **bool** |  | [optional] 
**options** | [**FieldOptions**](FieldOptions.md) |  | [optional] 
**optional** | **bool** |  | [optional] 
**repeated** | **bool** |  | [optional] 
**map_field** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.field_descriptor import FieldDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDescriptor from a JSON string
field_descriptor_instance = FieldDescriptor.from_json(json)
# print the JSON string representation of the object
print(FieldDescriptor.to_json())

# convert the object into a dict
field_descriptor_dict = field_descriptor_instance.to_dict()
# create an instance of FieldDescriptor from a dict
field_descriptor_from_dict = FieldDescriptor.from_dict(field_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


