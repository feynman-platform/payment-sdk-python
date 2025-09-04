# buybtcpay.PalmPayControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](PalmPayControllerApi.md#balance) | **GET** /v1/palmpay/balance | 
[**bank**](PalmPayControllerApi.md#bank) | **GET** /v1/palmpay/bank | 
[**get_latest_bank**](PalmPayControllerApi.md#get_latest_bank) | **GET** /v1/palmpay/bank/latest | 


# **balance**
> PayResponseQueryBalanceResponse balance()

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_query_balance_response import PayResponseQueryBalanceResponse
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
    api_instance = buybtcpay.PalmPayControllerApi(api_client)

    try:
        api_response = api_instance.balance()
        print("The response of PalmPayControllerApi->balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayControllerApi->balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayResponseQueryBalanceResponse**](PayResponseQueryBalanceResponse.md)

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

# **bank**
> PayResponseListPalmPayBank bank()

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_list_palm_pay_bank import PayResponseListPalmPayBank
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
    api_instance = buybtcpay.PalmPayControllerApi(api_client)

    try:
        api_response = api_instance.bank()
        print("The response of PalmPayControllerApi->bank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayControllerApi->bank: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayResponseListPalmPayBank**](PayResponseListPalmPayBank.md)

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

# **get_latest_bank**
> PayResponseListPalmPayBank get_latest_bank()

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_list_palm_pay_bank import PayResponseListPalmPayBank
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
    api_instance = buybtcpay.PalmPayControllerApi(api_client)

    try:
        api_response = api_instance.get_latest_bank()
        print("The response of PalmPayControllerApi->get_latest_bank:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PalmPayControllerApi->get_latest_bank: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayResponseListPalmPayBank**](PayResponseListPalmPayBank.md)

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

