# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
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
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**Location**](Location.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


