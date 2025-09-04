# buybtcpay.OpenPayoutApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagination7**](OpenPayoutApi.md#pagination7) | **POST** /v1/open/pay/pagination | 用户代付列表
[**payout1**](OpenPayoutApi.md#payout1) | **POST** /v1/open/pay/payout | 用户代付接口


# **pagination7**
> BuyBtcResponsePayPaginationPayoutEntityDto pagination7(pay_pagination_query_payout_pagination_query)

用户代付列表

仅能查询商户自己与子账户的代付记录，merchantId必传

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_payout_entity_dto import BuyBtcResponsePayPaginationPayoutEntityDto
from buybtcpay.models.pay_pagination_query_payout_pagination_query import PayPaginationQueryPayoutPaginationQuery
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
    api_instance = buybtcpay.OpenPayoutApi(api_client)
    pay_pagination_query_payout_pagination_query = buybtcpay.PayPaginationQueryPayoutPaginationQuery() # PayPaginationQueryPayoutPaginationQuery | 

    try:
        # 用户代付列表
        api_response = api_instance.pagination7(pay_pagination_query_payout_pagination_query)
        print("The response of OpenPayoutApi->pagination7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPayoutApi->pagination7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_payout_pagination_query** | [**PayPaginationQueryPayoutPaginationQuery**](PayPaginationQueryPayoutPaginationQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationPayoutEntityDto**](BuyBtcResponsePayPaginationPayoutEntityDto.md)

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

# **payout1**
> BuyBtcResponsePayoutOpenApiResponseDto payout1(open_payout_request_dto)

用户代付接口

请求参数需要签名，签名算法见MD文档 <br />该接口有限流设置，不要频繁调用

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payout_open_api_response_dto import BuyBtcResponsePayoutOpenApiResponseDto
from buybtcpay.models.open_payout_request_dto import OpenPayoutRequestDto
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
    api_instance = buybtcpay.OpenPayoutApi(api_client)
    open_payout_request_dto = buybtcpay.OpenPayoutRequestDto() # OpenPayoutRequestDto | 

    try:
        # 用户代付接口
        api_response = api_instance.payout1(open_payout_request_dto)
        print("The response of OpenPayoutApi->payout1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPayoutApi->payout1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_payout_request_dto** | [**OpenPayoutRequestDto**](OpenPayoutRequestDto.md)|  | 

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

