# Declaration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**full_name_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**type_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**reserved** | **bool** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**full_name** | **str** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**Declaration**](Declaration.md) |  | [optional] 
**repeated** | **bool** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.declaration import Declaration

# TODO update the JSON string below
json = "{}"
# create an instance of Declaration from a JSON string
declaration_instance = Declaration.from_json(json)
# print the JSON string representation of the object
print(Declaration.to_json())

# convert the object into a dict
declaration_dict = declaration_instance.to_dict()
# create an instance of Declaration from a dict
declaration_from_dict = Declaration.from_dict(declaration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


