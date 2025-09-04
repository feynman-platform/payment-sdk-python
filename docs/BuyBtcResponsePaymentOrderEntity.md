# BuyBtcResponsePaymentOrderEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PaymentOrderEntity**](PaymentOrderEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePaymentOrderEntity from a JSON string
buy_btc_response_payment_order_entity_instance = BuyBtcResponsePaymentOrderEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePaymentOrderEntity.to_json())

# convert the object into a dict
buy_btc_response_payment_order_entity_dict = buy_btc_response_payment_order_entity_instance.to_dict()
# create an instance of BuyBtcResponsePaymentOrderEntity from a dict
buy_btc_response_payment_order_entity_from_dict = BuyBtcResponsePaymentOrderEntity.from_dict(buy_btc_response_payment_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


