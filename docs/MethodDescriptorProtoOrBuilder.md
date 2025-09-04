# MethodDescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**options_or_builder** | [**MethodOptionsOrBuilder**](MethodOptionsOrBuilder.md) |  | [optional] 
**input_type_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**output_type_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**client_streaming** | **bool** |  | [optional] 
**server_streaming** | **bool** |  | [optional] 
**output_type** | **str** |  | [optional] 
**input_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**MethodOptions**](MethodOptions.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.method_descriptor_proto_or_builder import MethodDescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of MethodDescriptorProtoOrBuilder from a JSON string
method_descriptor_proto_or_builder_instance = MethodDescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(MethodDescriptorProtoOrBuilder.to_json())

# convert the object into a dict
method_descriptor_proto_or_builder_dict = method_descriptor_proto_or_builder_instance.to_dict()
# create an instance of MethodDescriptorProtoOrBuilder from a dict
method_descriptor_proto_or_builder_from_dict = MethodDescriptorProtoOrBuilder.from_dict(method_descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


