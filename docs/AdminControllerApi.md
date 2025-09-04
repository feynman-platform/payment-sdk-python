# buybtcpay.AdminControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform_wallet**](AdminControllerApi.md#create_platform_wallet) | **GET** /v1/admin/create/platform/wallets | 为平台账户创建各币种的钱包、手续费钱包
[**create_wallet_for_each_merchant**](AdminControllerApi.md#create_wallet_for_each_merchant) | **GET** /v1/admin/create/wallets | 为所有的商户创建各币种的钱包


# **create_platform_wallet**
> BuyBtcResponseString create_platform_wallet()

为平台账户创建各币种的钱包、手续费钱包

### Example


```python
import buybtcpay
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
    api_instance = buybtcpay.AdminControllerApi(api_client)

    try:
        # 为平台账户创建各币种的钱包、手续费钱包
        api_response = api_instance.create_platform_wallet()
        print("The response of AdminControllerApi->create_platform_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminControllerApi->create_platform_wallet: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseString**](BuyBtcResponseString.md)

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

# **create_wallet_for_each_merchant**
> BuyBtcResponseString create_wallet_for_each_merchant()

为所有的商户创建各币种的钱包

### Example


```python
import buybtcpay
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
    api_instance = buybtcpay.AdminControllerApi(api_client)

    try:
        # 为所有的商户创建各币种的钱包
        api_response = api_instance.create_wallet_for_each_merchant()
        print("The response of AdminControllerApi->create_wallet_for_each_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminControllerApi->create_wallet_for_each_merchant: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseString**](BuyBtcResponseString.md)

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

