# BuyBtcResponseCurrencyConversionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**CurrencyConversionResponseDto**](CurrencyConversionResponseDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_currency_conversion_response_dto import BuyBtcResponseCurrencyConversionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseCurrencyConversionResponseDto from a JSON string
buy_btc_response_currency_conversion_response_dto_instance = BuyBtcResponseCurrencyConversionResponseDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseCurrencyConversionResponseDto.to_json())

# convert the object into a dict
buy_btc_response_currency_conversion_response_dto_dict = buy_btc_response_currency_conversion_response_dto_instance.to_dict()
# create an instance of BuyBtcResponseCurrencyConversionResponseDto from a dict
buy_btc_response_currency_conversion_response_dto_from_dict = BuyBtcResponseCurrencyConversionResponseDto.from_dict(buy_btc_response_currency_conversion_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


