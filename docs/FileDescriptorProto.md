# FileDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**enum_type_count** | **int** |  | [optional] 
**extension_count** | **int** |  | [optional] 
**syntax** | **str** |  | [optional] 
**extension_list** | [**List[FieldDescriptorProto]**](FieldDescriptorProto.md) |  | [optional] 
**extension_or_builder_list** | [**List[FieldDescriptorProtoOrBuilder]**](FieldDescriptorProtoOrBuilder.md) |  | [optional] 
**public_dependency_count** | **int** |  | [optional] 
**dependency_count** | **int** |  | [optional] 
**message_type_count** | **int** |  | [optional] 
**service_count** | **int** |  | [optional] 
**enum_type_list** | [**List[EnumDescriptorProto]**](EnumDescriptorProto.md) |  | [optional] 
**enum_type_or_builder_list** | [**List[EnumDescriptorProtoOrBuilder]**](EnumDescriptorProtoOrBuilder.md) |  | [optional] 
**options_or_builder** | [**FileOptionsOrBuilder**](FileOptionsOrBuilder.md) |  | [optional] 
**edition** | **str** |  | [optional] 
**package_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**dependency_list** | **List[str]** |  | [optional] 
**public_dependency_list** | **List[int]** |  | [optional] 
**weak_dependency_list** | **List[int]** |  | [optional] 
**weak_dependency_count** | **int** |  | [optional] 
**message_type_list** | [**List[DescriptorProto]**](DescriptorProto.md) |  | [optional] 
**message_type_or_builder_list** | [**List[DescriptorProtoOrBuilder]**](DescriptorProtoOrBuilder.md) |  | [optional] 
**service_list** | [**List[ServiceDescriptorProto]**](ServiceDescriptorProto.md) |  | [optional] 
**service_or_builder_list** | [**List[ServiceDescriptorProtoOrBuilder]**](ServiceDescriptorProtoOrBuilder.md) |  | [optional] 
**source_code_info** | [**SourceCodeInfo**](SourceCodeInfo.md) |  | [optional] 
**syntax_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**source_code_info_or_builder** | [**SourceCodeInfoOrBuilder**](SourceCodeInfoOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**options** | [**FileOptions**](FileOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**FileDescriptorProto**](FileDescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.file_descriptor_proto import FileDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of FileDescriptorProto from a JSON string
file_descriptor_proto_instance = FileDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(FileDescriptorProto.to_json())

# convert the object into a dict
file_descriptor_proto_dict = file_descriptor_proto_instance.to_dict()
# create an instance of FileDescriptorProto from a dict
file_descriptor_proto_from_dict = FileDescriptorProto.from_dict(file_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


