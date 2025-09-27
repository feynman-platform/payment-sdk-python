# MerchantWalletCountVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **str** |  | [optional] 
**frozen** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_wallet_count_vo import MerchantWalletCountVo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWalletCountVo from a JSON string
merchant_wallet_count_vo_instance = MerchantWalletCountVo.from_json(json)
# print the JSON string representation of the object
print(MerchantWalletCountVo.to_json())

# convert the object into a dict
merchant_wallet_count_vo_dict = merchant_wallet_count_vo_instance.to_dict()
# create an instance of MerchantWalletCountVo from a dict
merchant_wallet_count_vo_from_dict = MerchantWalletCountVo.from_dict(merchant_wallet_count_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


