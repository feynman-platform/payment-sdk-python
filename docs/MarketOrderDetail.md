# MarketOrderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**maker_order_id** | [**ByteString**](ByteString.md) |  | [optional] 
**taker_order_id** | [**ByteString**](ByteString.md) |  | [optional] 
**fill_sell_quantity** | **int** |  | [optional] 
**fill_buy_quantity** | **int** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**MarketOrderDetail**](MarketOrderDetail.md) |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.market_order_detail import MarketOrderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MarketOrderDetail from a JSON string
market_order_detail_instance = MarketOrderDetail.from_json(json)
# print the JSON string representation of the object
print(MarketOrderDetail.to_json())

# convert the object into a dict
market_order_detail_dict = market_order_detail_instance.to_dict()
# create an instance of MarketOrderDetail from a dict
market_order_detail_from_dict = MarketOrderDetail.from_dict(market_order_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


