# buybtcpay.OpenApprovalApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_frozen_approval**](OpenApprovalApi.md#create_frozen_approval) | **POST** /v1/open/approval/frozen | 创建冻结审批单
[**create_merchant_recharge_approval**](OpenApprovalApi.md#create_merchant_recharge_approval) | **POST** /v1/open/approval/merchant/recharge | 创建商户充值审批单
[**create_merchant_self_service_recharge_approval**](OpenApprovalApi.md#create_merchant_self_service_recharge_approval) | **POST** /v1/open/approval/merchant/self/service/recharge | 创建商户自助充值审批单
[**create_platform_recharge_approval**](OpenApprovalApi.md#create_platform_recharge_approval) | **POST** /v1/open/approval/platform/recharge | 创建平台充值审批单
[**create_refund_approval**](OpenApprovalApi.md#create_refund_approval) | **POST** /v1/open/approval/refund | 创建退款审批单
[**create_reversal_merchant_to_merchant_approval**](OpenApprovalApi.md#create_reversal_merchant_to_merchant_approval) | **POST** /v1/open/approval/reversal/merchant/to/merchant | 创建商户到商户转账审批单
[**create_reversal_merchant_to_platfrom_approval**](OpenApprovalApi.md#create_reversal_merchant_to_platfrom_approval) | **POST** /v1/open/approval/reversal/merchant/to/platform | 创建商户到平台转账审批单
[**create_reversal_platform_to_merchant_approval**](OpenApprovalApi.md#create_reversal_platform_to_merchant_approval) | **POST** /v1/open/approval/reversal/platform/to/merchant | 创建平台转账到商户审批单
[**create_unfrozen_approval**](OpenApprovalApi.md#create_unfrozen_approval) | **POST** /v1/open/approval/unfrozen | 创建解冻审批单
[**create_virtual_account_recharge_approval**](OpenApprovalApi.md#create_virtual_account_recharge_approval) | **POST** /v1/open/approval/virtual/account/recharge | 创建虚拟账户充值审批单
[**pagination9**](OpenApprovalApi.md#pagination9) | **POST** /v1/open/approval/pagination | 分页查询审批单
[**processing_approval**](OpenApprovalApi.md#processing_approval) | **POST** /v1/open/approval/processing | 处理审批单
[**update_self_service_approval_recevied**](OpenApprovalApi.md#update_self_service_approval_recevied) | **POST** /v1/open/approval/self/service/recharge/received | 更新自助充值审批单用户是否已经收款
[**update_self_service_approval_submited**](OpenApprovalApi.md#update_self_service_approval_submited) | **POST** /v1/open/approval/self/service/recharge/submited | 更新自助充值审批单用户是否已经转账


# **create_frozen_approval**
> BuyBtcResponseApprovalEntity create_frozen_approval(create_approval_dto_create_frozen_approval_dto)

创建冻结审批单

只有管理员才有权限创建冻结审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_frozen_approval_dto import CreateApprovalDtoCreateFrozenApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_frozen_approval_dto = buybtcpay.CreateApprovalDtoCreateFrozenApprovalDto() # CreateApprovalDtoCreateFrozenApprovalDto | 

    try:
        # 创建冻结审批单
        api_response = api_instance.create_frozen_approval(create_approval_dto_create_frozen_approval_dto)
        print("The response of OpenApprovalApi->create_frozen_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_frozen_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_frozen_approval_dto** | [**CreateApprovalDtoCreateFrozenApprovalDto**](CreateApprovalDtoCreateFrozenApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_merchant_recharge_approval**
> BuyBtcResponseApprovalEntity create_merchant_recharge_approval(create_approval_dto_create_merchant_recharge_approval_dto)

创建商户充值审批单

只有管理员才有权限创建商户充值审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_merchant_recharge_approval_dto import CreateApprovalDtoCreateMerchantRechargeApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_merchant_recharge_approval_dto = buybtcpay.CreateApprovalDtoCreateMerchantRechargeApprovalDto() # CreateApprovalDtoCreateMerchantRechargeApprovalDto | 

    try:
        # 创建商户充值审批单
        api_response = api_instance.create_merchant_recharge_approval(create_approval_dto_create_merchant_recharge_approval_dto)
        print("The response of OpenApprovalApi->create_merchant_recharge_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_merchant_recharge_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_merchant_recharge_approval_dto** | [**CreateApprovalDtoCreateMerchantRechargeApprovalDto**](CreateApprovalDtoCreateMerchantRechargeApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_merchant_self_service_recharge_approval**
> BuyBtcResponseApprovalEntity create_merchant_self_service_recharge_approval(create_approval_dto_create_merchant_self_recharge_dto)

创建商户自助充值审批单

用户手动充值，系统检测到收款后，自动审批。
管理员可以给所有的商户创建，主账户可以给子账户创建，其他用户只能给自己创建。


### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_merchant_self_recharge_dto import CreateApprovalDtoCreateMerchantSelfRechargeDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_merchant_self_recharge_dto = buybtcpay.CreateApprovalDtoCreateMerchantSelfRechargeDto() # CreateApprovalDtoCreateMerchantSelfRechargeDto | 

    try:
        # 创建商户自助充值审批单
        api_response = api_instance.create_merchant_self_service_recharge_approval(create_approval_dto_create_merchant_self_recharge_dto)
        print("The response of OpenApprovalApi->create_merchant_self_service_recharge_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_merchant_self_service_recharge_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_merchant_self_recharge_dto** | [**CreateApprovalDtoCreateMerchantSelfRechargeDto**](CreateApprovalDtoCreateMerchantSelfRechargeDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_platform_recharge_approval**
> BuyBtcResponseApprovalEntity create_platform_recharge_approval(create_approval_dto_create_platform_recharge_approval_dto)

创建平台充值审批单

只有管理员才有权限创建平台充值审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_platform_recharge_approval_dto import CreateApprovalDtoCreatePlatformRechargeApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_platform_recharge_approval_dto = buybtcpay.CreateApprovalDtoCreatePlatformRechargeApprovalDto() # CreateApprovalDtoCreatePlatformRechargeApprovalDto | 

    try:
        # 创建平台充值审批单
        api_response = api_instance.create_platform_recharge_approval(create_approval_dto_create_platform_recharge_approval_dto)
        print("The response of OpenApprovalApi->create_platform_recharge_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_platform_recharge_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_platform_recharge_approval_dto** | [**CreateApprovalDtoCreatePlatformRechargeApprovalDto**](CreateApprovalDtoCreatePlatformRechargeApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_refund_approval**
> BuyBtcResponseApprovalEntity create_refund_approval(create_approval_dto_create_refund_approval_dto)

创建退款审批单

只有管理员才有权限创建退款审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_refund_approval_dto import CreateApprovalDtoCreateRefundApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_refund_approval_dto = buybtcpay.CreateApprovalDtoCreateRefundApprovalDto() # CreateApprovalDtoCreateRefundApprovalDto | 

    try:
        # 创建退款审批单
        api_response = api_instance.create_refund_approval(create_approval_dto_create_refund_approval_dto)
        print("The response of OpenApprovalApi->create_refund_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_refund_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_refund_approval_dto** | [**CreateApprovalDtoCreateRefundApprovalDto**](CreateApprovalDtoCreateRefundApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_reversal_merchant_to_merchant_approval**
> BuyBtcResponseApprovalEntity create_reversal_merchant_to_merchant_approval(create_approval_dto_create_reversal_merchant_to_merchant_approval_dto)

创建商户到商户转账审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_reversal_merchant_to_merchant_approval_dto import CreateApprovalDtoCreateReversalMerchantToMerchantApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_reversal_merchant_to_merchant_approval_dto = buybtcpay.CreateApprovalDtoCreateReversalMerchantToMerchantApprovalDto() # CreateApprovalDtoCreateReversalMerchantToMerchantApprovalDto | 

    try:
        # 创建商户到商户转账审批单
        api_response = api_instance.create_reversal_merchant_to_merchant_approval(create_approval_dto_create_reversal_merchant_to_merchant_approval_dto)
        print("The response of OpenApprovalApi->create_reversal_merchant_to_merchant_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_reversal_merchant_to_merchant_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_reversal_merchant_to_merchant_approval_dto** | [**CreateApprovalDtoCreateReversalMerchantToMerchantApprovalDto**](CreateApprovalDtoCreateReversalMerchantToMerchantApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_reversal_merchant_to_platfrom_approval**
> BuyBtcResponseApprovalEntity create_reversal_merchant_to_platfrom_approval(create_approval_dto_create_reversal_merchant_to_platform_approval_dto)

创建商户到平台转账审批单

只有管理员才有权限创建商户到平台转账审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_reversal_merchant_to_platform_approval_dto import CreateApprovalDtoCreateReversalMerchantToPlatformApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_reversal_merchant_to_platform_approval_dto = buybtcpay.CreateApprovalDtoCreateReversalMerchantToPlatformApprovalDto() # CreateApprovalDtoCreateReversalMerchantToPlatformApprovalDto | 

    try:
        # 创建商户到平台转账审批单
        api_response = api_instance.create_reversal_merchant_to_platfrom_approval(create_approval_dto_create_reversal_merchant_to_platform_approval_dto)
        print("The response of OpenApprovalApi->create_reversal_merchant_to_platfrom_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_reversal_merchant_to_platfrom_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_reversal_merchant_to_platform_approval_dto** | [**CreateApprovalDtoCreateReversalMerchantToPlatformApprovalDto**](CreateApprovalDtoCreateReversalMerchantToPlatformApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_reversal_platform_to_merchant_approval**
> BuyBtcResponseApprovalEntity create_reversal_platform_to_merchant_approval(create_approval_dto_create_reversal_platfrom_to_merchant_approval_dto)

创建平台转账到商户审批单

只有管理员才有权限创建平台转账到商户审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_reversal_platfrom_to_merchant_approval_dto import CreateApprovalDtoCreateReversalPlatfromToMerchantApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_reversal_platfrom_to_merchant_approval_dto = buybtcpay.CreateApprovalDtoCreateReversalPlatfromToMerchantApprovalDto() # CreateApprovalDtoCreateReversalPlatfromToMerchantApprovalDto | 

    try:
        # 创建平台转账到商户审批单
        api_response = api_instance.create_reversal_platform_to_merchant_approval(create_approval_dto_create_reversal_platfrom_to_merchant_approval_dto)
        print("The response of OpenApprovalApi->create_reversal_platform_to_merchant_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_reversal_platform_to_merchant_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_reversal_platfrom_to_merchant_approval_dto** | [**CreateApprovalDtoCreateReversalPlatfromToMerchantApprovalDto**](CreateApprovalDtoCreateReversalPlatfromToMerchantApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_unfrozen_approval**
> BuyBtcResponseApprovalEntity create_unfrozen_approval(create_approval_dto_create_unfronzen_approval_dto)

创建解冻审批单

只有管理员才有权限创建解冻审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_unfronzen_approval_dto import CreateApprovalDtoCreateUnfronzenApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_unfronzen_approval_dto = buybtcpay.CreateApprovalDtoCreateUnfronzenApprovalDto() # CreateApprovalDtoCreateUnfronzenApprovalDto | 

    try:
        # 创建解冻审批单
        api_response = api_instance.create_unfrozen_approval(create_approval_dto_create_unfronzen_approval_dto)
        print("The response of OpenApprovalApi->create_unfrozen_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_unfrozen_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_unfronzen_approval_dto** | [**CreateApprovalDtoCreateUnfronzenApprovalDto**](CreateApprovalDtoCreateUnfronzenApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **create_virtual_account_recharge_approval**
> BuyBtcResponseApprovalEntity create_virtual_account_recharge_approval(create_approval_dto_create_virtual_account_recharge_approval_dto)

创建虚拟账户充值审批单

只有管理员才有权限创建虚拟账户充值审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.create_approval_dto_create_virtual_account_recharge_approval_dto import CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    create_approval_dto_create_virtual_account_recharge_approval_dto = buybtcpay.CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto() # CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto | 

    try:
        # 创建虚拟账户充值审批单
        api_response = api_instance.create_virtual_account_recharge_approval(create_approval_dto_create_virtual_account_recharge_approval_dto)
        print("The response of OpenApprovalApi->create_virtual_account_recharge_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->create_virtual_account_recharge_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_approval_dto_create_virtual_account_recharge_approval_dto** | [**CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto**](CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **pagination9**
> PayResponsePaginationApprovalEntity pagination9(pay_pagination_query_approval_pagination_query)

分页查询审批单

如果不是管理员，只能查由自己发起的审批单

### Example


```python
import buybtcpay
from buybtcpay.models.pay_pagination_query_approval_pagination_query import PayPaginationQueryApprovalPaginationQuery
from buybtcpay.models.pay_response_pagination_approval_entity import PayResponsePaginationApprovalEntity
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    pay_pagination_query_approval_pagination_query = buybtcpay.PayPaginationQueryApprovalPaginationQuery() # PayPaginationQueryApprovalPaginationQuery | 

    try:
        # 分页查询审批单
        api_response = api_instance.pagination9(pay_pagination_query_approval_pagination_query)
        print("The response of OpenApprovalApi->pagination9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->pagination9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_pagination_query_approval_pagination_query** | [**PayPaginationQueryApprovalPaginationQuery**](PayPaginationQueryApprovalPaginationQuery.md)|  | 

### Return type

[**PayResponsePaginationApprovalEntity**](PayResponsePaginationApprovalEntity.md)

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

# **processing_approval**
> BuyBtcResponseApprovalEntity processing_approval(processing_approval_dto)

处理审批单

只有管理员才有权限处理审批单

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.processing_approval_dto import ProcessingApprovalDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    processing_approval_dto = buybtcpay.ProcessingApprovalDto() # ProcessingApprovalDto | 

    try:
        # 处理审批单
        api_response = api_instance.processing_approval(processing_approval_dto)
        print("The response of OpenApprovalApi->processing_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->processing_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processing_approval_dto** | [**ProcessingApprovalDto**](ProcessingApprovalDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

# **update_self_service_approval_recevied**
> BuyBtcResponseBoolean update_self_service_approval_recevied(update_self_service_approval_recevied_dto)

更新自助充值审批单用户是否已经收款

开发、测试环境可用

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_boolean import BuyBtcResponseBoolean
from buybtcpay.models.update_self_service_approval_recevied_dto import UpdateSelfServiceApprovalReceviedDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    update_self_service_approval_recevied_dto = buybtcpay.UpdateSelfServiceApprovalReceviedDto() # UpdateSelfServiceApprovalReceviedDto | 

    try:
        # 更新自助充值审批单用户是否已经收款
        api_response = api_instance.update_self_service_approval_recevied(update_self_service_approval_recevied_dto)
        print("The response of OpenApprovalApi->update_self_service_approval_recevied:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->update_self_service_approval_recevied: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_self_service_approval_recevied_dto** | [**UpdateSelfServiceApprovalReceviedDto**](UpdateSelfServiceApprovalReceviedDto.md)|  | 

### Return type

[**BuyBtcResponseBoolean**](BuyBtcResponseBoolean.md)

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

# **update_self_service_approval_submited**
> BuyBtcResponseApprovalEntity update_self_service_approval_submited(self_service_approval_submited_dto)

更新自助充值审批单用户是否已经转账

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_approval_entity import BuyBtcResponseApprovalEntity
from buybtcpay.models.self_service_approval_submited_dto import SelfServiceApprovalSubmitedDto
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
    api_instance = buybtcpay.OpenApprovalApi(api_client)
    self_service_approval_submited_dto = buybtcpay.SelfServiceApprovalSubmitedDto() # SelfServiceApprovalSubmitedDto | 

    try:
        # 更新自助充值审批单用户是否已经转账
        api_response = api_instance.update_self_service_approval_submited(self_service_approval_submited_dto)
        print("The response of OpenApprovalApi->update_self_service_approval_submited:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenApprovalApi->update_self_service_approval_submited: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_service_approval_submited_dto** | [**SelfServiceApprovalSubmitedDto**](SelfServiceApprovalSubmitedDto.md)|  | 

### Return type

[**BuyBtcResponseApprovalEntity**](BuyBtcResponseApprovalEntity.md)

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

