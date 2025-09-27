# MerchantWalletCountQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **List[str]** |  | [optional] 
**currency** | **str** | 货币类型 | [optional] 

## Example

```python
from buybtcpay.models.merchant_wallet_count_query import MerchantWalletCountQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWalletCountQuery from a JSON string
merchant_wallet_count_query_instance = MerchantWalletCountQuery.from_json(json)
# print the JSON string representation of the object
print(MerchantWalletCountQuery.to_json())

# convert the object into a dict
merchant_wallet_count_query_dict = merchant_wallet_count_query_instance.to_dict()
# create an instance of MerchantWalletCountQuery from a dict
merchant_wallet_count_query_from_dict = MerchantWalletCountQuery.from_dict(merchant_wallet_count_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


