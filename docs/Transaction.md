# Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**raw_data_or_builder** | [**RawOrBuilder**](RawOrBuilder.md) |  | [optional] 
**signature_list** | [**List[ByteString]**](ByteString.md) |  | [optional] 
**signature_count** | **int** |  | [optional] 
**ret_list** | [**List[Result]**](Result.md) |  | [optional] 
**ret_or_builder_list** | [**List[ResultOrBuilder]**](ResultOrBuilder.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**raw_data** | [**Raw**](Raw.md) |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**ret_count** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**Transaction**](Transaction.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


