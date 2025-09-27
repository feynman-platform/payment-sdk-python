# buybtcpay.TronApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_approval_record**](TronApi.md#close_approval_record) | **POST** /v1/tron/close/approval/record | 关闭充值审批
[**get_address_and_amount**](TronApi.md#get_address_and_amount) | **POST** /v1/tron/amount | 获取交易地址和交易金额
[**get_transaction_usdtby_id**](TronApi.md#get_transaction_usdtby_id) | **GET** /v1/tron/usdt/{txId} | 根据交易id查询USDT详情
[**save_approval_record**](TronApi.md#save_approval_record) | **POST** /v1/tron/save/approval/record | 保存充值审批记录
[**send_trx**](TronApi.md#send_trx) | **POST** /v1/tron/trx/send | 发送TRX
[**send_usdt**](TronApi.md#send_usdt) | **POST** /v1/tron/usdt/send | 发送USDT


# **close_approval_record**
> str close_approval_record(address_allocation_dto)

关闭充值审批

### Example


```python
import buybtcpay
from buybtcpay.models.address_allocation_dto import AddressAllocationDto
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
    api_instance = buybtcpay.TronApi(api_client)
    address_allocation_dto = buybtcpay.AddressAllocationDto() # AddressAllocationDto | 

    try:
        # 关闭充值审批
        api_response = api_instance.close_approval_record(address_allocation_dto)
        print("The response of TronApi->close_approval_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TronApi->close_approval_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_allocation_dto** | [**AddressAllocationDto**](AddressAllocationDto.md)|  | 

### Return type

**str**

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

# **get_address_and_amount**
> AddressAllocationVo get_address_and_amount(allocation_form)

获取交易地址和交易金额

### Example


```python
import buybtcpay
from buybtcpay.models.address_allocation_vo import AddressAllocationVo
from buybtcpay.models.allocation_form import AllocationForm
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
    api_instance = buybtcpay.TronApi(api_client)
    allocation_form = buybtcpay.AllocationForm() # AllocationForm | 

    try:
        # 获取交易地址和交易金额
        api_response = api_instance.get_address_and_amount(allocation_form)
        print("The response of TronApi->get_address_and_amount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TronApi->get_address_and_amount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_form** | [**AllocationForm**](AllocationForm.md)|  | 

### Return type

[**AddressAllocationVo**](AddressAllocationVo.md)

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

# **get_transaction_usdtby_id**
> get_transaction_usdtby_id(tx_id)

根据交易id查询USDT详情

### Example


```python
import buybtcpay
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
    api_instance = buybtcpay.TronApi(api_client)
    tx_id = 'tx_id_example' # str | 

    try:
        # 根据交易id查询USDT详情
        api_instance.get_transaction_usdtby_id(tx_id)
    except Exception as e:
        print("Exception when calling TronApi->get_transaction_usdtby_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_approval_record**
> AddressAllocationVo save_approval_record(address_allocation_dto)

保存充值审批记录

### Example


```python
import buybtcpay
from buybtcpay.models.address_allocation_dto import AddressAllocationDto
from buybtcpay.models.address_allocation_vo import AddressAllocationVo
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
    api_instance = buybtcpay.TronApi(api_client)
    address_allocation_dto = buybtcpay.AddressAllocationDto() # AddressAllocationDto | 

    try:
        # 保存充值审批记录
        api_response = api_instance.save_approval_record(address_allocation_dto)
        print("The response of TronApi->save_approval_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TronApi->save_approval_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_allocation_dto** | [**AddressAllocationDto**](AddressAllocationDto.md)|  | 

### Return type

[**AddressAllocationVo**](AddressAllocationVo.md)

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

# **send_trx**
> SendResponse send_trx(var_from, send_request)

发送TRX

### Example


```python
import buybtcpay
from buybtcpay.models.send_request import SendRequest
from buybtcpay.models.send_response import SendResponse
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
    api_instance = buybtcpay.TronApi(api_client)
    var_from = 'var_from_example' # str | 
    send_request = buybtcpay.SendRequest() # SendRequest | 

    try:
        # 发送TRX
        api_response = api_instance.send_trx(var_from, send_request)
        print("The response of TronApi->send_trx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TronApi->send_trx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**|  | 
 **send_request** | [**SendRequest**](SendRequest.md)|  | 

### Return type

[**SendResponse**](SendResponse.md)

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

# **send_usdt**
> SendResponse send_usdt(var_from, send_request)

发送USDT

### Example


```python
import buybtcpay
from buybtcpay.models.send_request import SendRequest
from buybtcpay.models.send_response import SendResponse
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
    api_instance = buybtcpay.TronApi(api_client)
    var_from = 'var_from_example' # str | 
    send_request = buybtcpay.SendRequest() # SendRequest | 

    try:
        # 发送USDT
        api_response = api_instance.send_usdt(var_from, send_request)
        print("The response of TronApi->send_usdt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TronApi->send_usdt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **str**|  | 
 **send_request** | [**SendRequest**](SendRequest.md)|  | 

### Return type

[**SendResponse**](SendResponse.md)

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

