# buybtcpay.PrepaymentOrderApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagination**](PrepaymentOrderApi.md#pagination) | **POST** /v1/prepayment/order/pagination | 分页查询预付单


# **pagination**
> BuyBtcResponsePayPaginationPrepaymentOrderEntity pagination(pay_pagination_query_prepayment_order_pagination_query)

分页查询预付单

分页查询预付单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_prepayment_order_entity import BuyBtcResponsePayPaginationPrepaymentOrderEntity
from buybtcpay.models.pay_pagination_query_prepayment_order_pagination_query import PayPaginationQueryPrepaymentOrderPaginationQuery
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
    api_instance = buybtcpay.PrepaymentOrderApi(api_client)
    pay_pagination_query_prepayment_order_pagination_query = buybtcpay.PayPaginationQueryPrepaymentOrderPaginationQuery() # PayPaginationQueryPrepaymentOrderPaginationQuery | 

    try:
        # 分页查询预付单
        api_response = api_instance.pagination(pay_pagination_query_prepayment_order_pagination_query)
        print("The response of PrepaymentOrderApi->pagination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrepaymentOrderApi->pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_prepayment_order_pagination_query** | [**PayPaginationQueryPrepaymentOrderPaginationQuery**](PayPaginationQueryPrepaymentOrderPaginationQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationPrepaymentOrderEntity**](BuyBtcResponsePayPaginationPrepaymentOrderEntity.md)

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

