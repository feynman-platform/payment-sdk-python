# CreateReversalPlatformToBankApprovalDto

冲销：平台到银行

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code** | **str** |  | 
**bank_account** | **str** | 收款银行账号 | 
**amount** | **str** |  | 
**currency_type** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**note** | **str** | 可选 | [optional] 

## Example

```python
from buybtcpay.models.create_reversal_platform_to_bank_approval_dto import CreateReversalPlatformToBankApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReversalPlatformToBankApprovalDto from a JSON string
create_reversal_platform_to_bank_approval_dto_instance = CreateReversalPlatformToBankApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateReversalPlatformToBankApprovalDto.to_json())

# convert the object into a dict
create_reversal_platform_to_bank_approval_dto_dict = create_reversal_platform_to_bank_approval_dto_instance.to_dict()
# create an instance of CreateReversalPlatformToBankApprovalDto from a dict
create_reversal_platform_to_bank_approval_dto_from_dict = CreateReversalPlatformToBankApprovalDto.from_dict(create_reversal_platform_to_bank_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


