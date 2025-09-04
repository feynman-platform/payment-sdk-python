# buybtcpay.NotifyMqControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_message**](NotifyMqControllerApi.md#send_message) | **GET** /v1/mq/notify/send | 


# **send_message**
> str send_message()

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
    api_instance = buybtcpay.NotifyMqControllerApi(api_client)

    try:
        api_response = api_instance.send_message()
        print("The response of NotifyMqControllerApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotifyMqControllerApi->send_message: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

