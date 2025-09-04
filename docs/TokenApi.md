# buybtcpay.TokenApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_merchant_refresh_token**](TokenApi.md#create_merchant_refresh_token) | **POST** /v1/auth/token | 创建商户AccessToken
[**delete**](TokenApi.md#delete) | **POST** /v1/auth/token/delete | 删除Refresh Token
[**pagination14**](TokenApi.md#pagination14) | **POST** /v1/auth/token/pagination | 分页查询Refresh Token


# **create_merchant_refresh_token**
> BuyBtcResponseCreateMerchantAccessTokenDto create_merchant_refresh_token()

创建商户AccessToken

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_create_merchant_access_token_dto import BuyBtcResponseCreateMerchantAccessTokenDto
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
    api_instance = buybtcpay.TokenApi(api_client)

    try:
        # 创建商户AccessToken
        api_response = api_instance.create_merchant_refresh_token()
        print("The response of TokenApi->create_merchant_refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->create_merchant_refresh_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseCreateMerchantAccessTokenDto**](BuyBtcResponseCreateMerchantAccessTokenDto.md)

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

# **delete**
> BuyBtcResponseBoolean delete(delete_dto)

删除Refresh Token

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_boolean import BuyBtcResponseBoolean
from buybtcpay.models.delete_dto import DeleteDto
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
    api_instance = buybtcpay.TokenApi(api_client)
    delete_dto = buybtcpay.DeleteDto() # DeleteDto | 

    try:
        # 删除Refresh Token
        api_response = api_instance.delete(delete_dto)
        print("The response of TokenApi->delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_dto** | [**DeleteDto**](DeleteDto.md)|  | 

### Return type

[**BuyBtcResponseBoolean**](BuyBtcResponseBoolean.md)

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

# **pagination14**
> PayResponsePaginationRefreshTokenEntity pagination14(pay_pagination_query_refresh_token_pagination_query)

分页查询Refresh Token

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_refresh_token_pagination_query import PayPaginationQueryRefreshTokenPaginationQuery
from buybtcpay.models.pay_response_pagination_refresh_token_entity import PayResponsePaginationRefreshTokenEntity
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
    api_instance = buybtcpay.TokenApi(api_client)
    pay_pagination_query_refresh_token_pagination_query = buybtcpay.PayPaginationQueryRefreshTokenPaginationQuery() # PayPaginationQueryRefreshTokenPaginationQuery | 

    try:
        # 分页查询Refresh Token
        api_response = api_instance.pagination14(pay_pagination_query_refresh_token_pagination_query)
        print("The response of TokenApi->pagination14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->pagination14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_refresh_token_pagination_query** | [**PayPaginationQueryRefreshTokenPaginationQuery**](PayPaginationQueryRefreshTokenPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationRefreshTokenEntity**](PayResponsePaginationRefreshTokenEntity.md)

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

