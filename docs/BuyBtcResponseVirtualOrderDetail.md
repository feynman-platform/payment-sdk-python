# BuyBtcResponseVirtualOrderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**VirtualOrderDetail**](VirtualOrderDetail.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_virtual_order_detail import BuyBtcResponseVirtualOrderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseVirtualOrderDetail from a JSON string
buy_btc_response_virtual_order_detail_instance = BuyBtcResponseVirtualOrderDetail.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseVirtualOrderDetail.to_json())

# convert the object into a dict
buy_btc_response_virtual_order_detail_dict = buy_btc_response_virtual_order_detail_instance.to_dict()
# create an instance of BuyBtcResponseVirtualOrderDetail from a dict
buy_btc_response_virtual_order_detail_from_dict = BuyBtcResponseVirtualOrderDetail.from_dict(buy_btc_response_virtual_order_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


