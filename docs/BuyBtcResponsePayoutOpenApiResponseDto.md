# BuyBtcResponsePayoutOpenApiResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**PayoutOpenApiResponseDto**](PayoutOpenApiResponseDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_payout_open_api_response_dto import BuyBtcResponsePayoutOpenApiResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponsePayoutOpenApiResponseDto from a JSON string
buy_btc_response_payout_open_api_response_dto_instance = BuyBtcResponsePayoutOpenApiResponseDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponsePayoutOpenApiResponseDto.to_json())

# convert the object into a dict
buy_btc_response_payout_open_api_response_dto_dict = buy_btc_response_payout_open_api_response_dto_instance.to_dict()
# create an instance of BuyBtcResponsePayoutOpenApiResponseDto from a dict
buy_btc_response_payout_open_api_response_dto_from_dict = BuyBtcResponsePayoutOpenApiResponseDto.from_dict(buy_btc_response_payout_open_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


