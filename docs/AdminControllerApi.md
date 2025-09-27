# buybtcpay.AdminControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_wallet_permission_to_owner**](AdminControllerApi.md#authorize_wallet_permission_to_owner) | **POST** /v1/admin/merchant/wallet/authorize/owner | 
[**create_platform_wallet**](AdminControllerApi.md#create_platform_wallet) | **GET** /v1/admin/create/platform/wallets | 为平台账户创建各币种的钱包、手续费钱包
[**create_wallet_for_each_merchant**](AdminControllerApi.md#create_wallet_for_each_merchant) | **GET** /v1/admin/create/wallets | 为所有的商户创建各币种的钱包
[**fill_merchant_wallet_vacancy**](AdminControllerApi.md#fill_merchant_wallet_vacancy) | **POST** /v1/admin/merchant/wallet/fill/vacancy | 
[**send_payout_notify**](AdminControllerApi.md#send_payout_notify) | **POST** /v1/admin/send/payout/notify | 


# **authorize_wallet_permission_to_owner**
> BuyBtcResponseInteger authorize_wallet_permission_to_owner()

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_integer import BuyBtcResponseInteger
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
        api_response = api_instance.authorize_wallet_permission_to_owner()
        print("The response of AdminControllerApi->authorize_wallet_permission_to_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminControllerApi->authorize_wallet_permission_to_owner: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseInteger**](BuyBtcResponseInteger.md)

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

# **fill_merchant_wallet_vacancy**
> BuyBtcResponseInteger fill_merchant_wallet_vacancy()

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_integer import BuyBtcResponseInteger
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
        api_response = api_instance.fill_merchant_wallet_vacancy()
        print("The response of AdminControllerApi->fill_merchant_wallet_vacancy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminControllerApi->fill_merchant_wallet_vacancy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseInteger**](BuyBtcResponseInteger.md)

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

# **send_payout_notify**
> BuyBtcResponsePalmPayNotifyResponse send_payout_notify(send_payout_notify_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_palm_pay_notify_response import BuyBtcResponsePalmPayNotifyResponse
from buybtcpay.models.send_payout_notify_dto import SendPayoutNotifyDto
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
    send_payout_notify_dto = buybtcpay.SendPayoutNotifyDto() # SendPayoutNotifyDto | 

    try:
        api_response = api_instance.send_payout_notify(send_payout_notify_dto)
        print("The response of AdminControllerApi->send_payout_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminControllerApi->send_payout_notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_payout_notify_dto** | [**SendPayoutNotifyDto**](SendPayoutNotifyDto.md)|  | 

### Return type

[**BuyBtcResponsePalmPayNotifyResponse**](BuyBtcResponsePalmPayNotifyResponse.md)

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

