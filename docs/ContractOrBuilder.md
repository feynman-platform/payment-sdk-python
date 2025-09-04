# ContractOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_or_builder** | [**AnyOrBuilder**](AnyOrBuilder.md) |  | [optional] 
**contract_name** | [**ByteString**](ByteString.md) |  | [optional] 
**permission_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**provider** | [**ByteString**](ByteString.md) |  | [optional] 
**parameter** | [**Any**](Any.md) |  | [optional] 
**type_value** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.contract_or_builder import ContractOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of ContractOrBuilder from a JSON string
contract_or_builder_instance = ContractOrBuilder.from_json(json)
# print the JSON string representation of the object
print(ContractOrBuilder.to_json())

# convert the object into a dict
contract_or_builder_dict = contract_or_builder_instance.to_dict()
# create an instance of ContractOrBuilder from a dict
contract_or_builder_from_dict = ContractOrBuilder.from_dict(contract_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


