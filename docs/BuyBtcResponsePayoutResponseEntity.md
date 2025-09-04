# BuyBtcResponsePayoutResponseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayoutResponseEntity**](PayoutResponseEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_payout_response_entity import BuyBtcResponsePayoutResponseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayoutResponseEntity from a JSON string
buy_btc_response_payout_response_entity_instance = BuyBtcResponsePayoutResponseEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayoutResponseEntity.to_json())

# convert the object into a dict
buy_btc_response_payout_response_entity_dict = buy_btc_response_payout_response_entity_instance.to_dict()
# create an instance of BuyBtcResponsePayoutResponseEntity from a dict
buy_btc_response_payout_response_entity_from_dict = BuyBtcResponsePayoutResponseEntity.from_dict(buy_btc_response_payout_response_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


