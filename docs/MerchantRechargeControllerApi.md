# buybtcpay.MerchantRechargeControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept**](MerchantRechargeControllerApi.md#accept) | **POST** /v1/merchant/recharge/accept/{id} | 
[**add**](MerchantRechargeControllerApi.md#add) | **POST** /v1/merchant/recharge/add | 
[**cancel**](MerchantRechargeControllerApi.md#cancel) | **POST** /v1/merchant/recharge/cancel/{id} | 
[**get_by_id1**](MerchantRechargeControllerApi.md#get_by_id1) | **GET** /v1/merchant/recharge/{id} | 
[**pagination11**](MerchantRechargeControllerApi.md#pagination11) | **POST** /v1/merchant/recharge/pagination | 
[**reject**](MerchantRechargeControllerApi.md#reject) | **POST** /v1/merchant/recharge/reject/{id} | 


# **accept**
> PayResponseMerchantRechargeEntity accept(id, approve_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.approve_dto import ApproveDto
from buybtcpay.models.pay_response_merchant_recharge_entity import PayResponseMerchantRechargeEntity
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
    api_instance = buybtcpay.MerchantRechargeControllerApi(api_client)
    id = 'id_example' # str | 
    approve_dto = buybtcpay.ApproveDto() # ApproveDto | 

    try:
        api_response = api_instance.accept(id, approve_dto)
        print("The response of MerchantRechargeControllerApi->accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantRechargeControllerApi->accept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **approve_dto** | [**ApproveDto**](ApproveDto.md)|  | 

### Return type

[**PayResponseMerchantRechargeEntity**](PayResponseMerchantRechargeEntity.md)

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

# **add**
> PayResponseMerchantRechargeEntity add(merchant_recharge_create_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.merchant_recharge_create_dto import MerchantRechargeCreateDto
from buybtcpay.models.pay_response_merchant_recharge_entity import PayResponseMerchantRechargeEntity
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
    api_instance = buybtcpay.MerchantRechargeControllerApi(api_client)
    merchant_recharge_create_dto = buybtcpay.MerchantRechargeCreateDto() # MerchantRechargeCreateDto | 

    try:
        api_response = api_instance.add(merchant_recharge_create_dto)
        print("The response of MerchantRechargeControllerApi->add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantRechargeControllerApi->add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_recharge_create_dto** | [**MerchantRechargeCreateDto**](MerchantRechargeCreateDto.md)|  | 

### Return type

[**PayResponseMerchantRechargeEntity**](PayResponseMerchantRechargeEntity.md)

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

# **cancel**
> PayResponseMerchantRechargeEntity cancel(id, approve_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.approve_dto import ApproveDto
from buybtcpay.models.pay_response_merchant_recharge_entity import PayResponseMerchantRechargeEntity
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
    api_instance = buybtcpay.MerchantRechargeControllerApi(api_client)
    id = 'id_example' # str | 
    approve_dto = buybtcpay.ApproveDto() # ApproveDto | 

    try:
        api_response = api_instance.cancel(id, approve_dto)
        print("The response of MerchantRechargeControllerApi->cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantRechargeControllerApi->cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **approve_dto** | [**ApproveDto**](ApproveDto.md)|  | 

### Return type

[**PayResponseMerchantRechargeEntity**](PayResponseMerchantRechargeEntity.md)

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

# **get_by_id1**
> PayResponseMerchantRechargeEntity get_by_id1(id)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_merchant_recharge_entity import PayResponseMerchantRechargeEntity
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
    api_instance = buybtcpay.MerchantRechargeControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_by_id1(id)
        print("The response of MerchantRechargeControllerApi->get_by_id1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantRechargeControllerApi->get_by_id1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PayResponseMerchantRechargeEntity**](PayResponseMerchantRechargeEntity.md)

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

# **pagination11**
> PayResponsePaginationMerchantRechargeEntity pagination11(pay_pagination_query_pagination_query)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_pagination_query import PayPaginationQueryPaginationQuery
from buybtcpay.models.pay_response_pagination_merchant_recharge_entity import PayResponsePaginationMerchantRechargeEntity
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
    api_instance = buybtcpay.MerchantRechargeControllerApi(api_client)
    pay_pagination_query_pagination_query = buybtcpay.PayPaginationQueryPaginationQuery() # PayPaginationQueryPaginationQuery | 

    try:
        api_response = api_instance.pagination11(pay_pagination_query_pagination_query)
        print("The response of MerchantRechargeControllerApi->pagination11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantRechargeControllerApi->pagination11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_pagination_query** | [**PayPaginationQueryPaginationQuery**](PayPaginationQueryPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationMerchantRechargeEntity**](PayResponsePaginationMerchantRechargeEntity.md)

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

# **reject**
> PayResponseMerchantRechargeEntity reject(id, approve_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.approve_dto import ApproveDto
from buybtcpay.models.pay_response_merchant_recharge_entity import PayResponseMerchantRechargeEntity
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
    api_instance = buybtcpay.MerchantRechargeControllerApi(api_client)
    id = 'id_example' # str | 
    approve_dto = buybtcpay.ApproveDto() # ApproveDto | 

    try:
        api_response = api_instance.reject(id, approve_dto)
        print("The response of MerchantRechargeControllerApi->reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantRechargeControllerApi->reject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **approve_dto** | [**ApproveDto**](ApproveDto.md)|  | 

### Return type

[**PayResponseMerchantRechargeEntity**](PayResponseMerchantRechargeEntity.md)

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

