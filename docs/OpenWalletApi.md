# buybtcpay.OpenWalletApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregation**](OpenWalletApi.md#aggregation) | **POST** /v1/open/wallet/aggregation | 钱包金额汇总
[**find_by_currency**](OpenWalletApi.md#find_by_currency) | **POST** /v1/open/wallet/{merchantId}/{currency} | 查询商户指定币种钱包
[**find_by_merchant_id**](OpenWalletApi.md#find_by_merchant_id) | **POST** /v1/open/wallet/{merchantId} | 查询商户所有钱包
[**find_by_type_and_currency**](OpenWalletApi.md#find_by_type_and_currency) | **POST** /v1/open/wallet/{merchantId}/{currency}/{type} | 查询商户指定币种、类型的钱包
[**pagination4**](OpenWalletApi.md#pagination4) | **POST** /v1/open/wallet/pagination | 分页查询商户钱包
[**query_merchant_wallet_info**](OpenWalletApi.md#query_merchant_wallet_info) | **GET** /v1/open/wallet/info/{walletId} | 查询钱包信息


# **aggregation**
> BuyBtcResponseMerchantWalletCountVo aggregation(merchant_wallet_count_query)

钱包金额汇总

要求管理员权限

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_wallet_count_vo import BuyBtcResponseMerchantWalletCountVo
from buybtcpay.models.merchant_wallet_count_query import MerchantWalletCountQuery
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    merchant_wallet_count_query = buybtcpay.MerchantWalletCountQuery() # MerchantWalletCountQuery | 

    try:
        # 钱包金额汇总
        api_response = api_instance.aggregation(merchant_wallet_count_query)
        print("The response of OpenWalletApi->aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_wallet_count_query** | [**MerchantWalletCountQuery**](MerchantWalletCountQuery.md)|  | 

### Return type

[**BuyBtcResponseMerchantWalletCountVo**](BuyBtcResponseMerchantWalletCountVo.md)

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

# **find_by_currency**
> BuyBtcResponseListMerchantWalletEntity find_by_currency(merchant_id, currency)

查询商户指定币种钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    merchant_id = 'merchant_id_example' # str | 
    currency = 'currency_example' # str | 

    try:
        # 查询商户指定币种钱包
        api_response = api_instance.find_by_currency(merchant_id, currency)
        print("The response of OpenWalletApi->find_by_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->find_by_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **currency** | **str**|  | 

### Return type

[**BuyBtcResponseListMerchantWalletEntity**](BuyBtcResponseListMerchantWalletEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_merchant_id**
> BuyBtcResponseListMerchantWalletEntity find_by_merchant_id(merchant_id)

查询商户所有钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 查询商户所有钱包
        api_response = api_instance.find_by_merchant_id(merchant_id)
        print("The response of OpenWalletApi->find_by_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->find_by_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseListMerchantWalletEntity**](BuyBtcResponseListMerchantWalletEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_type_and_currency**
> BuyBtcResponseMerchantWalletEntity find_by_type_and_currency(merchant_id, currency, type)

查询商户指定币种、类型的钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_wallet_entity import BuyBtcResponseMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    merchant_id = 'merchant_id_example' # str | 
    currency = 'currency_example' # str | 
    type = 56 # int | 

    try:
        # 查询商户指定币种、类型的钱包
        api_response = api_instance.find_by_type_and_currency(merchant_id, currency, type)
        print("The response of OpenWalletApi->find_by_type_and_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->find_by_type_and_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **currency** | **str**|  | 
 **type** | **int**|  | 

### Return type

[**BuyBtcResponseMerchantWalletEntity**](BuyBtcResponseMerchantWalletEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pagination4**
> PayResponsePaginationMerchantWalletEntity pagination4(pay_pagination_query_merchant_wallet_query)

分页查询商户钱包

要求管理员权限

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_merchant_wallet_query import PayPaginationQueryMerchantWalletQuery
from buybtcpay.models.pay_response_pagination_merchant_wallet_entity import PayResponsePaginationMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    pay_pagination_query_merchant_wallet_query = buybtcpay.PayPaginationQueryMerchantWalletQuery() # PayPaginationQueryMerchantWalletQuery | 

    try:
        # 分页查询商户钱包
        api_response = api_instance.pagination4(pay_pagination_query_merchant_wallet_query)
        print("The response of OpenWalletApi->pagination4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->pagination4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_merchant_wallet_query** | [**PayPaginationQueryMerchantWalletQuery**](PayPaginationQueryMerchantWalletQuery.md)|  | 

### Return type

[**PayResponsePaginationMerchantWalletEntity**](PayResponsePaginationMerchantWalletEntity.md)

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

# **query_merchant_wallet_info**
> BuyBtcResponseMerchantWalletEntity query_merchant_wallet_info(wallet_id)

查询钱包信息

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_wallet_entity import BuyBtcResponseMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    wallet_id = 56 # int | 

    try:
        # 查询钱包信息
        api_response = api_instance.query_merchant_wallet_info(wallet_id)
        print("The response of OpenWalletApi->query_merchant_wallet_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->query_merchant_wallet_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 

### Return type

[**BuyBtcResponseMerchantWalletEntity**](BuyBtcResponseMerchantWalletEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

