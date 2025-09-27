# MerchantWalletQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**currency** | **str** | 货币类型 | [optional] 
**tag** | **List[str]** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_wallet_query import MerchantWalletQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWalletQuery from a JSON string
merchant_wallet_query_instance = MerchantWalletQuery.from_json(json)
# print the JSON string representation of the object
print(MerchantWalletQuery.to_json())

# convert the object into a dict
merchant_wallet_query_dict = merchant_wallet_query_instance.to_dict()
# create an instance of MerchantWalletQuery from a dict
merchant_wallet_query_from_dict = MerchantWalletQuery.from_dict(merchant_wallet_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


