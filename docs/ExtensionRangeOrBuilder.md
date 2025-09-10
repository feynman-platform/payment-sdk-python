# ExtensionRangeOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options_or_builder** | [**ExtensionRangeOptionsOrBuilder**](ExtensionRangeOptionsOrBuilder.md) |  | [optional] 
**options** | [**ExtensionRangeOptions**](ExtensionRangeOptions.md) |  | [optional] 
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.extension_range_or_builder import ExtensionRangeOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionRangeOrBuilder from a JSON string
extension_range_or_builder_instance = ExtensionRangeOrBuilder.from_json(json)
# print the JSON string representation of the object
print(ExtensionRangeOrBuilder.to_json())

# convert the object into a dict
extension_range_or_builder_dict = extension_range_or_builder_instance.to_dict()
# create an instance of ExtensionRangeOrBuilder from a dict
extension_range_or_builder_from_dict = ExtensionRangeOrBuilder.from_dict(extension_range_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


