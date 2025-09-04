# buybtcpay.PalmPayVirtualAccountApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_account**](PalmPayVirtualAccountApi.md#create_virtual_account) | **POST** /v1/palmpay/virtual/account/bind/{merchantId} | 商户绑定虚拟账号
[**disable_virtual_account**](PalmPayVirtualAccountApi.md#disable_virtual_account) | **POST** /v1/palmpay/virtual/account/disable/{merchantId} | 禁用虚拟账号
[**enable_virtual_account**](PalmPayVirtualAccountApi.md#enable_virtual_account) | **POST** /v1/palmpay/virtual/account/enable/{merchantId} | 启用虚拟账号
[**query_virtual_account**](PalmPayVirtualAccountApi.md#query_virtual_account) | **GET** /v1/palmpay/virtual/account/{accountNo} | 查询虚拟账号
[**query_virtual_order_detail**](PalmPayVirtualAccountApi.md#query_virtual_order_detail) | **GET** /v1/palmpay/virtual/account/order/{orderNo} | 查询虚拟账号单详情
[**virtual_account_pagination**](PalmPayVirtualAccountApi.md#virtual_account_pagination) | **POST** /v1/palmpay/virtual/account/pagination | 查询虚拟账号列表
[**virtual_order_pagination**](PalmPayVirtualAccountApi.md#virtual_order_pagination) | **POST** /v1/palmpay/virtual/account/order/pagination | 查询虚拟账号交易列表
[**virtual_order_recharge_pagination**](PalmPayVirtualAccountApi.md#virtual_order_recharge_pagination) | **POST** /v1/palmpay/virtual/account/order/recharge/pagination | 查询虚拟账号充值订单列表


# **create_virtual_account**
> BuyBtcResponseMerchantEntity create_virtual_account(merchant_id)

商户绑定虚拟账号

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity import BuyBtcResponseMerchantEntity
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 商户绑定虚拟账号
        api_response = api_instance.create_virtual_account(merchant_id)
        print("The response of PalmPayVirtualAccountApi->create_virtual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->create_virtual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseMerchantEntity**](BuyBtcResponseMerchantEntity.md)

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

# **disable_virtual_account**
> BuyBtcResponseVirtualAccountLabelUpdateResponse disable_virtual_account(merchant_id)

禁用虚拟账号

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_account_label_update_response import BuyBtcResponseVirtualAccountLabelUpdateResponse
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 禁用虚拟账号
        api_response = api_instance.disable_virtual_account(merchant_id)
        print("The response of PalmPayVirtualAccountApi->disable_virtual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->disable_virtual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseVirtualAccountLabelUpdateResponse**](BuyBtcResponseVirtualAccountLabelUpdateResponse.md)

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

# **enable_virtual_account**
> BuyBtcResponseVirtualAccountLabelUpdateResponse enable_virtual_account(merchant_id)

启用虚拟账号

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_account_label_update_response import BuyBtcResponseVirtualAccountLabelUpdateResponse
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 启用虚拟账号
        api_response = api_instance.enable_virtual_account(merchant_id)
        print("The response of PalmPayVirtualAccountApi->enable_virtual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->enable_virtual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseVirtualAccountLabelUpdateResponse**](BuyBtcResponseVirtualAccountLabelUpdateResponse.md)

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

# **query_virtual_account**
> BuyBtcResponseVirtualAccountData query_virtual_account(account_no)

查询虚拟账号

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_account_data import BuyBtcResponseVirtualAccountData
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    account_no = 'account_no_example' # str | 

    try:
        # 查询虚拟账号
        api_response = api_instance.query_virtual_account(account_no)
        print("The response of PalmPayVirtualAccountApi->query_virtual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->query_virtual_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_no** | **str**|  | 

### Return type

[**BuyBtcResponseVirtualAccountData**](BuyBtcResponseVirtualAccountData.md)

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

# **query_virtual_order_detail**
> BuyBtcResponseVirtualOrderDetail query_virtual_order_detail(order_no)

查询虚拟账号单详情

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_order_detail import BuyBtcResponseVirtualOrderDetail
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    order_no = 'order_no_example' # str | 

    try:
        # 查询虚拟账号单详情
        api_response = api_instance.query_virtual_order_detail(order_no)
        print("The response of PalmPayVirtualAccountApi->query_virtual_order_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->query_virtual_order_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_no** | **str**|  | 

### Return type

[**BuyBtcResponseVirtualOrderDetail**](BuyBtcResponseVirtualOrderDetail.md)

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

# **virtual_account_pagination**
> PayResponsePaginationPalmPayVirtualAccountEntity virtual_account_pagination(pay_pagination_query_palm_pay_virtual_account_query)

查询虚拟账号列表

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_palm_pay_virtual_account_query import PayPaginationQueryPalmPayVirtualAccountQuery
from buybtcpay.models.pay_response_pagination_palm_pay_virtual_account_entity import PayResponsePaginationPalmPayVirtualAccountEntity
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    pay_pagination_query_palm_pay_virtual_account_query = buybtcpay.PayPaginationQueryPalmPayVirtualAccountQuery() # PayPaginationQueryPalmPayVirtualAccountQuery | 

    try:
        # 查询虚拟账号列表
        api_response = api_instance.virtual_account_pagination(pay_pagination_query_palm_pay_virtual_account_query)
        print("The response of PalmPayVirtualAccountApi->virtual_account_pagination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->virtual_account_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_palm_pay_virtual_account_query** | [**PayPaginationQueryPalmPayVirtualAccountQuery**](PayPaginationQueryPalmPayVirtualAccountQuery.md)|  | 

### Return type

[**PayResponsePaginationPalmPayVirtualAccountEntity**](PayResponsePaginationPalmPayVirtualAccountEntity.md)

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

# **virtual_order_pagination**
> PayResponsePaginationPalmPayVirtualAccountOrderEntity virtual_order_pagination(pay_pagination_query_palm_pay_virtual_account_order_query)

查询虚拟账号交易列表

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_palm_pay_virtual_account_order_query import PayPaginationQueryPalmPayVirtualAccountOrderQuery
from buybtcpay.models.pay_response_pagination_palm_pay_virtual_account_order_entity import PayResponsePaginationPalmPayVirtualAccountOrderEntity
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    pay_pagination_query_palm_pay_virtual_account_order_query = buybtcpay.PayPaginationQueryPalmPayVirtualAccountOrderQuery() # PayPaginationQueryPalmPayVirtualAccountOrderQuery | 

    try:
        # 查询虚拟账号交易列表
        api_response = api_instance.virtual_order_pagination(pay_pagination_query_palm_pay_virtual_account_order_query)
        print("The response of PalmPayVirtualAccountApi->virtual_order_pagination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->virtual_order_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_palm_pay_virtual_account_order_query** | [**PayPaginationQueryPalmPayVirtualAccountOrderQuery**](PayPaginationQueryPalmPayVirtualAccountOrderQuery.md)|  | 

### Return type

[**PayResponsePaginationPalmPayVirtualAccountOrderEntity**](PayResponsePaginationPalmPayVirtualAccountOrderEntity.md)

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

# **virtual_order_recharge_pagination**
> PayResponsePaginationPalmPayVirtualAccountOrderRechargeEntity virtual_order_recharge_pagination(pay_pagination_query_palm_pay_virtual_account_order_recharge_query)

查询虚拟账号充值订单列表

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_palm_pay_virtual_account_order_recharge_query import PayPaginationQueryPalmPayVirtualAccountOrderRechargeQuery
from buybtcpay.models.pay_response_pagination_palm_pay_virtual_account_order_recharge_entity import PayResponsePaginationPalmPayVirtualAccountOrderRechargeEntity
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
    api_instance = buybtcpay.PalmPayVirtualAccountApi(api_client)
    pay_pagination_query_palm_pay_virtual_account_order_recharge_query = buybtcpay.PayPaginationQueryPalmPayVirtualAccountOrderRechargeQuery() # PayPaginationQueryPalmPayVirtualAccountOrderRechargeQuery | 

    try:
        # 查询虚拟账号充值订单列表
        api_response = api_instance.virtual_order_recharge_pagination(pay_pagination_query_palm_pay_virtual_account_order_recharge_query)
        print("The response of PalmPayVirtualAccountApi->virtual_order_recharge_pagination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayVirtualAccountApi->virtual_order_recharge_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_palm_pay_virtual_account_order_recharge_query** | [**PayPaginationQueryPalmPayVirtualAccountOrderRechargeQuery**](PayPaginationQueryPalmPayVirtualAccountOrderRechargeQuery.md)|  | 

### Return type

[**PayResponsePaginationPalmPayVirtualAccountOrderRechargeEntity**](PayResponsePaginationPalmPayVirtualAccountOrderRechargeEntity.md)

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

