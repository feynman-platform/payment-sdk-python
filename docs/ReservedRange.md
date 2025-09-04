# ReservedRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**ReservedRange**](ReservedRange.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.reserved_range import ReservedRange

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedRange from a JSON string
reserved_range_instance = ReservedRange.from_json(json)
# print the JSON string representation of the object
print(ReservedRange.to_json())

# convert the object into a dict
reserved_range_dict = reserved_range_instance.to_dict()
# create an instance of ReservedRange from a dict
reserved_range_from_dict = ReservedRange.from_dict(reserved_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


