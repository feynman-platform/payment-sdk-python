# buybtcpay.OpenMerchantBillApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagination8**](OpenMerchantBillApi.md#pagination8) | **POST** /v1/open/merchant/bill/pagination | 分页查询


# **pagination8**
> BuyBtcResponsePayPaginationMerchantBillEntity pagination8(pay_pagination_query_merchant_bill_query)

分页查询

分页查询商户流水，如果不是管理员，必须传入merchantId参数

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_merchant_bill_entity import BuyBtcResponsePayPaginationMerchantBillEntity
from buybtcpay.models.pay_pagination_query_merchant_bill_query import PayPaginationQueryMerchantBillQuery
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
    api_instance = buybtcpay.OpenMerchantBillApi(api_client)
    pay_pagination_query_merchant_bill_query = buybtcpay.PayPaginationQueryMerchantBillQuery() # PayPaginationQueryMerchantBillQuery | 

    try:
        # 分页查询
        api_response = api_instance.pagination8(pay_pagination_query_merchant_bill_query)
        print("The response of OpenMerchantBillApi->pagination8:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantBillApi->pagination8: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_merchant_bill_query** | [**PayPaginationQueryMerchantBillQuery**](PayPaginationQueryMerchantBillQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationMerchantBillEntity**](BuyBtcResponsePayPaginationMerchantBillEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

