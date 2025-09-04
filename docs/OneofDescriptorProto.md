# OneofDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**options_or_builder** | [**OneofOptionsOrBuilder**](OneofOptionsOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**OneofOptions**](OneofOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**OneofDescriptorProto**](OneofDescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.oneof_descriptor_proto import OneofDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of OneofDescriptorProto from a JSON string
oneof_descriptor_proto_instance = OneofDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(OneofDescriptorProto.to_json())

# convert the object into a dict
oneof_descriptor_proto_dict = oneof_descriptor_proto_instance.to_dict()
# create an instance of OneofDescriptorProto from a dict
oneof_descriptor_proto_from_dict = OneofDescriptorProto.from_dict(oneof_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


