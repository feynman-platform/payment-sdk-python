# CreateReversalWalletToWalletApprovalDto

冲销：钱包到钱包

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_wallet_id** | **str** |  | 
**payee_wallet_id** | **str** |  | 
**amount** | **str** | 货币标准计量单位，注意，此处是字符类型。金额不能大于商户的充值金额 | 
**note** | **str** | 可选 | [optional] 

## Example

```python
from buybtcpay.models.create_reversal_wallet_to_wallet_approval_dto import CreateReversalWalletToWalletApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReversalWalletToWalletApprovalDto from a JSON string
create_reversal_wallet_to_wallet_approval_dto_instance = CreateReversalWalletToWalletApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateReversalWalletToWalletApprovalDto.to_json())

# convert the object into a dict
create_reversal_wallet_to_wallet_approval_dto_dict = create_reversal_wallet_to_wallet_approval_dto_instance.to_dict()
# create an instance of CreateReversalWalletToWalletApprovalDto from a dict
create_reversal_wallet_to_wallet_approval_dto_from_dict = CreateReversalWalletToWalletApprovalDto.from_dict(create_reversal_wallet_to_wallet_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


