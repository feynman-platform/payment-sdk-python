# CurrencyConversionDto

货币转换请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**Verification**](Verification.md) |  | [optional] 
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**payer** | **str** |  | 
**payee** | **str** |  | 
**source_currency** | **str** | 货币类型 | 
**target_currency** | **str** | 货币类型 | 
**amount** | **str** |  | 
**time_id** | **str** |  | 
**note** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.currency_conversion_dto import CurrencyConversionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyConversionDto from a JSON string
currency_conversion_dto_instance = CurrencyConversionDto.from_json(json)
# print the JSON string representation of the object
print(CurrencyConversionDto.to_json())

# convert the object into a dict
currency_conversion_dto_dict = currency_conversion_dto_instance.to_dict()
# create an instance of CurrencyConversionDto from a dict
currency_conversion_dto_from_dict = CurrencyConversionDto.from_dict(currency_conversion_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


