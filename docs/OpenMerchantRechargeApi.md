# buybtcpay.OpenMerchantRechargeApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](OpenMerchantRechargeApi.md#create1) | **POST** /v1/open/merchant/recharge/create | 创建充值审批单


# **create1**
> BuyBtcResponseMerchantRechargeEntity create1(open_merchant_recharge_create_dto)

创建充值审批单

需要管理员审核后，商户余额才会更新

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_recharge_entity import BuyBtcResponseMerchantRechargeEntity
from buybtcpay.models.open_merchant_recharge_create_dto import OpenMerchantRechargeCreateDto
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
    api_instance = buybtcpay.OpenMerchantRechargeApi(api_client)
    open_merchant_recharge_create_dto = buybtcpay.OpenMerchantRechargeCreateDto() # OpenMerchantRechargeCreateDto | 

    try:
        # 创建充值审批单
        api_response = api_instance.create1(open_merchant_recharge_create_dto)
        print("The response of OpenMerchantRechargeApi->create1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenMerchantRechargeApi->create1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_merchant_recharge_create_dto** | [**OpenMerchantRechargeCreateDto**](OpenMerchantRechargeCreateDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantRechargeEntity**](BuyBtcResponseMerchantRechargeEntity.md)

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

