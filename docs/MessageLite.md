# MessageLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**default_instance_for_type** | [**MessageLite**](MessageLite.md) |  | [optional] 

## Example

```python
from buybtcpay.models.message_lite import MessageLite

# TODO update the JSON string below
json = "{}"
# create an instance of MessageLite from a JSON string
message_lite_instance = MessageLite.from_json(json)
# print the JSON string representation of the object
print(MessageLite.to_json())

# convert the object into a dict
message_lite_dict = message_lite_instance.to_dict()
# create an instance of MessageLite from a dict
message_lite_from_dict = MessageLite.from_dict(message_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


