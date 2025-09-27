# PayPaginationQueryMerchantWalletQuery

分页查询

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** | 当前页码 | [optional] 
**size** | **int** | 每页大小 | [optional] 
**query** | [**MerchantWalletQuery**](MerchantWalletQuery.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_query_merchant_wallet_query import PayPaginationQueryMerchantWalletQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationQueryMerchantWalletQuery from a JSON string
pay_pagination_query_merchant_wallet_query_instance = PayPaginationQueryMerchantWalletQuery.from_json(json)
# print the JSON string representation of the object
print(PayPaginationQueryMerchantWalletQuery.to_json())

# convert the object into a dict
pay_pagination_query_merchant_wallet_query_dict = pay_pagination_query_merchant_wallet_query_instance.to_dict()
# create an instance of PayPaginationQueryMerchantWalletQuery from a dict
pay_pagination_query_merchant_wallet_query_from_dict = PayPaginationQueryMerchantWalletQuery.from_dict(pay_pagination_query_merchant_wallet_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


