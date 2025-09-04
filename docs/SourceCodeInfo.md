# SourceCodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**location_list** | [**List[Location]**](Location.md) |  | [optional] 
**location_count** | **int** |  | [optional] 
**location_or_builder_list** | [**List[LocationOrBuilder]**](LocationOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**SourceCodeInfo**](SourceCodeInfo.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.source_code_info import SourceCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCodeInfo from a JSON string
source_code_info_instance = SourceCodeInfo.from_json(json)
# print the JSON string representation of the object
print(SourceCodeInfo.to_json())

# convert the object into a dict
source_code_info_dict = source_code_info_instance.to_dict()
# create an instance of SourceCodeInfo from a dict
source_code_info_from_dict = SourceCodeInfo.from_dict(source_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


