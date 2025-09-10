# AuthorityOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_or_builder** | [**AccountIdOrBuilder**](AccountIdOrBuilder.md) |  | [optional] 
**permission_name** | [**ByteString**](ByteString.md) |  | [optional] 
**account** | [**AccountId**](AccountId.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.authority_or_builder import AuthorityOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorityOrBuilder from a JSON string
authority_or_builder_instance = AuthorityOrBuilder.from_json(json)
# print the JSON string representation of the object
print(AuthorityOrBuilder.to_json())

# convert the object into a dict
authority_or_builder_dict = authority_or_builder_instance.to_dict()
# create an instance of AuthorityOrBuilder from a dict
authority_or_builder_from_dict = AuthorityOrBuilder.from_dict(authority_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


