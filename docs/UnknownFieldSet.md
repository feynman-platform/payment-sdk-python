# UnknownFieldSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serialized_size_as_message_set** | **int** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 

## Example

```python
from buybtcpay.models.unknown_field_set import UnknownFieldSet

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownFieldSet from a JSON string
unknown_field_set_instance = UnknownFieldSet.from_json(json)
# print the JSON string representation of the object
print(UnknownFieldSet.to_json())

# convert the object into a dict
unknown_field_set_dict = unknown_field_set_instance.to_dict()
# create an instance of UnknownFieldSet from a dict
unknown_field_set_from_dict = UnknownFieldSet.from_dict(unknown_field_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


