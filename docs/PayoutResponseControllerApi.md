# buybtcpay.PayoutResponseControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagination1**](PayoutResponseControllerApi.md#pagination1) | **POST** /v1/payout/response/pagination | 


# **pagination1**
> PayResponsePaginationPayoutResponseEntity pagination1(pay_pagination_query_pagination_query)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_pagination_query import PayPaginationQueryPaginationQuery
from buybtcpay.models.pay_response_pagination_payout_response_entity import PayResponsePaginationPayoutResponseEntity
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
    api_instance = buybtcpay.PayoutResponseControllerApi(api_client)
    pay_pagination_query_pagination_query = buybtcpay.PayPaginationQueryPaginationQuery() # PayPaginationQueryPaginationQuery | 

    try:
        api_response = api_instance.pagination1(pay_pagination_query_pagination_query)
        print("The response of PayoutResponseControllerApi->pagination1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutResponseControllerApi->pagination1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_pagination_query** | [**PayPaginationQueryPaginationQuery**](PayPaginationQueryPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationPayoutResponseEntity**](PayResponsePaginationPayoutResponseEntity.md)

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

