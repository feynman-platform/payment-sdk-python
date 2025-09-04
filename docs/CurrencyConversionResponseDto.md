# CurrencyConversionResponseDto

汇率转换响应参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**target** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**value** | **str** | 源币种金额 | 
**rate** | **str** | 汇率 | 
**amount** | **str** | 汇率转换后的金额 | 

## Example

```python
from buybtcpay.models.currency_conversion_response_dto import CurrencyConversionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConversionResponseDto from a JSON string
currency_conversion_response_dto_instance = CurrencyConversionResponseDto.from_json(json)
# print the JSON string representation of the object
print(CurrencyConversionResponseDto.to_json())

# convert the object into a dict
currency_conversion_response_dto_dict = currency_conversion_response_dto_instance.to_dict()
# create an instance of CurrencyConversionResponseDto from a dict
currency_conversion_response_dto_from_dict = CurrencyConversionResponseDto.from_dict(currency_conversion_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


