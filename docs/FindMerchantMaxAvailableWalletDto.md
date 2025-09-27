# FindMerchantMaxAvailableWalletDto

查询商户可用余额最多的钱包请求参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | [optional] 
**currency** | **str** | 货币类型 | [optional] 
**wallet_type** | **str** | 钱包类型 | [optional] 

## Example

```python
from buybtcpay.models.find_merchant_max_available_wallet_dto import FindMerchantMaxAvailableWalletDto

# TODO update the JSON string below
json = "{}"
# create an instance of FindMerchantMaxAvailableWalletDto from a JSON string
find_merchant_max_available_wallet_dto_instance = FindMerchantMaxAvailableWalletDto.from_json(json)
# print the JSON string representation of the object
print(FindMerchantMaxAvailableWalletDto.to_json())

# convert the object into a dict
find_merchant_max_available_wallet_dto_dict = find_merchant_max_available_wallet_dto_instance.to_dict()
# create an instance of FindMerchantMaxAvailableWalletDto from a dict
find_merchant_max_available_wallet_dto_from_dict = FindMerchantMaxAvailableWalletDto.from_dict(find_merchant_max_available_wallet_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


