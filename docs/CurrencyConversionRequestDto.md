# CurrencyConversionRequestDto

汇率转换请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**target** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**value** | **str** | 源币种金额 | 

## Example

```python
from buybtcpay.models.currency_conversion_request_dto import CurrencyConversionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConversionRequestDto from a JSON string
currency_conversion_request_dto_instance = CurrencyConversionRequestDto.from_json(json)
# print the JSON string representation of the object
print(CurrencyConversionRequestDto.to_json())

# convert the object into a dict
currency_conversion_request_dto_dict = currency_conversion_request_dto_instance.to_dict()
# create an instance of CurrencyConversionRequestDto from a dict
currency_conversion_request_dto_from_dict = CurrencyConversionRequestDto.from_dict(currency_conversion_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


