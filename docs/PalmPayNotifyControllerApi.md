# buybtcpay.PalmPayNotifyControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify**](PalmPayNotifyControllerApi.md#notify) | **POST** /v1/notify/palmpay | 
[**pagination10**](PalmPayNotifyControllerApi.md#pagination10) | **POST** /v1/notify/pagination | 
[**resend_palm_pay_notify**](PalmPayNotifyControllerApi.md#resend_palm_pay_notify) | **POST** /v1/notify/resend/{id} | 
[**virtual_account_topup_notify**](PalmPayNotifyControllerApi.md#virtual_account_topup_notify) | **POST** /v1/notify/palmpay/va/topup | 


# **notify**
> str notify(body)

### Example


```python
import buybtcpay
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
    api_instance = buybtcpay.PalmPayNotifyControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        api_response = api_instance.notify(body)
        print("The response of PalmPayNotifyControllerApi->notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayNotifyControllerApi->notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

# **pagination10**
> PayResponsePaginationPalmPayNotifyEntity pagination10(pay_pagination_query_palm_pay_notify_pagination_query)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_palm_pay_notify_pagination_query import PayPaginationQueryPalmPayNotifyPaginationQuery
from buybtcpay.models.pay_response_pagination_palm_pay_notify_entity import PayResponsePaginationPalmPayNotifyEntity
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
    api_instance = buybtcpay.PalmPayNotifyControllerApi(api_client)
    pay_pagination_query_palm_pay_notify_pagination_query = buybtcpay.PayPaginationQueryPalmPayNotifyPaginationQuery() # PayPaginationQueryPalmPayNotifyPaginationQuery | 

    try:
        api_response = api_instance.pagination10(pay_pagination_query_palm_pay_notify_pagination_query)
        print("The response of PalmPayNotifyControllerApi->pagination10:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayNotifyControllerApi->pagination10: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_palm_pay_notify_pagination_query** | [**PayPaginationQueryPalmPayNotifyPaginationQuery**](PayPaginationQueryPalmPayNotifyPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationPalmPayNotifyEntity**](PayResponsePaginationPalmPayNotifyEntity.md)

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

# **resend_palm_pay_notify**
> BuyBtcResponseBoolean resend_palm_pay_notify(id)

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_boolean import BuyBtcResponseBoolean
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
    api_instance = buybtcpay.PalmPayNotifyControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.resend_palm_pay_notify(id)
        print("The response of PalmPayNotifyControllerApi->resend_palm_pay_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayNotifyControllerApi->resend_palm_pay_notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BuyBtcResponseBoolean**](BuyBtcResponseBoolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_account_topup_notify**
> str virtual_account_topup_notify(body)

### Example


```python
import buybtcpay
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
    api_instance = buybtcpay.PalmPayNotifyControllerApi(api_client)
    body = 'body_example' # str | 

    try:
        api_response = api_instance.virtual_account_topup_notify(body)
        print("The response of PalmPayNotifyControllerApi->virtual_account_topup_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayNotifyControllerApi->virtual_account_topup_notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

**str**

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

