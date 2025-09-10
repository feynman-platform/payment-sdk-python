# EnumDescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options_or_builder** | [**EnumOptionsOrBuilder**](EnumOptionsOrBuilder.md) |  | [optional] 
**reserved_range_or_builder_list** | [**List[EnumReservedRangeOrBuilder]**](EnumReservedRangeOrBuilder.md) |  | [optional] 
**reserved_range_count** | **int** |  | [optional] 
**reserved_name_count** | **int** |  | [optional] 
**reserved_range_list** | [**List[EnumReservedRange]**](EnumReservedRange.md) |  | [optional] 
**reserved_name_list** | **List[str]** |  | [optional] 
**value_count** | **int** |  | [optional] 
**value_list** | [**List[EnumValueDescriptorProto]**](EnumValueDescriptorProto.md) |  | [optional] 
**value_or_builder_list** | [**List[EnumValueDescriptorProtoOrBuilder]**](EnumValueDescriptorProtoOrBuilder.md) |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**EnumOptions**](EnumOptions.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of EnumDescriptorProtoOrBuilder from a JSON string
enum_descriptor_proto_or_builder_instance = EnumDescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(EnumDescriptorProtoOrBuilder.to_json())

# convert the object into a dict
enum_descriptor_proto_or_builder_dict = enum_descriptor_proto_or_builder_instance.to_dict()
# create an instance of EnumDescriptorProtoOrBuilder from a dict
enum_descriptor_proto_or_builder_from_dict = EnumDescriptorProtoOrBuilder.from_dict(enum_descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


