# buybtcpay.MerchantControllerApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active1**](MerchantControllerApi.md#active1) | **POST** /v1/merchant/active/{id} | 
[**create_merchant1**](MerchantControllerApi.md#create_merchant1) | **POST** /v1/merchant/add | 
[**disable1**](MerchantControllerApi.md#disable1) | **POST** /v1/merchant/disable/{id} | 
[**generate_rsa_key_pair**](MerchantControllerApi.md#generate_rsa_key_pair) | **GET** /v1/merchant/key/pair | 
[**get_access_token**](MerchantControllerApi.md#get_access_token) | **GET** /v1/merchant/access/token | 
[**get_by_id**](MerchantControllerApi.md#get_by_id) | **GET** /v1/merchant/{id} | 
[**get_by_merchant_id**](MerchantControllerApi.md#get_by_merchant_id) | **GET** /v1/merchant/merchant/{id} | 
[**get_signed_merchant**](MerchantControllerApi.md#get_signed_merchant) | **GET** /v1/merchant/signed | 
[**pagination12**](MerchantControllerApi.md#pagination12) | **POST** /v1/merchant/pagination | 
[**set_merchant_public_key**](MerchantControllerApi.md#set_merchant_public_key) | **POST** /v1/merchant/key/pair | 


# **active1**
> PayResponseMerchantEntityDto active1(id)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_merchant_entity_dto import PayResponseMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.active1(id)
        print("The response of MerchantControllerApi->active1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->active1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PayResponseMerchantEntityDto**](PayResponseMerchantEntityDto.md)

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

# **create_merchant1**
> PayResponseMerchantEntityDto create_merchant1(create_merchant_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.create_merchant_dto import CreateMerchantDto
from buybtcpay.models.pay_response_merchant_entity_dto import PayResponseMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    create_merchant_dto = buybtcpay.CreateMerchantDto() # CreateMerchantDto | 

    try:
        api_response = api_instance.create_merchant1(create_merchant_dto)
        print("The response of MerchantControllerApi->create_merchant1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->create_merchant1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_merchant_dto** | [**CreateMerchantDto**](CreateMerchantDto.md)|  | 

### Return type

[**PayResponseMerchantEntityDto**](PayResponseMerchantEntityDto.md)

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

# **disable1**
> PayResponseMerchantEntityDto disable1(id)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_merchant_entity_dto import PayResponseMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.disable1(id)
        print("The response of MerchantControllerApi->disable1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->disable1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PayResponseMerchantEntityDto**](PayResponseMerchantEntityDto.md)

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

# **generate_rsa_key_pair**
> BuyBtcResponseRsaKeyPair generate_rsa_key_pair()

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_rsa_key_pair import BuyBtcResponseRsaKeyPair
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)

    try:
        api_response = api_instance.generate_rsa_key_pair()
        print("The response of MerchantControllerApi->generate_rsa_key_pair:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->generate_rsa_key_pair: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseRsaKeyPair**](BuyBtcResponseRsaKeyPair.md)

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

# **get_access_token**
> BuyBtcResponseString get_access_token()

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
    api_instance = buybtcpay.MerchantControllerApi(api_client)

    try:
        api_response = api_instance.get_access_token()
        print("The response of MerchantControllerApi->get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->get_access_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyBtcResponseString**](BuyBtcResponseString.md)

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

# **get_by_id**
> PayResponseMerchantEntityDto get_by_id(id)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_merchant_entity_dto import PayResponseMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_by_id(id)
        print("The response of MerchantControllerApi->get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PayResponseMerchantEntityDto**](PayResponseMerchantEntityDto.md)

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

# **get_by_merchant_id**
> PayResponseMerchantEntityDto get_by_merchant_id(id)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_merchant_entity_dto import PayResponseMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_by_merchant_id(id)
        print("The response of MerchantControllerApi->get_by_merchant_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->get_by_merchant_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PayResponseMerchantEntityDto**](PayResponseMerchantEntityDto.md)

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

# **get_signed_merchant**
> PayResponseMerchantEntityDto get_signed_merchant()

### Example


```python
import buybtcpay
from buybtcpay.models.pay_response_merchant_entity_dto import PayResponseMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)

    try:
        api_response = api_instance.get_signed_merchant()
        print("The response of MerchantControllerApi->get_signed_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->get_signed_merchant: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayResponseMerchantEntityDto**](PayResponseMerchantEntityDto.md)

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

# **pagination12**
> PayResponsePaginationMerchantEntityDto pagination12(pay_pagination_query_pagination_query)

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_pagination_query import PayPaginationQueryPaginationQuery
from buybtcpay.models.pay_response_pagination_merchant_entity_dto import PayResponsePaginationMerchantEntityDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    pay_pagination_query_pagination_query = buybtcpay.PayPaginationQueryPaginationQuery() # PayPaginationQueryPaginationQuery | 

    try:
        api_response = api_instance.pagination12(pay_pagination_query_pagination_query)
        print("The response of MerchantControllerApi->pagination12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->pagination12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_pagination_query** | [**PayPaginationQueryPaginationQuery**](PayPaginationQueryPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationMerchantEntityDto**](PayResponsePaginationMerchantEntityDto.md)

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

# **set_merchant_public_key**
> BuyBtcResponseMerchantEntityDto set_merchant_public_key(set_merchant_public_key_dto)

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_merchant_entity_dto import BuyBtcResponseMerchantEntityDto
from buybtcpay.models.set_merchant_public_key_dto import SetMerchantPublicKeyDto
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
    api_instance = buybtcpay.MerchantControllerApi(api_client)
    set_merchant_public_key_dto = buybtcpay.SetMerchantPublicKeyDto() # SetMerchantPublicKeyDto | 

    try:
        api_response = api_instance.set_merchant_public_key(set_merchant_public_key_dto)
        print("The response of MerchantControllerApi->set_merchant_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantControllerApi->set_merchant_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_merchant_public_key_dto** | [**SetMerchantPublicKeyDto**](SetMerchantPublicKeyDto.md)|  | 

### Return type

[**BuyBtcResponseMerchantEntityDto**](BuyBtcResponseMerchantEntityDto.md)

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

