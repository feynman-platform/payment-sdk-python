# ExtensionRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**options_or_builder** | [**ExtensionRangeOptionsOrBuilder**](ExtensionRangeOptionsOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**options** | [**ExtensionRangeOptions**](ExtensionRangeOptions.md) |  | [optional] 
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**ExtensionRange**](ExtensionRange.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.extension_range import ExtensionRange

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionRange from a JSON string
extension_range_instance = ExtensionRange.from_json(json)
# print the JSON string representation of the object
print(ExtensionRange.to_json())

# convert the object into a dict
extension_range_dict = extension_range_instance.to_dict()
# create an instance of ExtensionRange from a dict
extension_range_from_dict = ExtensionRange.from_dict(extension_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


