# MessageOptionsOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_entry** | **bool** |  | [optional] 
**no_standard_descriptor_accessor** | **bool** |  | [optional] 
**deprecated_legacy_json_field_conflicts** | **bool** |  | [optional] 
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**message_set_wire_format** | **bool** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.message_options_or_builder import MessageOptionsOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOptionsOrBuilder from a JSON string
message_options_or_builder_instance = MessageOptionsOrBuilder.from_json(json)
# print the JSON string representation of the object
print(MessageOptionsOrBuilder.to_json())

# convert the object into a dict
message_options_or_builder_dict = message_options_or_builder_instance.to_dict()
# create an instance of MessageOptionsOrBuilder from a dict
message_options_or_builder_from_dict = MessageOptionsOrBuilder.from_dict(message_options_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


