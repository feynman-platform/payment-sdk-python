# NamePart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**name_part_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**is_extension** | **bool** |  | [optional] 
**name_part** | **str** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**NamePart**](NamePart.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.name_part import NamePart

# TODO update the JSON string below
json = "{}"
# create an instance of NamePart from a JSON string
name_part_instance = NamePart.from_json(json)
# print the JSON string representation of the object
print(NamePart.to_json())

# convert the object into a dict
name_part_dict = name_part_instance.to_dict()
# create an instance of NamePart from a dict
name_part_from_dict = NamePart.from_dict(name_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


