# ReservedRangeOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.reserved_range_or_builder import ReservedRangeOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedRangeOrBuilder from a JSON string
reserved_range_or_builder_instance = ReservedRangeOrBuilder.from_json(json)
# print the JSON string representation of the object
print(ReservedRangeOrBuilder.to_json())

# convert the object into a dict
reserved_range_or_builder_dict = reserved_range_or_builder_instance.to_dict()
# create an instance of ReservedRangeOrBuilder from a dict
reserved_range_or_builder_from_dict = ReservedRangeOrBuilder.from_dict(reserved_range_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


