# EnumValueDescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options_or_builder** | [**EnumValueOptionsOrBuilder**](EnumValueOptionsOrBuilder.md) |  | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**options** | [**EnumValueOptions**](EnumValueOptions.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of EnumValueDescriptorProtoOrBuilder from a JSON string
enum_value_descriptor_proto_or_builder_instance = EnumValueDescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(EnumValueDescriptorProtoOrBuilder.to_json())

# convert the object into a dict
enum_value_descriptor_proto_or_builder_dict = enum_value_descriptor_proto_or_builder_instance.to_dict()
# create an instance of EnumValueDescriptorProtoOrBuilder from a dict
enum_value_descriptor_proto_or_builder_from_dict = EnumValueDescriptorProtoOrBuilder.from_dict(enum_value_descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


