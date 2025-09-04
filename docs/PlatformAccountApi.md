# buybtcpay.PlatformAccountApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform_accounts**](PlatformAccountApi.md#get_platform_accounts) | **GET** /v1/platform/account | 获取平台账户列表


# **get_platform_accounts**
> BuyBtcResponseListPlatformAccountEntity get_platform_accounts()

获取平台账户列表

金额已经被转换为标准货币单位，前端不必再处理

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_platform_account_entity import BuyBtcResponseListPlatformAccountEntity
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
    api_instance = buybtcpay.PlatformAccountApi(api_client)

    try:
        # 获取平台账户列表
        api_response = api_instance.get_platform_accounts()
        print("The response of PlatformAccountApi->get_platform_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformAccountApi->get_platform_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseListPlatformAccountEntity**](BuyBtcResponseListPlatformAccountEntity.md)

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

