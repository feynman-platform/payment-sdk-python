# UninterpretedOptionOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**name_list** | [**List[NamePart]**](NamePart.md) |  | [optional] 
**name_or_builder_list** | [**List[NamePartOrBuilder]**](NamePartOrBuilder.md) |  | [optional] 
**identifier_value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**positive_int_value** | **int** |  | [optional] 
**negative_int_value** | **int** |  | [optional] 
**aggregate_value** | **str** |  | [optional] 
**double_value** | **float** |  | [optional] 
**name_count** | **int** |  | [optional] 
**string_value** | [**ByteString**](ByteString.md) |  | [optional] 
**identifier_value** | **str** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.uninterpreted_option_or_builder import UninterpretedOptionOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of UninterpretedOptionOrBuilder from a JSON string
uninterpreted_option_or_builder_instance = UninterpretedOptionOrBuilder.from_json(json)
# print the JSON string representation of the object
print(UninterpretedOptionOrBuilder.to_json())

# convert the object into a dict
uninterpreted_option_or_builder_dict = uninterpreted_option_or_builder_instance.to_dict()
# create an instance of UninterpretedOptionOrBuilder from a dict
uninterpreted_option_or_builder_from_dict = UninterpretedOptionOrBuilder.from_dict(uninterpreted_option_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


