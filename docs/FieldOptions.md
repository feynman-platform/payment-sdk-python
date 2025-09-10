# FieldOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**packed** | **bool** |  | [optional] 
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**ctype** | **str** |  | [optional] 
**jstype** | **str** |  | [optional] 
**lazy** | **bool** |  | [optional] 
**unverified_lazy** | **bool** |  | [optional] 
**weak** | **bool** |  | [optional] 
**debug_redact** | **bool** |  | [optional] 
**targets_list** | **List[str]** |  | [optional] 
**targets_count** | **int** |  | [optional] 
**edition_defaults_list** | [**List[EditionDefault]**](EditionDefault.md) |  | [optional] 
**edition_defaults_count** | **int** |  | [optional] 
**edition_defaults_or_builder_list** | [**List[EditionDefaultOrBuilder]**](EditionDefaultOrBuilder.md) |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**retention** | **str** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**FieldOptions**](FieldOptions.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**all_fields_raw** | **Dict[str, object]** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.field_options import FieldOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FieldOptions from a JSON string
field_options_instance = FieldOptions.from_json(json)
# print the JSON string representation of the object
print(FieldOptions.to_json())

# convert the object into a dict
field_options_dict = field_options_instance.to_dict()
# create an instance of FieldOptions from a dict
field_options_from_dict = FieldOptions.from_dict(field_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


