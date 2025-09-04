# CreateMerchantRechargeApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | 货币标准计量单位，注意，此处是字符类型 | 
**currency_type** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**merchant_id** | **str** | 商户ID | 
**note** | **str** | 可选 | [optional] 

## Example

```python
from buybtcpay.models.create_merchant_recharge_approval_dto import CreateMerchantRechargeApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantRechargeApprovalDto from a JSON string
create_merchant_recharge_approval_dto_instance = CreateMerchantRechargeApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateMerchantRechargeApprovalDto.to_json())

# convert the object into a dict
create_merchant_recharge_approval_dto_dict = create_merchant_recharge_approval_dto_instance.to_dict()
# create an instance of CreateMerchantRechargeApprovalDto from a dict
create_merchant_recharge_approval_dto_from_dict = CreateMerchantRechargeApprovalDto.from_dict(create_merchant_recharge_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


