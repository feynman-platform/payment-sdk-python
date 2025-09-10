# Raw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**ref_block_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**ref_block_num** | **int** |  | [optional] 
**ref_block_hash** | [**ByteString**](ByteString.md) |  | [optional] 
**auths_list** | [**List[Authority]**](Authority.md) |  | [optional] 
**auths_count** | **int** |  | [optional] 
**auths_or_builder_list** | [**List[AuthorityOrBuilder]**](AuthorityOrBuilder.md) |  | [optional] 
**contract_count** | **int** |  | [optional] 
**contract_or_builder_list** | [**List[ContractOrBuilder]**](ContractOrBuilder.md) |  | [optional] 
**fee_limit** | **int** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**timestamp** | **int** |  | [optional] 
**data** | [**ByteString**](ByteString.md) |  | [optional] 
**contract_list** | [**List[Contract]**](Contract.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**scripts** | [**ByteString**](ByteString.md) |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**Raw**](Raw.md) |  | [optional] 
**expiration** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.raw import Raw

# TODO update the JSON string below
json = "{}"
# create an instance of Raw from a JSON string
raw_instance = Raw.from_json(json)
# print the JSON string representation of the object
print(Raw.to_json())

# convert the object into a dict
raw_dict = raw_instance.to_dict()
# create an instance of Raw from a dict
raw_from_dict = Raw.from_dict(raw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


