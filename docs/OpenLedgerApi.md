# buybtcpay.OpenLedgerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggration**](OpenLedgerApi.md#aggration) | **POST** /v1/open/ledger/transaction/aggration/{merchantId} | 账本


# **aggration**
> BuyBtcResponseLedgerTransactionAggregation aggration(merchant_id, pay_pagination_query_open_ledger_transaction_query)

账本

用于统计商户的收入、支出、冻结余额等信息，商户可以查看自己的信息，也可以查询所属的虚拟账户信息

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_ledger_transaction_aggregation import BuyBtcResponseLedgerTransactionAggregation
from buybtcpay.models.pay_pagination_query_open_ledger_transaction_query import PayPaginationQueryOpenLedgerTransactionQuery
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
    api_instance = buybtcpay.OpenLedgerApi(api_client)
    merchant_id = 'merchant_id_example' # str | 
    pay_pagination_query_open_ledger_transaction_query = buybtcpay.PayPaginationQueryOpenLedgerTransactionQuery() # PayPaginationQueryOpenLedgerTransactionQuery | 

    try:
        # 账本
        api_response = api_instance.aggration(merchant_id, pay_pagination_query_open_ledger_transaction_query)
        print("The response of OpenLedgerApi->aggration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenLedgerApi->aggration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **pay_pagination_query_open_ledger_transaction_query** | [**PayPaginationQueryOpenLedgerTransactionQuery**](PayPaginationQueryOpenLedgerTransactionQuery.md)|  | 

### Return type

[**BuyBtcResponseLedgerTransactionAggregation**](BuyBtcResponseLedgerTransactionAggregation.md)

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

