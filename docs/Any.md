# Any


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**type_url** | **str** |  | [optional] 
**type_url_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**value** | [**ByteString**](ByteString.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**Any**](Any.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.any import Any

# TODO update the JSON string below
json = "{}"
# create an instance of Any from a JSON string
any_instance = Any.from_json(json)
# print the JSON string representation of the object
print(Any.to_json())

# convert the object into a dict
any_dict = any_instance.to_dict()
# create an instance of Any from a dict
any_from_dict = Any.from_dict(any_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


