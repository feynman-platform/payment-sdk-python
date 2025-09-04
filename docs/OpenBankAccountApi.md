# buybtcpay.OpenBankAccountApi

All URIs are relative to *http://localhost:9030*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_bank_account**](OpenBankAccountApi.md#query_bank_account) | **POST** /v1/open/bank/account/query | 查询银行账户信息


# **query_bank_account**
> BuyBtcResponseBankAccountDto query_bank_account(query_bank_account_dto)

查询银行账户信息

根据银行卡号和银行代码查询银行账户信息

### Example


```python
import buybtcpay
from buybtcpay.models.buy_btc_response_bank_account_dto import BuyBtcResponseBankAccountDto
from buybtcpay.models.query_bank_account_dto import QueryBankAccountDto
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
    api_instance = buybtcpay.OpenBankAccountApi(api_client)
    query_bank_account_dto = buybtcpay.QueryBankAccountDto() # QueryBankAccountDto | 

    try:
        # 查询银行账户信息
        api_response = api_instance.query_bank_account(query_bank_account_dto)
        print("The response of OpenBankAccountApi->query_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenBankAccountApi->query_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_bank_account_dto** | [**QueryBankAccountDto**](QueryBankAccountDto.md)|  | 

### Return type

[**BuyBtcResponseBankAccountDto**](BuyBtcResponseBankAccountDto.md)

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

