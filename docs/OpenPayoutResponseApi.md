# buybtcpay.OpenPayoutResponseApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagination5**](OpenPayoutResponseApi.md#pagination5) | **POST** /v1/open/payout/response/pagination | 分页查询商户的支付响应数据


# **pagination5**
> BuyBtcResponsePayPaginationPayoutResponseEntity pagination5(pay_pagination_query_pagination_query)

分页查询商户的支付响应数据

普通账户可以查自己以及所属虚拟账户的记录，虚拟账户只能查询自己的支付记录

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_payout_response_entity import BuyBtcResponsePayPaginationPayoutResponseEntity
from buybtcpay.models.pay_pagination_query_pagination_query import PayPaginationQueryPaginationQuery
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
    api_instance = buybtcpay.OpenPayoutResponseApi(api_client)
    pay_pagination_query_pagination_query = buybtcpay.PayPaginationQueryPaginationQuery() # PayPaginationQueryPaginationQuery | 

    try:
        # 分页查询商户的支付响应数据
        api_response = api_instance.pagination5(pay_pagination_query_pagination_query)
        print("The response of OpenPayoutResponseApi->pagination5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPayoutResponseApi->pagination5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_pagination_query** | [**PayPaginationQueryPaginationQuery**](PayPaginationQueryPaginationQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationPayoutResponseEntity**](BuyBtcResponsePayPaginationPayoutResponseEntity.md)

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

