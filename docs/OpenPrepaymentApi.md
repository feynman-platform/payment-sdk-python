# buybtcpay.OpenPrepaymentApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close**](OpenPrepaymentApi.md#close) | **POST** /v1/open/prepayment/close/{businessId} | 关闭预付订单
[**create_prepayment_order**](OpenPrepaymentApi.md#create_prepayment_order) | **POST** /v1/open/prepayment | 创建预付订单
[**create_trade_prepayment_order**](OpenPrepaymentApi.md#create_trade_prepayment_order) | **POST** /v1/open/prepayment/trade | 创建C站业务交易预付订单
[**currency_conversion**](OpenPrepaymentApi.md#currency_conversion) | **POST** /v1/open/prepayment/currency/conversion | 币种转换
[**find_merchant_max_available_wallet**](OpenPrepaymentApi.md#find_merchant_max_available_wallet) | **POST** /v1/open/prepayment/merchant/max/available/wallet | 查找商户可用余额最多的钱包
[**merchant_trade_transfer**](OpenPrepaymentApi.md#merchant_trade_transfer) | **POST** /v1/open/prepayment/payment/merchant/to/merchant | 商户到商户转账
[**merchant_trade_transfer_by_business_id**](OpenPrepaymentApi.md#merchant_trade_transfer_by_business_id) | **POST** /v1/open/prepayment/payment/merchant/to/merchant/{businessId} | 基于预付单的商户到商户转账
[**merchant_wallet_transfer**](OpenPrepaymentApi.md#merchant_wallet_transfer) | **POST** /v1/open/prepayment/merchant/transfer | 商户自己不同类型的钱包互转
[**pagination5**](OpenPrepaymentApi.md#pagination5) | **POST** /v1/open/prepayment/pagination | 查询预付订单
[**trade_transfer_aggregation**](OpenPrepaymentApi.md#trade_transfer_aggregation) | **POST** /v1/open/prepayment/trade/transfer/aggregation | 交易支付中的合并支付
[**update_amount**](OpenPrepaymentApi.md#update_amount) | **POST** /v1/open/prepayment/amount | 更新预付订单金额


# **close**
> BuyBtcResponsePrepaymentOrderEntity close(business_id)

关闭预付订单

关闭预付订单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_prepayment_order_entity import BuyBtcResponsePrepaymentOrderEntity
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    business_id = 'business_id_example' # str | 

    try:
        # 关闭预付订单
        api_response = api_instance.close(business_id)
        print("The response of OpenPrepaymentApi->close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 

### Return type

[**BuyBtcResponsePrepaymentOrderEntity**](BuyBtcResponsePrepaymentOrderEntity.md)

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

# **create_prepayment_order**
> BuyBtcResponsePrepaymentOrderEntity create_prepayment_order(create_prepayment_order_dto)

创建预付订单

请求参数需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_prepayment_order_entity import BuyBtcResponsePrepaymentOrderEntity
from buybtcpay.models.create_prepayment_order_dto import CreatePrepaymentOrderDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    create_prepayment_order_dto = buybtcpay.CreatePrepaymentOrderDto() # CreatePrepaymentOrderDto | 

    try:
        # 创建预付订单
        api_response = api_instance.create_prepayment_order(create_prepayment_order_dto)
        print("The response of OpenPrepaymentApi->create_prepayment_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->create_prepayment_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_prepayment_order_dto** | [**CreatePrepaymentOrderDto**](CreatePrepaymentOrderDto.md)|  | 

### Return type

[**BuyBtcResponsePrepaymentOrderEntity**](BuyBtcResponsePrepaymentOrderEntity.md)

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

# **create_trade_prepayment_order**
> BuyBtcResponsePrepaymentOrderEntity create_trade_prepayment_order(create_trade_prepayment_order_dto)

创建C站业务交易预付订单

请求参数需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_prepayment_order_entity import BuyBtcResponsePrepaymentOrderEntity
from buybtcpay.models.create_trade_prepayment_order_dto import CreateTradePrepaymentOrderDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    create_trade_prepayment_order_dto = buybtcpay.CreateTradePrepaymentOrderDto() # CreateTradePrepaymentOrderDto | 

    try:
        # 创建C站业务交易预付订单
        api_response = api_instance.create_trade_prepayment_order(create_trade_prepayment_order_dto)
        print("The response of OpenPrepaymentApi->create_trade_prepayment_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->create_trade_prepayment_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_trade_prepayment_order_dto** | [**CreateTradePrepaymentOrderDto**](CreateTradePrepaymentOrderDto.md)|  | 

### Return type

[**BuyBtcResponsePrepaymentOrderEntity**](BuyBtcResponsePrepaymentOrderEntity.md)

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

# **currency_conversion**
> BuyBtcResponseListMerchantWalletEntity currency_conversion(currency_conversion_dto)

币种转换

币种转换，需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity
from buybtcpay.models.currency_conversion_dto import CurrencyConversionDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    currency_conversion_dto = buybtcpay.CurrencyConversionDto() # CurrencyConversionDto | 

    try:
        # 币种转换
        api_response = api_instance.currency_conversion(currency_conversion_dto)
        print("The response of OpenPrepaymentApi->currency_conversion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->currency_conversion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_conversion_dto** | [**CurrencyConversionDto**](CurrencyConversionDto.md)|  | 

### Return type

[**BuyBtcResponseListMerchantWalletEntity**](BuyBtcResponseListMerchantWalletEntity.md)

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

# **find_merchant_max_available_wallet**
> BuyBtcResponseMerchantWalletEntity find_merchant_max_available_wallet(find_merchant_max_available_wallet_dto)

查找商户可用余额最多的钱包

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_wallet_entity import BuyBtcResponseMerchantWalletEntity
from buybtcpay.models.find_merchant_max_available_wallet_dto import FindMerchantMaxAvailableWalletDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    find_merchant_max_available_wallet_dto = buybtcpay.FindMerchantMaxAvailableWalletDto() # FindMerchantMaxAvailableWalletDto | 

    try:
        # 查找商户可用余额最多的钱包
        api_response = api_instance.find_merchant_max_available_wallet(find_merchant_max_available_wallet_dto)
        print("The response of OpenPrepaymentApi->find_merchant_max_available_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->find_merchant_max_available_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_merchant_max_available_wallet_dto** | [**FindMerchantMaxAvailableWalletDto**](FindMerchantMaxAvailableWalletDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantWalletEntity**](BuyBtcResponseMerchantWalletEntity.md)

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

# **merchant_trade_transfer**
> BuyBtcResponsePaymentOrderEntity merchant_trade_transfer(merchant_to_merchant_automatic_params)

商户到商户转账

该接口不依赖预付单业务ID，会主动创建预付单，需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
from buybtcpay.models.merchant_to_merchant_automatic_params import MerchantToMerchantAutomaticParams
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    merchant_to_merchant_automatic_params = buybtcpay.MerchantToMerchantAutomaticParams() # MerchantToMerchantAutomaticParams | 

    try:
        # 商户到商户转账
        api_response = api_instance.merchant_trade_transfer(merchant_to_merchant_automatic_params)
        print("The response of OpenPrepaymentApi->merchant_trade_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->merchant_trade_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_to_merchant_automatic_params** | [**MerchantToMerchantAutomaticParams**](MerchantToMerchantAutomaticParams.md)|  | 

### Return type

[**BuyBtcResponsePaymentOrderEntity**](BuyBtcResponsePaymentOrderEntity.md)

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

# **merchant_trade_transfer_by_business_id**
> BuyBtcResponsePaymentOrderEntity merchant_trade_transfer_by_business_id(business_id, merchant_trade_transfer_by_business_id_dto)

基于预付单的商户到商户转账

商户到商户转账，同商户不同钱包互转也可以使用这个接口。需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
from buybtcpay.models.merchant_trade_transfer_by_business_id_dto import MerchantTradeTransferByBusinessIdDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    business_id = 'business_id_example' # str | 
    merchant_trade_transfer_by_business_id_dto = buybtcpay.MerchantTradeTransferByBusinessIdDto() # MerchantTradeTransferByBusinessIdDto | 

    try:
        # 基于预付单的商户到商户转账
        api_response = api_instance.merchant_trade_transfer_by_business_id(business_id, merchant_trade_transfer_by_business_id_dto)
        print("The response of OpenPrepaymentApi->merchant_trade_transfer_by_business_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->merchant_trade_transfer_by_business_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 
 **merchant_trade_transfer_by_business_id_dto** | [**MerchantTradeTransferByBusinessIdDto**](MerchantTradeTransferByBusinessIdDto.md)|  | 

### Return type

[**BuyBtcResponsePaymentOrderEntity**](BuyBtcResponsePaymentOrderEntity.md)

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

# **merchant_wallet_transfer**
> BuyBtcResponseListMerchantWalletEntity merchant_wallet_transfer(merchant_wallet_transfer_dto)

商户自己不同类型的钱包互转

要求同币种

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_list_merchant_wallet_entity import BuyBtcResponseListMerchantWalletEntity
from buybtcpay.models.merchant_wallet_transfer_dto import MerchantWalletTransferDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    merchant_wallet_transfer_dto = buybtcpay.MerchantWalletTransferDto() # MerchantWalletTransferDto | 

    try:
        # 商户自己不同类型的钱包互转
        api_response = api_instance.merchant_wallet_transfer(merchant_wallet_transfer_dto)
        print("The response of OpenPrepaymentApi->merchant_wallet_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->merchant_wallet_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_wallet_transfer_dto** | [**MerchantWalletTransferDto**](MerchantWalletTransferDto.md)|  | 

### Return type

[**BuyBtcResponseListMerchantWalletEntity**](BuyBtcResponseListMerchantWalletEntity.md)

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

# **pagination5**
> BuyBtcResponsePayPaginationPrepaymentOrderEntity pagination5(pay_pagination_query_prepayment_order_pagination_query)

查询预付订单

分页查询预付订单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_pay_pagination_prepayment_order_entity import BuyBtcResponsePayPaginationPrepaymentOrderEntity
from buybtcpay.models.pay_pagination_query_prepayment_order_pagination_query import PayPaginationQueryPrepaymentOrderPaginationQuery
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    pay_pagination_query_prepayment_order_pagination_query = buybtcpay.PayPaginationQueryPrepaymentOrderPaginationQuery() # PayPaginationQueryPrepaymentOrderPaginationQuery | 

    try:
        # 查询预付订单
        api_response = api_instance.pagination5(pay_pagination_query_prepayment_order_pagination_query)
        print("The response of OpenPrepaymentApi->pagination5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->pagination5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_prepayment_order_pagination_query** | [**PayPaginationQueryPrepaymentOrderPaginationQuery**](PayPaginationQueryPrepaymentOrderPaginationQuery.md)|  | 

### Return type

[**BuyBtcResponsePayPaginationPrepaymentOrderEntity**](BuyBtcResponsePayPaginationPrepaymentOrderEntity.md)

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

# **trade_transfer_aggregation**
> BuyBtcResponsePaymentOrderEntity trade_transfer_aggregation(trade_transfer_aggregation_dto)

交易支付中的合并支付

合并支付，只支持商户到商户的支付，接口参数需要签名

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
from buybtcpay.models.trade_transfer_aggregation_dto import TradeTransferAggregationDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    trade_transfer_aggregation_dto = buybtcpay.TradeTransferAggregationDto() # TradeTransferAggregationDto | 

    try:
        # 交易支付中的合并支付
        api_response = api_instance.trade_transfer_aggregation(trade_transfer_aggregation_dto)
        print("The response of OpenPrepaymentApi->trade_transfer_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->trade_transfer_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_transfer_aggregation_dto** | [**TradeTransferAggregationDto**](TradeTransferAggregationDto.md)|  | 

### Return type

[**BuyBtcResponsePaymentOrderEntity**](BuyBtcResponsePaymentOrderEntity.md)

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

# **update_amount**
> BuyBtcResponsePrepaymentOrderEntity update_amount(update_prepayment_order_amount_dto)

更新预付订单金额

更新预付订单金额

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_prepayment_order_entity import BuyBtcResponsePrepaymentOrderEntity
from buybtcpay.models.update_prepayment_order_amount_dto import UpdatePrepaymentOrderAmountDto
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
    api_instance = buybtcpay.OpenPrepaymentApi(api_client)
    update_prepayment_order_amount_dto = buybtcpay.UpdatePrepaymentOrderAmountDto() # UpdatePrepaymentOrderAmountDto | 

    try:
        # 更新预付订单金额
        api_response = api_instance.update_amount(update_prepayment_order_amount_dto)
        print("The response of OpenPrepaymentApi->update_amount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->update_amount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_prepayment_order_amount_dto** | [**UpdatePrepaymentOrderAmountDto**](UpdatePrepaymentOrderAmountDto.md)|  | 

### Return type

[**BuyBtcResponsePrepaymentOrderEntity**](BuyBtcResponsePrepaymentOrderEntity.md)

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

