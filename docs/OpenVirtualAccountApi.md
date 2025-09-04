# buybtcpay.OpenVirtualAccountApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](OpenVirtualAccountApi.md#create) | **POST** /v1/open/va/create | 创建虚拟账户
[**query_by_pagination**](OpenVirtualAccountApi.md#query_by_pagination) | **POST** /v1/open/va/pagination | 分页查询虚拟账户
[**update**](OpenVirtualAccountApi.md#update) | **POST** /v1/open/va/update | 更新虚拟账户


# **create**
> BuyBtcResponseVirtualAccountEntity create(virtual_account_create_dto)

创建虚拟账户

如果已经创建，会返回错误消息

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_account_entity import BuyBtcResponseVirtualAccountEntity
from buybtcpay.models.virtual_account_create_dto import VirtualAccountCreateDto
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
    api_instance = buybtcpay.OpenVirtualAccountApi(api_client)
    virtual_account_create_dto = buybtcpay.VirtualAccountCreateDto() # VirtualAccountCreateDto | 

    try:
        # 创建虚拟账户
        api_response = api_instance.create(virtual_account_create_dto)
        print("The response of OpenVirtualAccountApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenVirtualAccountApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_account_create_dto** | [**VirtualAccountCreateDto**](VirtualAccountCreateDto.md)|  | 

### Return type

[**BuyBtcResponseVirtualAccountEntity**](BuyBtcResponseVirtualAccountEntity.md)

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

# **query_by_pagination**
> BuyBtcResponsePayPaginationVirtualAccountEntity query_by_pagination(pay_pagination_query_virtual_account_pagination_query)

分页查询虚拟账户

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_virtual_account_entity import BuyBtcResponsePayPaginationVirtualAccountEntity
from buybtcpay.models.pay_pagination_query_virtual_account_pagination_query import PayPaginationQueryVirtualAccountPaginationQuery
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
    api_instance = buybtcpay.OpenVirtualAccountApi(api_client)
    pay_pagination_query_virtual_account_pagination_query = buybtcpay.PayPaginationQueryVirtualAccountPaginationQuery() # PayPaginationQueryVirtualAccountPaginationQuery | 

    try:
        # 分页查询虚拟账户
        api_response = api_instance.query_by_pagination(pay_pagination_query_virtual_account_pagination_query)
        print("The response of OpenVirtualAccountApi->query_by_pagination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenVirtualAccountApi->query_by_pagination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_virtual_account_pagination_query** | [**PayPaginationQueryVirtualAccountPaginationQuery**](PayPaginationQueryVirtualAccountPaginationQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationVirtualAccountEntity**](BuyBtcResponsePayPaginationVirtualAccountEntity.md)

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

# **update**
> BuyBtcResponseVirtualAccountEntity update(virtual_account_update_dto)

更新虚拟账户

目前只以更新虚拟账户的状态，与商户管理中启用、禁用的功能一样

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_account_entity import BuyBtcResponseVirtualAccountEntity
from buybtcpay.models.virtual_account_update_dto import VirtualAccountUpdateDto
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
    api_instance = buybtcpay.OpenVirtualAccountApi(api_client)
    virtual_account_update_dto = buybtcpay.VirtualAccountUpdateDto() # VirtualAccountUpdateDto | 

    try:
        # 更新虚拟账户
        api_response = api_instance.update(virtual_account_update_dto)
        print("The response of OpenVirtualAccountApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenVirtualAccountApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_account_update_dto** | [**VirtualAccountUpdateDto**](VirtualAccountUpdateDto.md)|  | 

### Return type

[**BuyBtcResponseVirtualAccountEntity**](BuyBtcResponseVirtualAccountEntity.md)

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

