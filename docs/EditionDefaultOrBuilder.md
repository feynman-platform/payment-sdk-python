# EditionDefaultOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | **str** |  | [optional] 
**value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**value** | **str** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.edition_default_or_builder import EditionDefaultOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of EditionDefaultOrBuilder from a JSON string
edition_default_or_builder_instance = EditionDefaultOrBuilder.from_json(json)
# print the JSON string representation of the object
print(EditionDefaultOrBuilder.to_json())

# convert the object into a dict
edition_default_or_builder_dict = edition_default_or_builder_instance.to_dict()
# create an instance of EditionDefaultOrBuilder from a dict
edition_default_or_builder_from_dict = EditionDefaultOrBuilder.from_dict(edition_default_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


