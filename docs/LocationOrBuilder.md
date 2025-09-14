# LocationOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_list** | **List[int]** |  | [optional] 
**path_count** | **int** |  | [optional] 
**span_list** | **List[int]** |  | [optional] 
**span_count** | **int** |  | [optional] 
**leading_comments** | **str** |  | [optional] 
**leading_comments_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**trailing_comments** | **str** |  | [optional] 
**trailing_comments_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**leading_detached_comments_list** | **List[str]** |  | [optional] 
**leading_detached_comments_count** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.location_or_builder import LocationOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of LocationOrBuilder from a JSON string
location_or_builder_instance = LocationOrBuilder.from_json(json)
# print the JSON string representation of the object
print(LocationOrBuilder.to_json())

# convert the object into a dict
location_or_builder_dict = location_or_builder_instance.to_dict()
# create an instance of LocationOrBuilder from a dict
location_or_builder_from_dict = LocationOrBuilder.from_dict(location_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


