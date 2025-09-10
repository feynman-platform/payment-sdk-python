# FeatureSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**json_format** | **str** |  | [optional] 
**repeated_field_encoding** | **str** |  | [optional] 
**utf8_validation** | **str** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**enum_type** | **str** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**message_encoding** | **str** |  | [optional] 
**field_presence** | **str** |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**all_fields_raw** | **Dict[str, object]** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.feature_set import FeatureSet

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureSet from a JSON string
feature_set_instance = FeatureSet.from_json(json)
# print the JSON string representation of the object
print(FeatureSet.to_json())

# convert the object into a dict
feature_set_dict = feature_set_instance.to_dict()
# create an instance of FeatureSet from a dict
feature_set_from_dict = FeatureSet.from_dict(feature_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


