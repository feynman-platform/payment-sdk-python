# EnumReservedRangeOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.enum_reserved_range_or_builder import EnumReservedRangeOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of EnumReservedRangeOrBuilder from a JSON string
enum_reserved_range_or_builder_instance = EnumReservedRangeOrBuilder.from_json(json)
# print the JSON string representation of the object
print(EnumReservedRangeOrBuilder.to_json())

# convert the object into a dict
enum_reserved_range_or_builder_dict = enum_reserved_range_or_builder_instance.to_dict()
# create an instance of EnumReservedRangeOrBuilder from a dict
enum_reserved_range_or_builder_from_dict = EnumReservedRangeOrBuilder.from_dict(enum_reserved_range_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


