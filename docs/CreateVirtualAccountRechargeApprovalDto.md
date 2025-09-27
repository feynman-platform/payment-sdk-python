# CreateVirtualAccountRechargeApprovalDto

如果主商户资金账户余额不够，则无法充值

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | 货币标准计量单位，注意，此处是字符类型 | 
**currency_type** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**wallet_id** | **str** | 商户钱包ID，要求为资金账户 | 
**note** | **str** | 可选 | [optional] 
**dmerchant_id** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.create_virtual_account_recharge_approval_dto import CreateVirtualAccountRechargeApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVirtualAccountRechargeApprovalDto from a JSON string
create_virtual_account_recharge_approval_dto_instance = CreateVirtualAccountRechargeApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateVirtualAccountRechargeApprovalDto.to_json())

# convert the object into a dict
create_virtual_account_recharge_approval_dto_dict = create_virtual_account_recharge_approval_dto_instance.to_dict()
# create an instance of CreateVirtualAccountRechargeApprovalDto from a dict
create_virtual_account_recharge_approval_dto_from_dict = CreateVirtualAccountRechargeApprovalDto.from_dict(create_virtual_account_recharge_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


