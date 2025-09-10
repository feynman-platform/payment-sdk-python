# MethodDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**options_or_builder** | [**MethodOptionsOrBuilder**](MethodOptionsOrBuilder.md) |  | [optional] 
**input_type_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**output_type_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**client_streaming** | **bool** |  | [optional] 
**server_streaming** | **bool** |  | [optional] 
**output_type** | **str** |  | [optional] 
**input_type** | **str** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**MethodOptions**](MethodOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**MethodDescriptorProto**](MethodDescriptorProto.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.method_descriptor_proto import MethodDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of MethodDescriptorProto from a JSON string
method_descriptor_proto_instance = MethodDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(MethodDescriptorProto.to_json())

# convert the object into a dict
method_descriptor_proto_dict = method_descriptor_proto_instance.to_dict()
# create an instance of MethodDescriptorProto from a dict
method_descriptor_proto_from_dict = MethodDescriptorProto.from_dict(method_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


