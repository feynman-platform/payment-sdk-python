# FieldDescriptorProto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**label** | **str** |  | [optional] 
**name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**json_name** | **str** |  | [optional] 
**proto3_optional** | **bool** |  | [optional] 
**oneof_index** | **int** |  | [optional] 
**extendee** | **str** |  | [optional] 
**options_or_builder** | [**FieldOptionsOrBuilder**](FieldOptionsOrBuilder.md) |  | [optional] 
**type_name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**extendee_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**default_value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**json_name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**options** | [**FieldOptions**](FieldOptions.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**FieldDescriptorProto**](FieldDescriptorProto.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.field_descriptor_proto import FieldDescriptorProto

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDescriptorProto from a JSON string
field_descriptor_proto_instance = FieldDescriptorProto.from_json(json)
# print the JSON string representation of the object
print(FieldDescriptorProto.to_json())

# convert the object into a dict
field_descriptor_proto_dict = field_descriptor_proto_instance.to_dict()
# create an instance of FieldDescriptorProto from a dict
field_descriptor_proto_from_dict = FieldDescriptorProto.from_dict(field_descriptor_proto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


