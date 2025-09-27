# buybtcpay.PayoutApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**open_payout**](PayoutApi.md#open_payout) | **POST** /v1/payment/dev/payout | 
[**pagination2**](PayoutApi.md#pagination2) | **POST** /v1/payment/pagination | 
[**payout**](PayoutApi.md#payout) | **POST** /v1/payment/payout | 登录商户发起支付
[**withdraw**](PayoutApi.md#withdraw) | **POST** /v1/payment/withdraw | 登录商户发起提现


# **open_payout**
> BuyBtcResponsePayoutResponseEntity open_payout(merchant_payout_request_dto)

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
        api_response = api_instance.open_payout(merchant_payout_request_dto)
        print("The response of PayoutApi->open_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->open_payout: %s\n" % e)
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

# **withdraw**
> BuyBtcResponsePayoutResponseEntity withdraw(merchant_payout_request_dto)

登录商户发起提现

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
        # 登录商户发起提现
        api_response = api_instance.withdraw(merchant_payout_request_dto)
        print("The response of PayoutApi->withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutApi->withdraw: %s\n" % e)
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

