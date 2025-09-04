# buybtcpay.OpenQueryPayStatusApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_check_order_data**](OpenQueryPayStatusApi.md#query_check_order_data) | **POST** /v1/open/pay/status/{orderId}/order/data | 代付银行查询交易单状态
[**query_pay_status**](OpenQueryPayStatusApi.md#query_pay_status) | **POST** /v1/open/pay/status/{orderId} | 查询交易单状态


# **query_check_order_data**
> BuyBtcResponseQueryPayStatusResponse query_check_order_data(order_id)

代付银行查询交易单状态

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_query_pay_status_response import BuyBtcResponseQueryPayStatusResponse
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
    api_instance = buybtcpay.OpenQueryPayStatusApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # 代付银行查询交易单状态
        api_response = api_instance.query_check_order_data(order_id)
        print("The response of OpenQueryPayStatusApi->query_check_order_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenQueryPayStatusApi->query_check_order_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**BuyBtcResponseQueryPayStatusResponse**](BuyBtcResponseQueryPayStatusResponse.md)

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

# **query_pay_status**
> BuyBtcResponsePalmPayNotifyEntity query_pay_status(order_id)

查询交易单状态

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_palm_pay_notify_entity import BuyBtcResponsePalmPayNotifyEntity
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
    api_instance = buybtcpay.OpenQueryPayStatusApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # 查询交易单状态
        api_response = api_instance.query_pay_status(order_id)
        print("The response of OpenQueryPayStatusApi->query_pay_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenQueryPayStatusApi->query_pay_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**BuyBtcResponsePalmPayNotifyEntity**](BuyBtcResponsePalmPayNotifyEntity.md)

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

