# CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicant_id** | **str** | 不用填，系统会根据请求用户自己设定 | [optional] 
**business_id** | **str** |  | [optional] 
**approval_type** | **int** | 0: Platform Recharge, 1: Merchant Recharge, 11: Virtual Account Recharge, 12: Merchant Self Service Recharge, 13: Virtual Account Self Service Recharge, 14: Merchant Self Service Recharge by PalmPay Virtual Account, 15: Virtual erchant Self Service Recharge by PalmPay Virtual Account, 2: Refund, 3: Frozen, 4: Unfrozen, 100: Reversal platform to merchant, 101: Reversal merchant to platform, 102: Reversal merchant to merchant | 
**content** | [**CreateVirtualAccountRechargeApprovalDto**](CreateVirtualAccountRechargeApprovalDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.create_approval_dto_create_virtual_account_recharge_approval_dto import CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto from a JSON string
create_approval_dto_create_virtual_account_recharge_approval_dto_instance = CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto.to_json())

# convert the object into a dict
create_approval_dto_create_virtual_account_recharge_approval_dto_dict = create_approval_dto_create_virtual_account_recharge_approval_dto_instance.to_dict()
# create an instance of CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto from a dict
create_approval_dto_create_virtual_account_recharge_approval_dto_from_dict = CreateApprovalDtoCreateVirtualAccountRechargeApprovalDto.from_dict(create_approval_dto_create_virtual_account_recharge_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


