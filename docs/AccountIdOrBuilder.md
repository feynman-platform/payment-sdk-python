# AccountIdOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ByteString**](ByteString.md) |  | [optional] 
**address** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.account_id_or_builder import AccountIdOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of AccountIdOrBuilder from a JSON string
account_id_or_builder_instance = AccountIdOrBuilder.from_json(json)
# print the JSON string representation of the object
print(AccountIdOrBuilder.to_json())

# convert the object into a dict
account_id_or_builder_dict = account_id_or_builder_instance.to_dict()
# create an instance of AccountIdOrBuilder from a dict
account_id_or_builder_from_dict = AccountIdOrBuilder.from_dict(account_id_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


