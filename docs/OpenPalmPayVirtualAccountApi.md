# buybtcpay.OpenPalmPayVirtualAccountApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_top_up_notify**](OpenPalmPayVirtualAccountApi.md#send_top_up_notify) | **POST** /v1/open/palmpay/virtual/account/dev/topup/notify | 发送充值通知


# **send_top_up_notify**
> BuyBtcResponseVirtualAccountTopUpNotifyResponse send_top_up_notify(send_top_up_notify_dto)

发送充值通知

生产环境不可用

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_virtual_account_top_up_notify_response import BuyBtcResponseVirtualAccountTopUpNotifyResponse
from buybtcpay.models.send_top_up_notify_dto import SendTopUpNotifyDto
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
    api_instance = buybtcpay.OpenPalmPayVirtualAccountApi(api_client)
    send_top_up_notify_dto = buybtcpay.SendTopUpNotifyDto() # SendTopUpNotifyDto | 

    try:
        # 发送充值通知
        api_response = api_instance.send_top_up_notify(send_top_up_notify_dto)
        print("The response of OpenPalmPayVirtualAccountApi->send_top_up_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPalmPayVirtualAccountApi->send_top_up_notify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_top_up_notify_dto** | [**SendTopUpNotifyDto**](SendTopUpNotifyDto.md)|  | 

### Return type

[**BuyBtcResponseVirtualAccountTopUpNotifyResponse**](BuyBtcResponseVirtualAccountTopUpNotifyResponse.md)

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

