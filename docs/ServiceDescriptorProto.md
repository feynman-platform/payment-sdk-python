# ServiceDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**method_list** | [**List[MethodDescriptorProto]**](MethodDescriptorProto.md) |  | [optional] 
**options_or_builder** | [**ServiceOptionsOrBuilder**](ServiceOptionsOrBuilder.md) |  | [optional] 
**method_count** | **int** |  | [optional] 
**method_or_builder_list** | [**List[MethodDescriptorProtoOrBuilder]**](MethodDescriptorProtoOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**ServiceOptions**](ServiceOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**ServiceDescriptorProto**](ServiceDescriptorProto.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.service_descriptor_proto import ServiceDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDescriptorProto from a JSON string
service_descriptor_proto_instance = ServiceDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(ServiceDescriptorProto.to_json())

# convert the object into a dict
service_descriptor_proto_dict = service_descriptor_proto_instance.to_dict()
# create an instance of ServiceDescriptorProto from a dict
service_descriptor_proto_from_dict = ServiceDescriptorProto.from_dict(service_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


