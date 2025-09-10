# OneofDescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options_or_builder** | [**OneofOptionsOrBuilder**](OneofOptionsOrBuilder.md) |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**OneofOptions**](OneofOptions.md) |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.oneof_descriptor_proto_or_builder import OneofDescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of OneofDescriptorProtoOrBuilder from a JSON string
oneof_descriptor_proto_or_builder_instance = OneofDescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(OneofDescriptorProtoOrBuilder.to_json())

# convert the object into a dict
oneof_descriptor_proto_or_builder_dict = oneof_descriptor_proto_or_builder_instance.to_dict()
# create an instance of OneofDescriptorProtoOrBuilder from a dict
oneof_descriptor_proto_or_builder_from_dict = OneofDescriptorProtoOrBuilder.from_dict(oneof_descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


