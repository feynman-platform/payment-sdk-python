# FieldDescriptorProtoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_name** | **str** |  | [optional] 
**proto3_optional** | **bool** |  | [optional] 
**oneof_index** | **int** |  | [optional] 
**extendee** | **str** |  | [optional] 
**options_or_builder** | [**FieldOptionsOrBuilder**](FieldOptionsOrBuilder.md) |  | [optional] 
**extendee_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**default_value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**json_name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**type_name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**name** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**options** | [**FieldOptions**](FieldOptions.md) |  | [optional] 
**label** | **str** |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDescriptorProtoOrBuilder from a JSON string
field_descriptor_proto_or_builder_instance = FieldDescriptorProtoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(FieldDescriptorProtoOrBuilder.to_json())

# convert the object into a dict
field_descriptor_proto_or_builder_dict = field_descriptor_proto_or_builder_instance.to_dict()
# create an instance of FieldDescriptorProtoOrBuilder from a dict
field_descriptor_proto_or_builder_from_dict = FieldDescriptorProtoOrBuilder.from_dict(field_descriptor_proto_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


