# Authority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**account_or_builder** | [**AccountIdOrBuilder**](AccountIdOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**permission_name** | [**ByteString**](ByteString.md) |  | [optional] 
**account** | [**AccountId**](AccountId.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**Authority**](Authority.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.authority import Authority

# TODO update the JSON string below
json = "{}"
# create an instance of Authority from a JSON string
authority_instance = Authority.from_json(json)
# print the JSON string representation of the object
print(Authority.to_json())

# convert the object into a dict
authority_dict = authority_instance.to_dict()
# create an instance of Authority from a dict
authority_from_dict = Authority.from_dict(authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


