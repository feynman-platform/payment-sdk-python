# SourceCodeInfoOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_count** | **int** |  | [optional] 
**location_or_builder_list** | [**List[LocationOrBuilder]**](LocationOrBuilder.md) |  | [optional] 
**location_list** | [**List[Location]**](Location.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.source_code_info_or_builder import SourceCodeInfoOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCodeInfoOrBuilder from a JSON string
source_code_info_or_builder_instance = SourceCodeInfoOrBuilder.from_json(json)
# print the JSON string representation of the object
print(SourceCodeInfoOrBuilder.to_json())

# convert the object into a dict
source_code_info_or_builder_dict = source_code_info_or_builder_instance.to_dict()
# create an instance of SourceCodeInfoOrBuilder from a dict
source_code_info_or_builder_from_dict = SourceCodeInfoOrBuilder.from_dict(source_code_info_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


