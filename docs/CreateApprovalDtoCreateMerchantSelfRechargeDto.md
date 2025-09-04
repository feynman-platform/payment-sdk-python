# CreateApprovalDtoCreateMerchantSelfRechargeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicant_id** | **str** | 不用填，系统会根据请求用户自己设定 | [optional] 
**business_id** | **str** |  | [optional] 
**approval_type** | **int** | 0: Platform Recharge, 1: Merchant Recharge, 11: Virtual Account Recharge, 12: Merchant Self Service Recharge, 13: Virtual Account Self Service Recharge, 14: Merchant Self Service Recharge by PalmPay Virtual Account, 15: Virtual erchant Self Service Recharge by PalmPay Virtual Account, 2: Refund, 3: Frozen, 4: Unfrozen, 100: Reversal platform to merchant, 101: Reversal merchant to platform, 102: Reversal merchant to merchant | 
**content** | [**CreateMerchantSelfRechargeDto**](CreateMerchantSelfRechargeDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.create_approval_dto_create_merchant_self_recharge_dto import CreateApprovalDtoCreateMerchantSelfRechargeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApprovalDtoCreateMerchantSelfRechargeDto from a JSON string
create_approval_dto_create_merchant_self_recharge_dto_instance = CreateApprovalDtoCreateMerchantSelfRechargeDto.from_json(json)
# print the JSON string representation of the object
print(CreateApprovalDtoCreateMerchantSelfRechargeDto.to_json())

# convert the object into a dict
create_approval_dto_create_merchant_self_recharge_dto_dict = create_approval_dto_create_merchant_self_recharge_dto_instance.to_dict()
# create an instance of CreateApprovalDtoCreateMerchantSelfRechargeDto from a dict
create_approval_dto_create_merchant_self_recharge_dto_from_dict = CreateApprovalDtoCreateMerchantSelfRechargeDto.from_dict(create_approval_dto_create_merchant_self_recharge_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


