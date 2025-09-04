# EditionDefault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**edition** | **str** |  | [optional] 
**value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**EditionDefault**](EditionDefault.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.edition_default import EditionDefault

# TODO update the JSON string below
json = "{}"
# create an instance of EditionDefault from a JSON string
edition_default_instance = EditionDefault.from_json(json)
# print the JSON string representation of the object
print(EditionDefault.to_json())

# convert the object into a dict
edition_default_dict = edition_default_instance.to_dict()
# create an instance of EditionDefault from a dict
edition_default_from_dict = EditionDefault.from_dict(edition_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


