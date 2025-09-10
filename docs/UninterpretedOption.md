# UninterpretedOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**aggregate_value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**name_list** | [**List[NamePart]**](NamePart.md) |  | [optional] 
**name_or_builder_list** | [**List[NamePartOrBuilder]**](NamePartOrBuilder.md) |  | [optional] 
**identifier_value_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**positive_int_value** | **int** |  | [optional] 
**negative_int_value** | **int** |  | [optional] 
**aggregate_value** | **str** |  | [optional] 
**double_value** | **float** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name_count** | **int** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**string_value** | [**ByteString**](ByteString.md) |  | [optional] 
**identifier_value** | **str** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**UninterpretedOption**](UninterpretedOption.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.uninterpreted_option import UninterpretedOption

# TODO update the JSON string below
json = "{}"
# create an instance of UninterpretedOption from a JSON string
uninterpreted_option_instance = UninterpretedOption.from_json(json)
# print the JSON string representation of the object
print(UninterpretedOption.to_json())

# convert the object into a dict
uninterpreted_option_dict = uninterpreted_option_instance.to_dict()
# create an instance of UninterpretedOption from a dict
uninterpreted_option_from_dict = UninterpretedOption.from_dict(uninterpreted_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


