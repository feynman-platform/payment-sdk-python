# buybtcpay.OpenMerchantApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active**](OpenMerchantApi.md#active) | **POST** /v1/open/merchant/active/{merchantId} | 激活商户
[**create_merchant**](OpenMerchantApi.md#create_merchant) | **POST** /v1/open/merchant | 创建商户
[**disable**](OpenMerchantApi.md#disable) | **POST** /v1/open/merchant/disable/{merchantId} | 禁用商户
[**get_merchant_by_merchant_id**](OpenMerchantApi.md#get_merchant_by_merchant_id) | **POST** /v1/open/merchant/{merchantId} | 查看商户信息
[**query_merchant_info_by_merchant_id**](OpenMerchantApi.md#query_merchant_info_by_merchant_id) | **POST** /v1/open/merchant/info/{merchantId} | 查看商户信息
[**set_merchant_tag**](OpenMerchantApi.md#set_merchant_tag) | **POST** /v1/open/merchant/tag | 设置商户标签
[**update_profile**](OpenMerchantApi.md#update_profile) | **PATCH** /v1/open/merchant/{merchantId} | 更新商户信息


# **active**
> BuyBtcResponseMerchantEntity active(merchant_id)

激活商户

如果商户未激活，无法进行代付操作

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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 激活商户
        api_response = api_instance.active(merchant_id)
        print("The response of OpenMerchantApi->active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->active: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_merchant**
> BuyBtcResponseMerchantEntity create_merchant(create_merchant_open_dto)

创建商户

创建商户开放接口

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity import BuyBtcResponseMerchantEntity
from buybtcpay.models.create_merchant_open_dto import CreateMerchantOpenDto
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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    create_merchant_open_dto = buybtcpay.CreateMerchantOpenDto() # CreateMerchantOpenDto | 

    try:
        # 创建商户
        api_response = api_instance.create_merchant(create_merchant_open_dto)
        print("The response of OpenMerchantApi->create_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->create_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_merchant_open_dto** | [**CreateMerchantOpenDto**](CreateMerchantOpenDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantEntity**](BuyBtcResponseMerchantEntity.md)

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

# **disable**
> BuyBtcResponseMerchantEntity disable(merchant_id)

禁用商户

如果商户被禁用，无法进行代付操作

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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 禁用商户
        api_response = api_instance.disable(merchant_id)
        print("The response of OpenMerchantApi->disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->disable: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_by_merchant_id**
> BuyBtcResponseMerchantEntityDto get_merchant_by_merchant_id(merchant_id)

查看商户信息

商户可以查询自己的信息，也可查询所属的虚拟账户信息

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity_dto import BuyBtcResponseMerchantEntityDto
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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 查看商户信息
        api_response = api_instance.get_merchant_by_merchant_id(merchant_id)
        print("The response of OpenMerchantApi->get_merchant_by_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->get_merchant_by_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseMerchantEntityDto**](BuyBtcResponseMerchantEntityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_merchant_info_by_merchant_id**
> BuyBtcResponseMerchantEntityDto query_merchant_info_by_merchant_id(merchant_id)

查看商户信息

商户可以查询自己的信息，也可查询所属的虚拟账户信息

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity_dto import BuyBtcResponseMerchantEntityDto
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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 查看商户信息
        api_response = api_instance.query_merchant_info_by_merchant_id(merchant_id)
        print("The response of OpenMerchantApi->query_merchant_info_by_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->query_merchant_info_by_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseMerchantEntityDto**](BuyBtcResponseMerchantEntityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_merchant_tag**
> BuyBtcResponseMerchantEntity set_merchant_tag(set_merchant_tag_dto)

设置商户标签

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity import BuyBtcResponseMerchantEntity
from buybtcpay.models.set_merchant_tag_dto import SetMerchantTagDto
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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    set_merchant_tag_dto = buybtcpay.SetMerchantTagDto() # SetMerchantTagDto | 

    try:
        # 设置商户标签
        api_response = api_instance.set_merchant_tag(set_merchant_tag_dto)
        print("The response of OpenMerchantApi->set_merchant_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->set_merchant_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_merchant_tag_dto** | [**SetMerchantTagDto**](SetMerchantTagDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantEntity**](BuyBtcResponseMerchantEntity.md)

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

# **update_profile**
> BuyBtcResponseMerchantEntity update_profile(merchant_id, merchant_update_profile_dto)

更新商户信息

更新商户信息，需要传入商户ID

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity import BuyBtcResponseMerchantEntity
from buybtcpay.models.merchant_update_profile_dto import MerchantUpdateProfileDto
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
    api_instance = buybtcpay.OpenMerchantApi(api_client)
    merchant_id = 'merchant_id_example' # str | 
    merchant_update_profile_dto = buybtcpay.MerchantUpdateProfileDto() # MerchantUpdateProfileDto | 

    try:
        # 更新商户信息
        api_response = api_instance.update_profile(merchant_id, merchant_update_profile_dto)
        print("The response of OpenMerchantApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **merchant_update_profile_dto** | [**MerchantUpdateProfileDto**](MerchantUpdateProfileDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantEntity**](BuyBtcResponseMerchantEntity.md)

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

