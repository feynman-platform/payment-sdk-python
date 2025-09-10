# FeatureSetOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_format** | **str** |  | [optional] 
**repeated_field_encoding** | **str** |  | [optional] 
**utf8_validation** | **str** |  | [optional] 
**enum_type** | **str** |  | [optional] 
**message_encoding** | **str** |  | [optional] 
**field_presence** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.feature_set_or_builder import FeatureSetOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureSetOrBuilder from a JSON string
feature_set_or_builder_instance = FeatureSetOrBuilder.from_json(json)
# print the JSON string representation of the object
print(FeatureSetOrBuilder.to_json())

# convert the object into a dict
feature_set_or_builder_dict = feature_set_or_builder_instance.to_dict()
# create an instance of FeatureSetOrBuilder from a dict
feature_set_or_builder_from_dict = FeatureSetOrBuilder.from_dict(feature_set_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


