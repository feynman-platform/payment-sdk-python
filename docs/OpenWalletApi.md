# buybtcpay.OpenWalletApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_by_currencty**](OpenWalletApi.md#find_by_currencty) | **POST** /v1/open/wallet/{merchantId}/{currency} | 查询商户指定币种钱包
[**find_by_merchant_id**](OpenWalletApi.md#find_by_merchant_id) | **POST** /v1/open/wallet/{merchantId} | 查询商户所有钱包


# **find_by_currencty**
> BuyBtcResponseMerchantWalletEntity find_by_currencty(merchant_id, currency)

查询商户指定币种钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_wallet_entity import BuyBtcResponseMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    merchant_id = 'merchant_id_example' # str | 
    currency = 'currency_example' # str | 

    try:
        # 查询商户指定币种钱包
        api_response = api_instance.find_by_currencty(merchant_id, currency)
        print("The response of OpenWalletApi->find_by_currencty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->find_by_currencty: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 
 **currency** | **str**|  | 

### Return type

[**BuyBtcResponseMerchantWalletEntity**](BuyBtcResponseMerchantWalletEntity.md)

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

# **find_by_merchant_id**
> BuyBtcResponseListMerchantWalletEntity find_by_merchant_id(merchant_id)

查询商户所有钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity
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
    api_instance = buybtcpay.OpenWalletApi(api_client)
    merchant_id = 'merchant_id_example' # str | 

    try:
        # 查询商户所有钱包
        api_response = api_instance.find_by_merchant_id(merchant_id)
        print("The response of OpenWalletApi->find_by_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenWalletApi->find_by_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**|  | 

### Return type

[**BuyBtcResponseListMerchantWalletEntity**](BuyBtcResponseListMerchantWalletEntity.md)

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

