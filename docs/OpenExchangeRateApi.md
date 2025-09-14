# buybtcpay.OpenExchangeRateApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_conversion1**](OpenExchangeRateApi.md#currency_conversion1) | **POST** /v1/open/exchange/rate/currency/conversion | 币种转换


# **currency_conversion1**
> BuyBtcResponseCurrencyConversionResponseDto currency_conversion1(currency_conversion_request_dto)

币种转换

将源币种金额转换为目标币种金额

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_currency_conversion_response_dto import BuyBtcResponseCurrencyConversionResponseDto
from buybtcpay.models.currency_conversion_request_dto import CurrencyConversionRequestDto
from buybtcpay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9030
# See configuration.py for a list of all supported configuration parameters.
configuration = buybtcpay.Configuration(
    host = "http://localhost:9030"
)


# Enter a context with an instance of the API client
with buybtcpay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = buybtcpay.OpenExchangeRateApi(api_client)
    currency_conversion_request_dto = buybtcpay.CurrencyConversionRequestDto() # CurrencyConversionRequestDto | 

    try:
        # 币种转换
        api_response = api_instance.currency_conversion1(currency_conversion_request_dto)
        print("The response of OpenExchangeRateApi->currency_conversion1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenExchangeRateApi->currency_conversion1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_conversion_request_dto** | [**CurrencyConversionRequestDto**](CurrencyConversionRequestDto.md)|  | 

### Return type

[**BuyBtcResponseCurrencyConversionResponseDto**](BuyBtcResponseCurrencyConversionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

