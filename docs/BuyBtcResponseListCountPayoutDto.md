# BuyBtcResponseListCountPayoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**List[CountPayoutDto]**](CountPayoutDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_list_count_payout_dto import BuyBtcResponseListCountPayoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseListCountPayoutDto from a JSON string
buy_btc_response_list_count_payout_dto_instance = BuyBtcResponseListCountPayoutDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseListCountPayoutDto.to_json())

# convert the object into a dict
buy_btc_response_list_count_payout_dto_dict = buy_btc_response_list_count_payout_dto_instance.to_dict()
# create an instance of BuyBtcResponseListCountPayoutDto from a dict
buy_btc_response_list_count_payout_dto_from_dict = BuyBtcResponseListCountPayoutDto.from_dict(buy_btc_response_list_count_payout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


