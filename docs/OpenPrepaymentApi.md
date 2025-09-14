# buybtcpay.OpenPrepaymentApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close**](OpenPrepaymentApi.md#close) | **POST** /v1/open/prepayment/close/{businessId} | 关闭预付订单
[**create_prepayment_order**](OpenPrepaymentApi.md#create_prepayment_order) | **POST** /v1/open/prepayment | 创建预付订单
[**currency_conversion**](OpenPrepaymentApi.md#currency_conversion) | **POST** /v1/open/prepayment/currency/conversion | 币种转换
[**pagination4**](OpenPrepaymentApi.md#pagination4) | **POST** /v1/open/prepayment/pagination | 查询预付订单
[**payment_aggregation**](OpenPrepaymentApi.md#payment_aggregation) | **POST** /v1/open/prepayment/payment/aggregation | 合并支付
[**payment_merchant_to_merchant**](OpenPrepaymentApi.md#payment_merchant_to_merchant) | **POST** /v1/open/prepayment/payment/merchant/to/merchant | 商户到商户转账
[**payment_merchant_to_merchant_by_business_id**](OpenPrepaymentApi.md#payment_merchant_to_merchant_by_business_id) | **POST** /v1/open/prepayment/payment/merchant/to/merchant/{businessId} | 基于预付单的商户到商户转账
[**payment_ngn_currency**](OpenPrepaymentApi.md#payment_ngn_currency) | **POST** /v1/open/prepayment/payment/ngn/{businessId} | 支付NGN币种
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

# **currency_conversion**
> BuyBtcResponsePaymentOrderEntity currency_conversion(currency_conversion_dto)

币种转换

币种转换，需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
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

# **pagination4**
> BuyBtcResponsePayPaginationPrepaymentOrderEntity pagination4(pay_pagination_query_prepayment_order_pagination_query)

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
        api_response = api_instance.pagination4(pay_pagination_query_prepayment_order_pagination_query)
        print("The response of OpenPrepaymentApi->pagination4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->pagination4: %s\n" % e)
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

# **payment_aggregation**
> BuyBtcResponsePaymentOrderEntity payment_aggregation(prepayment_aggregation_dto)

合并支付

合并支付，只支持商户到商户的支付，接口参数需要签名

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
from buybtcpay.models.prepayment_aggregation_dto import PrepaymentAggregationDto
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
    prepayment_aggregation_dto = buybtcpay.PrepaymentAggregationDto() # PrepaymentAggregationDto | 

    try:
        # 合并支付
        api_response = api_instance.payment_aggregation(prepayment_aggregation_dto)
        print("The response of OpenPrepaymentApi->payment_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->payment_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_aggregation_dto** | [**PrepaymentAggregationDto**](PrepaymentAggregationDto.md)|  | 

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

# **payment_merchant_to_merchant**
> BuyBtcResponsePaymentOrderEntity payment_merchant_to_merchant(merchant_to_merchant_automatic_params)

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
        api_response = api_instance.payment_merchant_to_merchant(merchant_to_merchant_automatic_params)
        print("The response of OpenPrepaymentApi->payment_merchant_to_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->payment_merchant_to_merchant: %s\n" % e)
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

# **payment_merchant_to_merchant_by_business_id**
> BuyBtcResponsePaymentOrderEntity payment_merchant_to_merchant_by_business_id(business_id, merchant_to_merchant_params)

基于预付单的商户到商户转账

商户到商户转账，同商户不同钱包互转也可以使用这个接口。需要签名，签名算法见MD文档

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
from buybtcpay.models.merchant_to_merchant_params import MerchantToMerchantParams
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
    merchant_to_merchant_params = buybtcpay.MerchantToMerchantParams() # MerchantToMerchantParams | 

    try:
        # 基于预付单的商户到商户转账
        api_response = api_instance.payment_merchant_to_merchant_by_business_id(business_id, merchant_to_merchant_params)
        print("The response of OpenPrepaymentApi->payment_merchant_to_merchant_by_business_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->payment_merchant_to_merchant_by_business_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 
 **merchant_to_merchant_params** | [**MerchantToMerchantParams**](MerchantToMerchantParams.md)|  | 

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

# **payment_ngn_currency**
> BuyBtcResponsePaymentOrderEntity payment_ngn_currency(business_id, payment_palm_pay_param)

支付NGN币种

支付NGN币种

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_payment_order_entity import BuyBtcResponsePaymentOrderEntity
from buybtcpay.models.payment_palm_pay_param import PaymentPalmPayParam
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
    payment_palm_pay_param = buybtcpay.PaymentPalmPayParam() # PaymentPalmPayParam | 

    try:
        # 支付NGN币种
        api_response = api_instance.payment_ngn_currency(business_id, payment_palm_pay_param)
        print("The response of OpenPrepaymentApi->payment_ngn_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPrepaymentApi->payment_ngn_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 
 **payment_palm_pay_param** | [**PaymentPalmPayParam**](PaymentPalmPayParam.md)|  | 

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

