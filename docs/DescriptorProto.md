# DescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**reserved_range_list** | [**List[ReservedRange]**](ReservedRange.md) |  | [optional] 
**reserved_name_list** | **List[str]** |  | [optional] 
**extension_range_list** | [**List[ExtensionRange]**](ExtensionRange.md) |  | [optional] 
**oneof_decl_count** | **int** |  | [optional] 
**nested_type_count** | **int** |  | [optional] 
**enum_type_count** | **int** |  | [optional] 
**extension_count** | **int** |  | [optional] 
**extension_range_count** | **int** |  | [optional] 
**field_or_builder_list** | [**List[FieldDescriptorProtoOrBuilder]**](FieldDescriptorProtoOrBuilder.md) |  | [optional] 
**extension_list** | [**List[FieldDescriptorProto]**](FieldDescriptorProto.md) |  | [optional] 
**extension_or_builder_list** | [**List[FieldDescriptorProtoOrBuilder]**](FieldDescriptorProtoOrBuilder.md) |  | [optional] 
**nested_type_list** | [**List[DescriptorProto]**](DescriptorProto.md) |  | [optional] 
**nested_type_or_builder_list** | [**List[DescriptorProtoOrBuilder]**](DescriptorProtoOrBuilder.md) |  | [optional] 
**enum_type_list** | [**List[EnumDescriptorProto]**](EnumDescriptorProto.md) |  | [optional] 
**enum_type_or_builder_list** | [**List[EnumDescriptorProtoOrBuilder]**](EnumDescriptorProtoOrBuilder.md) |  | [optional] 
**extension_range_or_builder_list** | [**List[ExtensionRangeOrBuilder]**](ExtensionRangeOrBuilder.md) |  | [optional] 
**oneof_decl_list** | [**List[OneofDescriptorProto]**](OneofDescriptorProto.md) |  | [optional] 
**oneof_decl_or_builder_list** | [**List[OneofDescriptorProtoOrBuilder]**](OneofDescriptorProtoOrBuilder.md) |  | [optional] 
**options_or_builder** | [**MessageOptionsOrBuilder**](MessageOptionsOrBuilder.md) |  | [optional] 
**reserved_range_or_builder_list** | [**List[ReservedRangeOrBuilder]**](ReservedRangeOrBuilder.md) |  | [optional] 
**reserved_range_count** | **int** |  | [optional] 
**reserved_name_count** | **int** |  | [optional] 
**field_count** | **int** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**MessageOptions**](MessageOptions.md) |  | [optional] 
**field_list** | [**List[FieldDescriptorProto]**](FieldDescriptorProto.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**DescriptorProto**](DescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.descriptor_proto import DescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptorProto from a JSON string
descriptor_proto_instance = DescriptorProto.from_json(json)
# print the JSON string representation of the object
print(DescriptorProto.to_json())

# convert the object into a dict
descriptor_proto_dict = descriptor_proto_instance.to_dict()
# create an instance of DescriptorProto from a dict
descriptor_proto_from_dict = DescriptorProto.from_dict(descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


