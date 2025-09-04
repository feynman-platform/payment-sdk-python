# buybtcpay.PayoutApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**open_payout**](PayoutApi.md#open_payout) | **POST** /v1/payment/open/payout | 商户开放API发起支付
[**pagination2**](PayoutApi.md#pagination2) | **POST** /v1/payment/pagination | 
[**payout**](PayoutApi.md#payout) | **POST** /v1/payment/payout | 登录商户发起支付
[**test**](PayoutApi.md#test) | **GET** /v1/payment/test | 


# **open_payout**
> BuyBtcResponsePayoutOpenApiResponseDto open_payout(payout_request_dto)

商户开放API发起支付

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payout_open_api_response_dto import BuyBtcResponsePayoutOpenApiResponseDto
from buybtcpay.models.payout_request_dto import PayoutRequestDto
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
    api_instance = buybtcpay.PayoutApi(api_client)
    payout_request_dto = buybtcpay.PayoutRequestDto() # PayoutRequestDto | 

    try:
        # 商户开放API发起支付
        api_response = api_instance.open_payout(payout_request_dto)
        print("The response of PayoutApi->open_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->open_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_request_dto** | [**PayoutRequestDto**](PayoutRequestDto.md)|  | 

### Return type

[**BuyBtcResponsePayoutOpenApiResponseDto**](BuyBtcResponsePayoutOpenApiResponseDto.md)

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

# **pagination2**
> PayResponsePaginationPayoutEntityDto pagination2(pay_pagination_query_payout_pagination_query)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_payout_pagination_query import PayPaginationQueryPayoutPaginationQuery
from buybtcpay.models.pay_response_pagination_payout_entity_dto import PayResponsePaginationPayoutEntityDto
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
    api_instance = buybtcpay.PayoutApi(api_client)
    pay_pagination_query_payout_pagination_query = buybtcpay.PayPaginationQueryPayoutPaginationQuery() # PayPaginationQueryPayoutPaginationQuery | 

    try:
        api_response = api_instance.pagination2(pay_pagination_query_payout_pagination_query)
        print("The response of PayoutApi->pagination2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->pagination2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_payout_pagination_query** | [**PayPaginationQueryPayoutPaginationQuery**](PayPaginationQueryPayoutPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationPayoutEntityDto**](PayResponsePaginationPayoutEntityDto.md)

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

# **payout**
> BuyBtcResponsePayoutResponseEntity payout(merchant_payout_request_dto)

登录商户发起支付

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payout_response_entity import BuyBtcResponsePayoutResponseEntity
from buybtcpay.models.merchant_payout_request_dto import MerchantPayoutRequestDto
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
    api_instance = buybtcpay.PayoutApi(api_client)
    merchant_payout_request_dto = buybtcpay.MerchantPayoutRequestDto() # MerchantPayoutRequestDto | 

    try:
        # 登录商户发起支付
        api_response = api_instance.payout(merchant_payout_request_dto)
        print("The response of PayoutApi->payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_payout_request_dto** | [**MerchantPayoutRequestDto**](MerchantPayoutRequestDto.md)|  | 

### Return type

[**BuyBtcResponsePayoutResponseEntity**](BuyBtcResponsePayoutResponseEntity.md)

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

# **test**
> BuyBtcResponsePayoutResponseEntity test()

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payout_response_entity import BuyBtcResponsePayoutResponseEntity
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
    api_instance = buybtcpay.PayoutApi(api_client)

    try:
        api_response = api_instance.test()
        print("The response of PayoutApi->test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->test: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponsePayoutResponseEntity**](BuyBtcResponsePayoutResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

