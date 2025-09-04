# RawOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_block_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**ref_block_num** | **int** |  | [optional] 
**ref_block_hash** | [**ByteString**](ByteString.md) |  | [optional] 
**auths_list** | [**List[Authority]**](Authority.md) |  | [optional] 
**auths_count** | **int** |  | [optional] 
**auths_or_builder_list** | [**List[AuthorityOrBuilder]**](AuthorityOrBuilder.md) |  | [optional] 
**contract_count** | **int** |  | [optional] 
**contract_or_builder_list** | [**List[ContractOrBuilder]**](ContractOrBuilder.md) |  | [optional] 
**fee_limit** | **int** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**data** | [**ByteString**](ByteString.md) |  | [optional] 
**expiration** | **int** |  | [optional] 
**contract_list** | [**List[Contract]**](Contract.md) |  | [optional] 
**scripts** | [**ByteString**](ByteString.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.raw_or_builder import RawOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of RawOrBuilder from a JSON string
raw_or_builder_instance = RawOrBuilder.from_json(json)
# print the JSON string representation of the object
print(RawOrBuilder.to_json())

# convert the object into a dict
raw_or_builder_dict = raw_or_builder_instance.to_dict()
# create an instance of RawOrBuilder from a dict
raw_or_builder_from_dict = RawOrBuilder.from_dict(raw_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


