# EnumValueDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**options_or_builder** | [**EnumValueOptionsOrBuilder**](EnumValueOptionsOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**options** | [**EnumValueOptions**](EnumValueOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**EnumValueDescriptorProto**](EnumValueDescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_value_descriptor_proto import EnumValueDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of EnumValueDescriptorProto from a JSON string
enum_value_descriptor_proto_instance = EnumValueDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(EnumValueDescriptorProto.to_json())

# convert the object into a dict
enum_value_descriptor_proto_dict = enum_value_descriptor_proto_instance.to_dict()
# create an instance of EnumValueDescriptorProto from a dict
enum_value_descriptor_proto_from_dict = EnumValueDescriptorProto.from_dict(enum_value_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


