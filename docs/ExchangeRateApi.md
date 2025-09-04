# buybtcpay.ExchangeRateApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate_list**](ExchangeRateApi.md#get_rate_list) | **POST** /v1/exchange/rate/pagination | 分页查询汇率列表


# **get_rate_list**
> GrpcListReplayCMRate get_rate_list(rate_list_request_query)

分页查询汇率列表

分页查询汇率列表

### Example


```python
import buybtcpay
from buybtcpay.models.grpc_list_replay_cm_rate import GrpcListReplayCMRate
from buybtcpay.models.rate_list_request_query import RateListRequestQuery
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
    api_instance = buybtcpay.ExchangeRateApi(api_client)
    rate_list_request_query = buybtcpay.RateListRequestQuery() # RateListRequestQuery | 

    try:
        # 分页查询汇率列表
        api_response = api_instance.get_rate_list(rate_list_request_query)
        print("The response of ExchangeRateApi->get_rate_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeRateApi->get_rate_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_list_request_query** | [**RateListRequestQuery**](RateListRequestQuery.md)|  | 

### Return type

[**GrpcListReplayCMRate**](GrpcListReplayCMRate.md)

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

