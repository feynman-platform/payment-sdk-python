# ServiceDescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**method_list** | [**List[MethodDescriptorProto]**](MethodDescriptorProto.md) |  | [optional] 
**options_or_builder** | [**ServiceOptionsOrBuilder**](ServiceOptionsOrBuilder.md) |  | [optional] 
**method_count** | **int** |  | [optional] 
**method_or_builder_list** | [**List[MethodDescriptorProtoOrBuilder]**](MethodDescriptorProtoOrBuilder.md) |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**ServiceOptions**](ServiceOptions.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.service_descriptor_proto_or_builder import ServiceDescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDescriptorProtoOrBuilder from a JSON string
service_descriptor_proto_or_builder_instance = ServiceDescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(ServiceDescriptorProtoOrBuilder.to_json())

# convert the object into a dict
service_descriptor_proto_or_builder_dict = service_descriptor_proto_or_builder_instance.to_dict()
# create an instance of ServiceDescriptorProtoOrBuilder from a dict
service_descriptor_proto_or_builder_from_dict = ServiceDescriptorProtoOrBuilder.from_dict(service_descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


