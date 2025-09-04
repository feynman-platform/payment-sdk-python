# BuyBtcResponsePayPaginationPrepaymentOrderEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayPaginationPrepaymentOrderEntity**](PayPaginationPrepaymentOrderEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_pay_pagination_prepayment_order_entity import BuyBtcResponsePayPaginationPrepaymentOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayPaginationPrepaymentOrderEntity from a JSON string
buy_btc_response_pay_pagination_prepayment_order_entity_instance = BuyBtcResponsePayPaginationPrepaymentOrderEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayPaginationPrepaymentOrderEntity.to_json())

# convert the object into a dict
buy_btc_response_pay_pagination_prepayment_order_entity_dict = buy_btc_response_pay_pagination_prepayment_order_entity_instance.to_dict()
# create an instance of BuyBtcResponsePayPaginationPrepaymentOrderEntity from a dict
buy_btc_response_pay_pagination_prepayment_order_entity_from_dict = BuyBtcResponsePayPaginationPrepaymentOrderEntity.from_dict(buy_btc_response_pay_pagination_prepayment_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


