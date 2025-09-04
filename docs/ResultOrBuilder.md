# ResultOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ret** | **str** |  | [optional] 
**asset_issue_id** | **str** |  | [optional] 
**asset_issue_id_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**withdraw_amount** | **int** |  | [optional] 
**unfreeze_amount** | **int** |  | [optional] 
**exchange_received_amount** | **int** |  | [optional] 
**exchange_inject_another_amount** | **int** |  | [optional] 
**exchange_withdraw_another_amount** | **int** |  | [optional] 
**shielded_transaction_fee** | **int** |  | [optional] 
**order_details_list** | [**List[MarketOrderDetail]**](MarketOrderDetail.md) |  | [optional] 
**order_details_or_builder_list** | [**List[MarketOrderDetailOrBuilder]**](MarketOrderDetailOrBuilder.md) |  | [optional] 
**order_details_count** | **int** |  | [optional] 
**withdraw_expire_amount** | **int** |  | [optional] 
**cancel_unfreeze_v2_amount_count** | **int** |  | [optional] 
**cancel_unfreeze_v2_amount** | **Dict[str, int]** |  | [optional] 
**cancel_unfreeze_v2_amount_map** | **Dict[str, int]** |  | [optional] 
**ret_value** | **int** |  | [optional] 
**contract_ret_value** | **int** |  | [optional] 
**contract_ret** | **str** |  | [optional] 
**order_id** | [**ByteString**](ByteString.md) |  | [optional] 
**fee** | **int** |  | [optional] 
**exchange_id** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.result_or_builder import ResultOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of ResultOrBuilder from a JSON string
result_or_builder_instance = ResultOrBuilder.from_json(json)
# print the JSON string representation of the object
print(ResultOrBuilder.to_json())

# convert the object into a dict
result_or_builder_dict = result_or_builder_instance.to_dict()
# create an instance of ResultOrBuilder from a dict
result_or_builder_from_dict = ResultOrBuilder.from_dict(result_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


