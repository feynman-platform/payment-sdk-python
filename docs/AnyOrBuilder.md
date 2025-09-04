# AnyOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_url** | **str** |  | [optional] 
**type_url_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**value** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.any_or_builder import AnyOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of AnyOrBuilder from a JSON string
any_or_builder_instance = AnyOrBuilder.from_json(json)
# print the JSON string representation of the object
print(AnyOrBuilder.to_json())

# convert the object into a dict
any_or_builder_dict = any_or_builder_instance.to_dict()
# create an instance of AnyOrBuilder from a dict
any_or_builder_from_dict = AnyOrBuilder.from_dict(any_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


