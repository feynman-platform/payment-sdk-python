# BuyBtcResponsePayPaginationMerchantBillEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayPaginationMerchantBillEntity**](PayPaginationMerchantBillEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_pay_pagination_merchant_bill_entity import BuyBtcResponsePayPaginationMerchantBillEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayPaginationMerchantBillEntity from a JSON string
buy_btc_response_pay_pagination_merchant_bill_entity_instance = BuyBtcResponsePayPaginationMerchantBillEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayPaginationMerchantBillEntity.to_json())

# convert the object into a dict
buy_btc_response_pay_pagination_merchant_bill_entity_dict = buy_btc_response_pay_pagination_merchant_bill_entity_instance.to_dict()
# create an instance of BuyBtcResponsePayPaginationMerchantBillEntity from a dict
buy_btc_response_pay_pagination_merchant_bill_entity_from_dict = BuyBtcResponsePayPaginationMerchantBillEntity.from_dict(buy_btc_response_pay_pagination_merchant_bill_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


