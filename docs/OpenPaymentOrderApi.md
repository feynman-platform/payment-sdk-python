# buybtcpay.OpenPaymentOrderApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_by_order_id**](OpenPaymentOrderApi.md#find_by_order_id) | **POST** /v1/open/payment/order/{orderId} | 查询支付单
[**pagination6**](OpenPaymentOrderApi.md#pagination6) | **POST** /v1/open/payment/order/pagination | 分页查询支付单


# **find_by_order_id**
> BuyBtcResponsePaymentOrderEntity find_by_order_id(order_id)

查询支付单

根据订单号查询支付单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
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
    api_instance = buybtcpay.OpenPaymentOrderApi(api_client)
    order_id = 'order_id_example' # str | 

    try:
        # 查询支付单
        api_response = api_instance.find_by_order_id(order_id)
        print("The response of OpenPaymentOrderApi->find_by_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPaymentOrderApi->find_by_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**BuyBtcResponsePaymentOrderEntity**](BuyBtcResponsePaymentOrderEntity.md)

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

# **pagination6**
> BuyBtcResponsePayPaginationPaymentOrderEntity pagination6(pay_pagination_query_payment_order_pagination_query)

分页查询支付单

分页查询支付单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_payment_order_entity import BuyBtcResponsePayPaginationPaymentOrderEntity
from buybtcpay.models.pay_pagination_query_payment_order_pagination_query import PayPaginationQueryPaymentOrderPaginationQuery
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
    api_instance = buybtcpay.OpenPaymentOrderApi(api_client)
    pay_pagination_query_payment_order_pagination_query = buybtcpay.PayPaginationQueryPaymentOrderPaginationQuery() # PayPaginationQueryPaymentOrderPaginationQuery | 

    try:
        # 分页查询支付单
        api_response = api_instance.pagination6(pay_pagination_query_payment_order_pagination_query)
        print("The response of OpenPaymentOrderApi->pagination6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPaymentOrderApi->pagination6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_payment_order_pagination_query** | [**PayPaginationQueryPaymentOrderPaginationQuery**](PayPaginationQueryPaymentOrderPaginationQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationPaymentOrderEntity**](BuyBtcResponsePayPaginationPaymentOrderEntity.md)

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

