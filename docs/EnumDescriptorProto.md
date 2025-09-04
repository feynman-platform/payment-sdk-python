# EnumDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**reserved_range_list** | [**List[EnumReservedRange]**](EnumReservedRange.md) |  | [optional] 
**reserved_name_list** | **List[str]** |  | [optional] 
**value_count** | **int** |  | [optional] 
**options_or_builder** | [**EnumOptionsOrBuilder**](EnumOptionsOrBuilder.md) |  | [optional] 
**reserved_range_or_builder_list** | [**List[EnumReservedRangeOrBuilder]**](EnumReservedRangeOrBuilder.md) |  | [optional] 
**reserved_range_count** | **int** |  | [optional] 
**reserved_name_count** | **int** |  | [optional] 
**value_list** | [**List[EnumValueDescriptorProto]**](EnumValueDescriptorProto.md) |  | [optional] 
**value_or_builder_list** | [**List[EnumValueDescriptorProtoOrBuilder]**](EnumValueDescriptorProtoOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**EnumOptions**](EnumOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**EnumDescriptorProto**](EnumDescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_descriptor_proto import EnumDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of EnumDescriptorProto from a JSON string
enum_descriptor_proto_instance = EnumDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(EnumDescriptorProto.to_json())

# convert the object into a dict
enum_descriptor_proto_dict = enum_descriptor_proto_instance.to_dict()
# create an instance of EnumDescriptorProto from a dict
enum_descriptor_proto_from_dict = EnumDescriptorProto.from_dict(enum_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


