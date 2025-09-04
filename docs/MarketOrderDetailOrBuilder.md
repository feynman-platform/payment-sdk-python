# MarketOrderDetailOrBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_order_id** | [**ByteString**](ByteString.md) |  | [optional] 
**taker_order_id** | [**ByteString**](ByteString.md) |  | [optional] 
**fill_sell_quantity** | **int** |  | [optional] 
**fill_buy_quantity** | **int** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**default_instance_for_type** | [**Message**](Message.md) |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**initialized** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.market_order_detail_or_builder import MarketOrderDetailOrBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of MarketOrderDetailOrBuilder from a JSON string
market_order_detail_or_builder_instance = MarketOrderDetailOrBuilder.from_json(json)
# print the JSON string representation of the object
print(MarketOrderDetailOrBuilder.to_json())

# convert the object into a dict
market_order_detail_or_builder_dict = market_order_detail_or_builder_instance.to_dict()
# create an instance of MarketOrderDetailOrBuilder from a dict
market_order_detail_or_builder_from_dict = MarketOrderDetailOrBuilder.from_dict(market_order_detail_or_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


