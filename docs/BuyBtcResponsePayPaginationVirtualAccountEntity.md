# BuyBtcResponsePayPaginationVirtualAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayPaginationVirtualAccountEntity**](PayPaginationVirtualAccountEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_pay_pagination_virtual_account_entity import BuyBtcResponsePayPaginationVirtualAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayPaginationVirtualAccountEntity from a JSON string
buy_btc_response_pay_pagination_virtual_account_entity_instance = BuyBtcResponsePayPaginationVirtualAccountEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayPaginationVirtualAccountEntity.to_json())

# convert the object into a dict
buy_btc_response_pay_pagination_virtual_account_entity_dict = buy_btc_response_pay_pagination_virtual_account_entity_instance.to_dict()
# create an instance of BuyBtcResponsePayPaginationVirtualAccountEntity from a dict
buy_btc_response_pay_pagination_virtual_account_entity_from_dict = BuyBtcResponsePayPaginationVirtualAccountEntity.from_dict(buy_btc_response_pay_pagination_virtual_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


