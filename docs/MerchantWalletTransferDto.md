# MerchantWalletTransferDto

商户自己的不同类型的钱包互转，要求同币种

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_wallet_id** | **str** | 转出钱包ID | 
**to_wallet_id** | **str** | 转入钱包DI | 
**amount** | **str** | 交易金额 | 

## Example

```python
from buybtcpay.models.merchant_wallet_transfer_dto import MerchantWalletTransferDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWalletTransferDto from a JSON string
merchant_wallet_transfer_dto_instance = MerchantWalletTransferDto.from_json(json)
# print the JSON string representation of the object
print(MerchantWalletTransferDto.to_json())

# convert the object into a dict
merchant_wallet_transfer_dto_dict = merchant_wallet_transfer_dto_instance.to_dict()
# create an instance of MerchantWalletTransferDto from a dict
merchant_wallet_transfer_dto_from_dict = MerchantWalletTransferDto.from_dict(merchant_wallet_transfer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


