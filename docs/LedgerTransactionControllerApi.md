# buybtcpay.LedgerTransactionControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggration1**](LedgerTransactionControllerApi.md#aggration1) | **POST** /v1/ledger/transaction/aggregation | 
[**pagination13**](LedgerTransactionControllerApi.md#pagination13) | **POST** /v1/ledger/transaction/pagination | 
[**virtual_account_aggregation**](LedgerTransactionControllerApi.md#virtual_account_aggregation) | **POST** /v1/ledger/transaction/virtual/account/aggregation | 


# **aggration1**
> BuyBtcResponseLedgerTransactionAggregation aggration1(pay_pagination_query_ledger_transaction_query)

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_ledger_transaction_aggregation import BuyBtcResponseLedgerTransactionAggregation
from buybtcpay.models.pay_pagination_query_ledger_transaction_query import PayPaginationQueryLedgerTransactionQuery
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
    api_instance = buybtcpay.LedgerTransactionControllerApi(api_client)
    pay_pagination_query_ledger_transaction_query = buybtcpay.PayPaginationQueryLedgerTransactionQuery() # PayPaginationQueryLedgerTransactionQuery | 

    try:
        api_response = api_instance.aggration1(pay_pagination_query_ledger_transaction_query)
        print("The response of LedgerTransactionControllerApi->aggration1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTransactionControllerApi->aggration1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_ledger_transaction_query** | [**PayPaginationQueryLedgerTransactionQuery**](PayPaginationQueryLedgerTransactionQuery.md)|  | 

### Return type

[**BuyBtcResponseLedgerTransactionAggregation**](BuyBtcResponseLedgerTransactionAggregation.md)

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

# **pagination13**
> PayResponsePaginationLedgerTransactionEntity pagination13(pay_pagination_query_ledger_transaction_query)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_ledger_transaction_query import PayPaginationQueryLedgerTransactionQuery
from buybtcpay.models.pay_response_pagination_ledger_transaction_entity import PayResponsePaginationLedgerTransactionEntity
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
    api_instance = buybtcpay.LedgerTransactionControllerApi(api_client)
    pay_pagination_query_ledger_transaction_query = buybtcpay.PayPaginationQueryLedgerTransactionQuery() # PayPaginationQueryLedgerTransactionQuery | 

    try:
        api_response = api_instance.pagination13(pay_pagination_query_ledger_transaction_query)
        print("The response of LedgerTransactionControllerApi->pagination13:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTransactionControllerApi->pagination13: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_ledger_transaction_query** | [**PayPaginationQueryLedgerTransactionQuery**](PayPaginationQueryLedgerTransactionQuery.md)|  | 

### Return type

[**PayResponsePaginationLedgerTransactionEntity**](PayResponsePaginationLedgerTransactionEntity.md)

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

# **virtual_account_aggregation**
> BuyBtcResponseLedgerTransactionAggregation virtual_account_aggregation(pay_pagination_query_ledger_transaction_latest_virtual_account_query)

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_ledger_transaction_aggregation import BuyBtcResponseLedgerTransactionAggregation
from buybtcpay.models.pay_pagination_query_ledger_transaction_latest_virtual_account_query import PayPaginationQueryLedgerTransactionLatestVirtualAccountQuery
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
    api_instance = buybtcpay.LedgerTransactionControllerApi(api_client)
    pay_pagination_query_ledger_transaction_latest_virtual_account_query = buybtcpay.PayPaginationQueryLedgerTransactionLatestVirtualAccountQuery() # PayPaginationQueryLedgerTransactionLatestVirtualAccountQuery | 

    try:
        api_response = api_instance.virtual_account_aggregation(pay_pagination_query_ledger_transaction_latest_virtual_account_query)
        print("The response of LedgerTransactionControllerApi->virtual_account_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTransactionControllerApi->virtual_account_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_ledger_transaction_latest_virtual_account_query** | [**PayPaginationQueryLedgerTransactionLatestVirtualAccountQuery**](PayPaginationQueryLedgerTransactionLatestVirtualAccountQuery.md)|  | 

### Return type

[**BuyBtcResponseLedgerTransactionAggregation**](BuyBtcResponseLedgerTransactionAggregation.md)

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

