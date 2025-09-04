# BuyBtcResponsePayPaginationPayoutEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayPaginationPayoutEntityDto**](PayPaginationPayoutEntityDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_pay_pagination_payout_entity_dto import BuyBtcResponsePayPaginationPayoutEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayPaginationPayoutEntityDto from a JSON string
buy_btc_response_pay_pagination_payout_entity_dto_instance = BuyBtcResponsePayPaginationPayoutEntityDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayPaginationPayoutEntityDto.to_json())

# convert the object into a dict
buy_btc_response_pay_pagination_payout_entity_dto_dict = buy_btc_response_pay_pagination_payout_entity_dto_instance.to_dict()
# create an instance of BuyBtcResponsePayPaginationPayoutEntityDto from a dict
buy_btc_response_pay_pagination_payout_entity_dto_from_dict = BuyBtcResponsePayPaginationPayoutEntityDto.from_dict(buy_btc_response_pay_pagination_payout_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


