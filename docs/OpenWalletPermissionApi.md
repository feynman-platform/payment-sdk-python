# buybtcpay.OpenWalletPermissionApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_trade_account_permissions**](OpenWalletPermissionApi.md#authorize_trade_account_permissions) | **POST** /v1/open/wallet/permission/authorize/trade/account/permissions | 将指定商户的交易账户授权给其他商户，授予的权限为交易账户的基础权限
[**authorize_wallet_permissions**](OpenWalletPermissionApi.md#authorize_wallet_permissions) | **POST** /v1/open/wallet/permission/authorize | 将指定钱包的权限授权给指定商户，以覆盖的方式更新
[**delete_merchant_permissions**](OpenWalletPermissionApi.md#delete_merchant_permissions) | **POST** /v1/open/wallet/permission/unauthorize | 删除商户在钱包的权限
[**find_all_by_wallet_id**](OpenWalletPermissionApi.md#find_all_by_wallet_id) | **GET** /v1/open/wallet/permission/{walletId} | 查询自己在指定钱包的权限列表
[**find_all_by_wallet_id_and_merchant_id**](OpenWalletPermissionApi.md#find_all_by_wallet_id_and_merchant_id) | **GET** /v1/open/wallet/permission/{walletId}/merchant/{merchantId} | 查询指定商户在指定钱包的权限列表
[**find_by_wallet_id_and_permission_and_merchant_id**](OpenWalletPermissionApi.md#find_by_wallet_id_and_permission_and_merchant_id) | **GET** /v1/open/wallet/permission/{walletId}/{permission} | 查询自己在指定钱包、指定权限是否存在
[**query_merchant_authorized_wallets**](OpenWalletPermissionApi.md#query_merchant_authorized_wallets) | **POST** /v1/open/wallet/permission/merchant/authorized | 查询商户已授权的钱包列表
[**query_merchant_authorized_wallets_with_permissions**](OpenWalletPermissionApi.md#query_merchant_authorized_wallets_with_permissions) | **POST** /v1/open/wallet/permission/merchant/authorized/with/permissions | 查询商户已授权的钱包列表，附带权限列表
[**query_wallet_authorized_merchants**](OpenWalletPermissionApi.md#query_wallet_authorized_merchants) | **GET** /v1/open/wallet/permission/{walletId}/merchants | 查询钱包下面挂了多少个商户
[**wallet_permission_pagination**](OpenWalletPermissionApi.md#wallet_permission_pagination) | **POST** /v1/open/wallet/permission/pagination | 分页查询钱包的权限列表


# **authorize_trade_account_permissions**
> BuyBtcResponseListWalletPermissionEntity authorize_trade_account_permissions(authorize_trade_account_permission_dto)

将指定商户的交易账户授权给其他商户，授予的权限为交易账户的基础权限

除管理员外，只能授权属于自己的交易账户

### Example


```python
import buybtcpay
from buybtcpay.models.authorize_trade_account_permission_dto import AuthorizeTradeAccountPermissionDto
from buybtcpay.models.buy_btc_response_list_wallet_permission_entity import BuyBtcResponseListWalletPermissionEntity
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    authorize_trade_account_permission_dto = buybtcpay.AuthorizeTradeAccountPermissionDto() # AuthorizeTradeAccountPermissionDto | 

    try:
        # 将指定商户的交易账户授权给其他商户，授予的权限为交易账户的基础权限
        api_response = api_instance.authorize_trade_account_permissions(authorize_trade_account_permission_dto)
        print("The response of OpenWalletPermissionApi->authorize_trade_account_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->authorize_trade_account_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_trade_account_permission_dto** | [**AuthorizeTradeAccountPermissionDto**](AuthorizeTradeAccountPermissionDto.md)|  | 

### Return type

[**BuyBtcResponseListWalletPermissionEntity**](BuyBtcResponseListWalletPermissionEntity.md)

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

# **authorize_wallet_permissions**
> BuyBtcResponseListWalletPermissionEntity authorize_wallet_permissions(wallet_authorization_param)

将指定钱包的权限授权给指定商户，以覆盖的方式更新

如果是管理员，可以授权任意钱包的任意权限；如果是商户，只能授权自己的钱包的权限

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_wallet_permission_entity import BuyBtcResponseListWalletPermissionEntity
from buybtcpay.models.wallet_authorization_param import WalletAuthorizationParam
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    wallet_authorization_param = buybtcpay.WalletAuthorizationParam() # WalletAuthorizationParam | 

    try:
        # 将指定钱包的权限授权给指定商户，以覆盖的方式更新
        api_response = api_instance.authorize_wallet_permissions(wallet_authorization_param)
        print("The response of OpenWalletPermissionApi->authorize_wallet_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->authorize_wallet_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_authorization_param** | [**WalletAuthorizationParam**](WalletAuthorizationParam.md)|  | 

### Return type

[**BuyBtcResponseListWalletPermissionEntity**](BuyBtcResponseListWalletPermissionEntity.md)

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

# **delete_merchant_permissions**
> BuyBtcResponseBoolean delete_merchant_permissions(wallet_permission_delete_record_dto)

删除商户在钱包的权限

商户可以删除自己在指定钱包的权限，钱包所有者可以删除任意商户在该钱包的权限，管理员无限制

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_boolean import BuyBtcResponseBoolean
from buybtcpay.models.wallet_permission_delete_record_dto import WalletPermissionDeleteRecordDto
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    wallet_permission_delete_record_dto = buybtcpay.WalletPermissionDeleteRecordDto() # WalletPermissionDeleteRecordDto | 

    try:
        # 删除商户在钱包的权限
        api_response = api_instance.delete_merchant_permissions(wallet_permission_delete_record_dto)
        print("The response of OpenWalletPermissionApi->delete_merchant_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->delete_merchant_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_permission_delete_record_dto** | [**WalletPermissionDeleteRecordDto**](WalletPermissionDeleteRecordDto.md)|  | 

### Return type

[**BuyBtcResponseBoolean**](BuyBtcResponseBoolean.md)

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

# **find_all_by_wallet_id**
> BuyBtcResponseListWalletPermissionEntity find_all_by_wallet_id(wallet_id)

查询自己在指定钱包的权限列表

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_wallet_permission_entity import BuyBtcResponseListWalletPermissionEntity
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    wallet_id = 56 # int | 

    try:
        # 查询自己在指定钱包的权限列表
        api_response = api_instance.find_all_by_wallet_id(wallet_id)
        print("The response of OpenWalletPermissionApi->find_all_by_wallet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->find_all_by_wallet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 

### Return type

[**BuyBtcResponseListWalletPermissionEntity**](BuyBtcResponseListWalletPermissionEntity.md)

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

# **find_all_by_wallet_id_and_merchant_id**
> BuyBtcResponseListWalletPermissionEntity find_all_by_wallet_id_and_merchant_id(wallet_id, merchant_id)

查询指定商户在指定钱包的权限列表

需要管理员权限

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_wallet_permission_entity import BuyBtcResponseListWalletPermissionEntity
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    wallet_id = 56 # int | 
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 查询指定商户在指定钱包的权限列表
        api_response = api_instance.find_all_by_wallet_id_and_merchant_id(wallet_id, merchant_id)
        print("The response of OpenWalletPermissionApi->find_all_by_wallet_id_and_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->find_all_by_wallet_id_and_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseListWalletPermissionEntity**](BuyBtcResponseListWalletPermissionEntity.md)

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

# **find_by_wallet_id_and_permission_and_merchant_id**
> BuyBtcResponseWalletPermissionEntity find_by_wallet_id_and_permission_and_merchant_id(wallet_id, permission)

查询自己在指定钱包、指定权限是否存在

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_wallet_permission_entity import BuyBtcResponseWalletPermissionEntity
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    wallet_id = 56 # int | 
    permission = 56 # int | 

    try:
        # 查询自己在指定钱包、指定权限是否存在
        api_response = api_instance.find_by_wallet_id_and_permission_and_merchant_id(wallet_id, permission)
        print("The response of OpenWalletPermissionApi->find_by_wallet_id_and_permission_and_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->find_by_wallet_id_and_permission_and_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 
 **permission** | **int**|  | 

### Return type

[**BuyBtcResponseWalletPermissionEntity**](BuyBtcResponseWalletPermissionEntity.md)

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

# **query_merchant_authorized_wallets**
> BuyBtcResponseListMerchantWalletEntity query_merchant_authorized_wallets(query_merchant_authorized_wallets_dto)

查询商户已授权的钱包列表

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity
from buybtcpay.models.query_merchant_authorized_wallets_dto import QueryMerchantAuthorizedWalletsDto
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    query_merchant_authorized_wallets_dto = buybtcpay.QueryMerchantAuthorizedWalletsDto() # QueryMerchantAuthorizedWalletsDto | 

    try:
        # 查询商户已授权的钱包列表
        api_response = api_instance.query_merchant_authorized_wallets(query_merchant_authorized_wallets_dto)
        print("The response of OpenWalletPermissionApi->query_merchant_authorized_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->query_merchant_authorized_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_merchant_authorized_wallets_dto** | [**QueryMerchantAuthorizedWalletsDto**](QueryMerchantAuthorizedWalletsDto.md)|  | 

### Return type

[**BuyBtcResponseListMerchantWalletEntity**](BuyBtcResponseListMerchantWalletEntity.md)

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

# **query_merchant_authorized_wallets_with_permissions**
> BuyBtcResponseListMerchantWalletsWithPermissionsDto query_merchant_authorized_wallets_with_permissions(query_merchant_authorized_wallets_dto)

查询商户已授权的钱包列表，附带权限列表

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallets_with_permissions_dto import BuyBtcResponseListMerchantWalletsWithPermissionsDto
from buybtcpay.models.query_merchant_authorized_wallets_dto import QueryMerchantAuthorizedWalletsDto
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    query_merchant_authorized_wallets_dto = buybtcpay.QueryMerchantAuthorizedWalletsDto() # QueryMerchantAuthorizedWalletsDto | 

    try:
        # 查询商户已授权的钱包列表，附带权限列表
        api_response = api_instance.query_merchant_authorized_wallets_with_permissions(query_merchant_authorized_wallets_dto)
        print("The response of OpenWalletPermissionApi->query_merchant_authorized_wallets_with_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->query_merchant_authorized_wallets_with_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_merchant_authorized_wallets_dto** | [**QueryMerchantAuthorizedWalletsDto**](QueryMerchantAuthorizedWalletsDto.md)|  | 

### Return type

[**BuyBtcResponseListMerchantWalletsWithPermissionsDto**](BuyBtcResponseListMerchantWalletsWithPermissionsDto.md)

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

# **query_wallet_authorized_merchants**
> BuyBtcResponseListMerchantEntity query_wallet_authorized_merchants(wallet_id)

查询钱包下面挂了多少个商户

除管理员外，只能查自己的钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_entity import BuyBtcResponseListMerchantEntity
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    wallet_id = 56 # int | 

    try:
        # 查询钱包下面挂了多少个商户
        api_response = api_instance.query_wallet_authorized_merchants(wallet_id)
        print("The response of OpenWalletPermissionApi->query_wallet_authorized_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->query_wallet_authorized_merchants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 

### Return type

[**BuyBtcResponseListMerchantEntity**](BuyBtcResponseListMerchantEntity.md)

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

# **wallet_permission_pagination**
> BuyBtcResponsePayPaginationWalletPermissionEntity wallet_permission_pagination(pay_pagination_query_wallet_permission_query)

分页查询钱包的权限列表

管理员可以查看所有钱包的权限列表；商户只能查看自己的钱包的权限列表

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_wallet_permission_entity import BuyBtcResponsePayPaginationWalletPermissionEntity
from buybtcpay.models.pay_pagination_query_wallet_permission_query import PayPaginationQueryWalletPermissionQuery
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
    api_instance = buybtcpay.OpenWalletPermissionApi(api_client)
    pay_pagination_query_wallet_permission_query = buybtcpay.PayPaginationQueryWalletPermissionQuery() # PayPaginationQueryWalletPermissionQuery | 

    try:
        # 分页查询钱包的权限列表
        api_response = api_instance.wallet_permission_pagination(pay_pagination_query_wallet_permission_query)
        print("The response of OpenWalletPermissionApi->wallet_permission_pagination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletPermissionApi->wallet_permission_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_wallet_permission_query** | [**PayPaginationQueryWalletPermissionQuery**](PayPaginationQueryWalletPermissionQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationWalletPermissionEntity**](BuyBtcResponsePayPaginationWalletPermissionEntity.md)

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

