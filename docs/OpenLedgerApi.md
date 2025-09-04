# buybtcpay.OpenLedgerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggration**](OpenLedgerApi.md#aggration) | **POST** /v1/open/ledger/transaction/aggration/{merchantId} | 账本
[**merchant_in_and_out**](OpenLedgerApi.md#merchant_in_and_out) | **POST** /v1/open/ledger/transaction/io/{merchantId} | 商户收支查询


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

# **merchant_in_and_out**
> BuyBtcResponsePayPaginationLedgerTransactionEntity merchant_in_and_out(merchant_id, pay_pagination_query_merchant_in_and_out_query)

商户收支查询

# 查询商户收入、支出记录

## 收入:
- 充值
- 子账户充值，账户类型为子账户
- 退款（账户类型为商户的记录）
- 解冻 （账户类型为商户的记录）
- 商户到商户（记账方向为借）
- 商户到商户不同币种（记账方向为借）
- 冲销：平台到商户，账户类型为商户
- 冲销：商户到商户（记账方向为借）

## 支出：
- 子账户充值，账户类型商户
- 代付，账户类型为商户冻结：代付成功后从冻结金额中扣款
- 费用，账户类型为商户冻结，交易对方账户类型为平台账户，交易对方账户为平台手续费账户：代付成功后手续费
- 商户到商户，记账方向为贷：向商户转账
- 商户到商户不同币种，记账方向为贷：向商户转账
- 冲销：商户到商户，记账方向为贷
- 冲销：商户到平台，记账方向为贷


### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_ledger_transaction_entity import BuyBtcResponsePayPaginationLedgerTransactionEntity
from buybtcpay.models.pay_pagination_query_merchant_in_and_out_query import PayPaginationQueryMerchantInAndOutQuery
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
    pay_pagination_query_merchant_in_and_out_query = buybtcpay.PayPaginationQueryMerchantInAndOutQuery() # PayPaginationQueryMerchantInAndOutQuery | 

    try:
        # 商户收支查询
        api_response = api_instance.merchant_in_and_out(merchant_id, pay_pagination_query_merchant_in_and_out_query)
        print("The response of OpenLedgerApi->merchant_in_and_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenLedgerApi->merchant_in_and_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **pay_pagination_query_merchant_in_and_out_query** | [**PayPaginationQueryMerchantInAndOutQuery**](PayPaginationQueryMerchantInAndOutQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationLedgerTransactionEntity**](BuyBtcResponsePayPaginationLedgerTransactionEntity.md)

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

