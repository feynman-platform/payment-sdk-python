# CreateReversalWalletToPlatformApprovalDto

冲销：钱包到平台

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | 谁向平台转账 | 
**amount** | **str** | 货币标准计量单位，注意，此处是字符类型。金额不能大于商户的充值金额 | 
**note** | **str** | 可选 | [optional] 

## Example

```python
from buybtcpay.models.create_reversal_wallet_to_platform_approval_dto import CreateReversalWalletToPlatformApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReversalWalletToPlatformApprovalDto from a JSON string
create_reversal_wallet_to_platform_approval_dto_instance = CreateReversalWalletToPlatformApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateReversalWalletToPlatformApprovalDto.to_json())

# convert the object into a dict
create_reversal_wallet_to_platform_approval_dto_dict = create_reversal_wallet_to_platform_approval_dto_instance.to_dict()
# create an instance of CreateReversalWalletToPlatformApprovalDto from a dict
create_reversal_wallet_to_platform_approval_dto_from_dict = CreateReversalWalletToPlatformApprovalDto.from_dict(create_reversal_wallet_to_platform_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


