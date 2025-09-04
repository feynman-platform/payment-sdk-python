# EnumReservedRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**EnumReservedRange**](EnumReservedRange.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_reserved_range import EnumReservedRange

# TODO update the JSON string below
json = "{}"
# create an instance of EnumReservedRange from a JSON string
enum_reserved_range_instance = EnumReservedRange.from_json(json)
# print the JSON string representation of the object
print(EnumReservedRange.to_json())

# convert the object into a dict
enum_reserved_range_dict = enum_reserved_range_instance.to_dict()
# create an instance of EnumReservedRange from a dict
enum_reserved_range_from_dict = EnumReservedRange.from_dict(enum_reserved_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


