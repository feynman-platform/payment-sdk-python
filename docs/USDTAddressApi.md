# buybtcpay.USDTAddressApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_address**](USDTAddressApi.md#delete_address) | **DELETE** /v1/usdt/address/{id} | 删除地址
[**get_address**](USDTAddressApi.md#get_address) | **GET** /v1/usdt/address | 查询地址列表
[**insert_address**](USDTAddressApi.md#insert_address) | **POST** /v1/usdt/address | 新增地址


# **delete_address**
> BuyBtcResponseBoolean delete_address(id)

删除地址

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_boolean import BuyBtcResponseBoolean
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
    api_instance = buybtcpay.USDTAddressApi(api_client)
    id = 56 # int | 

    try:
        # 删除地址
        api_response = api_instance.delete_address(id)
        print("The response of USDTAddressApi->delete_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USDTAddressApi->delete_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BuyBtcResponseBoolean**](BuyBtcResponseBoolean.md)

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

# **get_address**
> PayResponsePaginationAddressEntity get_address()

查询地址列表

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_pagination_address_entity import PayResponsePaginationAddressEntity
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
    api_instance = buybtcpay.USDTAddressApi(api_client)

    try:
        # 查询地址列表
        api_response = api_instance.get_address()
        print("The response of USDTAddressApi->get_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USDTAddressApi->get_address: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayResponsePaginationAddressEntity**](PayResponsePaginationAddressEntity.md)

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

# **insert_address**
> BuyBtcResponseString insert_address(address_form)

新增地址

### Example


```python
import buybtcpay
from buybtcpay.models.address_form import AddressForm
from buybtcpay.models.buy_btc_response_string import BuyBtcResponseString
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
    api_instance = buybtcpay.USDTAddressApi(api_client)
    address_form = buybtcpay.AddressForm() # AddressForm | 

    try:
        # 新增地址
        api_response = api_instance.insert_address(address_form)
        print("The response of USDTAddressApi->insert_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling USDTAddressApi->insert_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_form** | [**AddressForm**](AddressForm.md)|  | 

### Return type

[**BuyBtcResponseString**](BuyBtcResponseString.md)

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

