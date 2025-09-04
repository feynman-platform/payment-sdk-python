# AccountId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**name** | [**ByteString**](ByteString.md) |  | [optional] 
**address** | [**ByteString**](ByteString.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**AccountId**](AccountId.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.account_id import AccountId

# TODO update the JSON string below
json = "{}"
# create an instance of AccountId from a JSON string
account_id_instance = AccountId.from_json(json)
# print the JSON string representation of the object
print(AccountId.to_json())

# convert the object into a dict
account_id_dict = account_id_instance.to_dict()
# create an instance of AccountId from a dict
account_id_from_dict = AccountId.from_dict(account_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


