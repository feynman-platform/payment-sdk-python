# EnumOptionsOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated_legacy_json_field_conflicts** | **bool** |  | [optional] 
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**allow_alias** | **bool** |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_options_or_builder import EnumOptionsOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of EnumOptionsOrBuilder from a JSON string
enum_options_or_builder_instance = EnumOptionsOrBuilder.from_json(json)
# print the JSON string representation of the object
print(EnumOptionsOrBuilder.to_json())

# convert the object into a dict
enum_options_or_builder_dict = enum_options_or_builder_instance.to_dict()
# create an instance of EnumOptionsOrBuilder from a dict
enum_options_or_builder_from_dict = EnumOptionsOrBuilder.from_dict(enum_options_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


