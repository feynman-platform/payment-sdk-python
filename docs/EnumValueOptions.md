# EnumValueOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**debug_redact** | **bool** |  | [optional] 
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**EnumValueOptions**](EnumValueOptions.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**all_fields_raw** | **Dict[str, object]** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_value_options import EnumValueOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EnumValueOptions from a JSON string
enum_value_options_instance = EnumValueOptions.from_json(json)
# print the JSON string representation of the object
print(EnumValueOptions.to_json())

# convert the object into a dict
enum_value_options_dict = enum_value_options_instance.to_dict()
# create an instance of EnumValueOptions from a dict
enum_value_options_from_dict = EnumValueOptions.from_dict(enum_value_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


