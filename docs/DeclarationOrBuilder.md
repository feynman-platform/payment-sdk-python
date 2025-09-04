# DeclarationOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**type_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**reserved** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**full_name** | **str** |  | [optional] 
**repeated** | **bool** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.declaration_or_builder import DeclarationOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarationOrBuilder from a JSON string
declaration_or_builder_instance = DeclarationOrBuilder.from_json(json)
# print the JSON string representation of the object
print(DeclarationOrBuilder.to_json())

# convert the object into a dict
declaration_or_builder_dict = declaration_or_builder_instance.to_dict()
# create an instance of DeclarationOrBuilder from a dict
declaration_or_builder_from_dict = DeclarationOrBuilder.from_dict(declaration_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


