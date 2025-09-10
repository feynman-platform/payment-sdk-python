# FieldOptionsOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**deprecated** | **bool** |  | [optional] 
**retention** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.field_options_or_builder import FieldOptionsOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of FieldOptionsOrBuilder from a JSON string
field_options_or_builder_instance = FieldOptionsOrBuilder.from_json(json)
# print the JSON string representation of the object
print(FieldOptionsOrBuilder.to_json())

# convert the object into a dict
field_options_or_builder_dict = field_options_or_builder_instance.to_dict()
# create an instance of FieldOptionsOrBuilder from a dict
field_options_or_builder_from_dict = FieldOptionsOrBuilder.from_dict(field_options_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


