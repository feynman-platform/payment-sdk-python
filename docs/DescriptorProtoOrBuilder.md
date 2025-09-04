# DescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**name** | **str** |  | [optional] 
**options** | [**MessageOptions**](MessageOptions.md) |  | [optional] 
**field_list** | [**List[FieldDescriptorProto]**](FieldDescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.descriptor_proto_or_builder import DescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptorProtoOrBuilder from a JSON string
descriptor_proto_or_builder_instance = DescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(DescriptorProtoOrBuilder.to_json())

# convert the object into a dict
descriptor_proto_or_builder_dict = descriptor_proto_or_builder_instance.to_dict()
# create an instance of DescriptorProtoOrBuilder from a dict
descriptor_proto_or_builder_from_dict = DescriptorProtoOrBuilder.from_dict(descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


