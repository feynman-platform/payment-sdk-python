# MessageOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**map_entry** | **bool** |  | [optional] 
**no_standard_descriptor_accessor** | **bool** |  | [optional] 
**deprecated_legacy_json_field_conflicts** | **bool** |  | [optional] 
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**MessageOptions**](MessageOptions.md) |  | [optional] 
**message_set_wire_format** | **bool** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**all_fields_raw** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.message_options import MessageOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOptions from a JSON string
message_options_instance = MessageOptions.from_json(json)
# print the JSON string representation of the object
print(MessageOptions.to_json())

# convert the object into a dict
message_options_dict = message_options_instance.to_dict()
# create an instance of MessageOptions from a dict
message_options_from_dict = MessageOptions.from_dict(message_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


