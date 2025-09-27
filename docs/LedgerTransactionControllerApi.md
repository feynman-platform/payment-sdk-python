# buybtcpay.LedgerTransactionControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregation1**](LedgerTransactionControllerApi.md#aggregation1) | **POST** /v1/ledger/transaction/aggregation | 
[**merchant_available_balance_aggregation**](LedgerTransactionControllerApi.md#merchant_available_balance_aggregation) | **POST** /v1/ledger/transaction/merchant/aggregation | 
[**pagination13**](LedgerTransactionControllerApi.md#pagination13) | **POST** /v1/ledger/transaction/pagination | 


# **aggregation1**
> BuyBtcResponseLedgerTransactionAggregation aggregation1(pay_pagination_query_ledger_transaction_query)

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
        api_response = api_instance.aggregation1(pay_pagination_query_ledger_transaction_query)
        print("The response of LedgerTransactionControllerApi->aggregation1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTransactionControllerApi->aggregation1: %s\n" % e)
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

# **merchant_available_balance_aggregation**
> BuyBtcResponseLedgerTransactionAggregation merchant_available_balance_aggregation(pay_pagination_query_ledger_transaction_latest_merchant_account_query)

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_ledger_transaction_aggregation import BuyBtcResponseLedgerTransactionAggregation
from buybtcpay.models.pay_pagination_query_ledger_transaction_latest_merchant_account_query import PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery
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
    pay_pagination_query_ledger_transaction_latest_merchant_account_query = buybtcpay.PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery() # PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery | 

    try:
        api_response = api_instance.merchant_available_balance_aggregation(pay_pagination_query_ledger_transaction_latest_merchant_account_query)
        print("The response of LedgerTransactionControllerApi->merchant_available_balance_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerTransactionControllerApi->merchant_available_balance_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_ledger_transaction_latest_merchant_account_query** | [**PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery**](PayPaginationQueryLedgerTransactionLatestMerchantAccountQuery.md)|  | 

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

