# buybtcpay.OpenStatisticsApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_merchant_money_usage**](OpenStatisticsApi.md#count_merchant_money_usage) | **POST** /v1/open/statistics/merchant/money/usage | 商户币种消耗情况
[**count_merchant_payout_by_time_between**](OpenStatisticsApi.md#count_merchant_payout_by_time_between) | **POST** /v1/open/statistics/merchant/payout | 统计商户代付金额
[**count_payout**](OpenStatisticsApi.md#count_payout) | **POST** /v1/open/statistics/merchant/payout/times | 统计商户代付笔数
[**merchant_money_state**](OpenStatisticsApi.md#merchant_money_state) | **POST** /v1/open/statistics/merchant/money/state | 商户汇总数据


# **count_merchant_money_usage**
> BuyBtcResponseListMerchantMoneyUsageStateVo count_merchant_money_usage(merchant_money_usage_statistics_req)

商户币种消耗情况

统计商户币种消耗情况

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_money_usage_state_vo import BuyBtcResponseListMerchantMoneyUsageStateVo
from buybtcpay.models.merchant_money_usage_statistics_req import MerchantMoneyUsageStatisticsReq
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
    api_instance = buybtcpay.OpenStatisticsApi(api_client)
    merchant_money_usage_statistics_req = buybtcpay.MerchantMoneyUsageStatisticsReq() # MerchantMoneyUsageStatisticsReq | 

    try:
        # 商户币种消耗情况
        api_response = api_instance.count_merchant_money_usage(merchant_money_usage_statistics_req)
        print("The response of OpenStatisticsApi->count_merchant_money_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenStatisticsApi->count_merchant_money_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_money_usage_statistics_req** | [**MerchantMoneyUsageStatisticsReq**](MerchantMoneyUsageStatisticsReq.md)|  | 

### Return type

[**BuyBtcResponseListMerchantMoneyUsageStateVo**](BuyBtcResponseListMerchantMoneyUsageStateVo.md)

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

# **count_merchant_payout_by_time_between**
> BuyBtcResponseListMerchantMoneyUsageStateVo count_merchant_payout_by_time_between(merchant_money_usage_statistics_req)

统计商户代付金额

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_money_usage_state_vo import BuyBtcResponseListMerchantMoneyUsageStateVo
from buybtcpay.models.merchant_money_usage_statistics_req import MerchantMoneyUsageStatisticsReq
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
    api_instance = buybtcpay.OpenStatisticsApi(api_client)
    merchant_money_usage_statistics_req = buybtcpay.MerchantMoneyUsageStatisticsReq() # MerchantMoneyUsageStatisticsReq | 

    try:
        # 统计商户代付金额
        api_response = api_instance.count_merchant_payout_by_time_between(merchant_money_usage_statistics_req)
        print("The response of OpenStatisticsApi->count_merchant_payout_by_time_between:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenStatisticsApi->count_merchant_payout_by_time_between: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_money_usage_statistics_req** | [**MerchantMoneyUsageStatisticsReq**](MerchantMoneyUsageStatisticsReq.md)|  | 

### Return type

[**BuyBtcResponseListMerchantMoneyUsageStateVo**](BuyBtcResponseListMerchantMoneyUsageStateVo.md)

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

# **count_payout**
> BuyBtcResponseListCountPayoutDto count_payout(merchant_money_base_req)

统计商户代付笔数

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_count_payout_dto import BuyBtcResponseListCountPayoutDto
from buybtcpay.models.merchant_money_base_req import MerchantMoneyBaseReq
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
    api_instance = buybtcpay.OpenStatisticsApi(api_client)
    merchant_money_base_req = buybtcpay.MerchantMoneyBaseReq() # MerchantMoneyBaseReq | 

    try:
        # 统计商户代付笔数
        api_response = api_instance.count_payout(merchant_money_base_req)
        print("The response of OpenStatisticsApi->count_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenStatisticsApi->count_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_money_base_req** | [**MerchantMoneyBaseReq**](MerchantMoneyBaseReq.md)|  | 

### Return type

[**BuyBtcResponseListCountPayoutDto**](BuyBtcResponseListCountPayoutDto.md)

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

# **merchant_money_state**
> BuyBtcResponseMerchantMoneyStateVo merchant_money_state(merchant_money_base_req)

商户汇总数据

限流1秒一个

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_money_state_vo import BuyBtcResponseMerchantMoneyStateVo
from buybtcpay.models.merchant_money_base_req import MerchantMoneyBaseReq
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
    api_instance = buybtcpay.OpenStatisticsApi(api_client)
    merchant_money_base_req = buybtcpay.MerchantMoneyBaseReq() # MerchantMoneyBaseReq | 

    try:
        # 商户汇总数据
        api_response = api_instance.merchant_money_state(merchant_money_base_req)
        print("The response of OpenStatisticsApi->merchant_money_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenStatisticsApi->merchant_money_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_money_base_req** | [**MerchantMoneyBaseReq**](MerchantMoneyBaseReq.md)|  | 

### Return type

[**BuyBtcResponseMerchantMoneyStateVo**](BuyBtcResponseMerchantMoneyStateVo.md)

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

