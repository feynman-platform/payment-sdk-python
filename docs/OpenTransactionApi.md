# buybtcpay.OpenTransactionApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_to_merchant**](OpenTransactionApi.md#merchant_to_merchant) | **POST** /v1/open/transaction/merchant/to/merchant | 商户间转账


# **merchant_to_merchant**
> BuyBtcResponseMerchantTransactionEntity merchant_to_merchant(merchant_to_merchant_transaction_request_dto)

商户间转账

请求参数需要签名，签名算法见MD文档 <br />该接口有限流设置，不要频繁调用

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_transaction_entity import BuyBtcResponseMerchantTransactionEntity
from buybtcpay.models.merchant_to_merchant_transaction_request_dto import MerchantToMerchantTransactionRequestDto
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
    api_instance = buybtcpay.OpenTransactionApi(api_client)
    merchant_to_merchant_transaction_request_dto = buybtcpay.MerchantToMerchantTransactionRequestDto() # MerchantToMerchantTransactionRequestDto | 

    try:
        # 商户间转账
        api_response = api_instance.merchant_to_merchant(merchant_to_merchant_transaction_request_dto)
        print("The response of OpenTransactionApi->merchant_to_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenTransactionApi->merchant_to_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_to_merchant_transaction_request_dto** | [**MerchantToMerchantTransactionRequestDto**](MerchantToMerchantTransactionRequestDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantTransactionEntity**](BuyBtcResponseMerchantTransactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

