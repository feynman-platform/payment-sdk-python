# ServiceOptionsOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.service_options_or_builder import ServiceOptionsOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceOptionsOrBuilder from a JSON string
service_options_or_builder_instance = ServiceOptionsOrBuilder.from_json(json)
# print the JSON string representation of the object
print(ServiceOptionsOrBuilder.to_json())

# convert the object into a dict
service_options_or_builder_dict = service_options_or_builder_instance.to_dict()
# create an instance of ServiceOptionsOrBuilder from a dict
service_options_or_builder_from_dict = ServiceOptionsOrBuilder.from_dict(service_options_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


