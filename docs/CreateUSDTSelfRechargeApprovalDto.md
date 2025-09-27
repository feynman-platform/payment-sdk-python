# CreateUSDTSelfRechargeApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_amount** | **str** |  | 
**exchange_rate_id** | **str** | 源币种兑换目标币种的汇率ID，不用填，由系统设置 | [optional] 
**exchange_rate** | **str** | 源币种兑换目标币种的汇率，不用填，由系统设置 | [optional] 
**exchange_rate_source** | **str** | 币种汇率来源 | [optional] 
**payee_wallet_address** | **str** | 不用填，由系统自动生成 | [optional] 
**target_amount** | **str** | 不用填，由系统自动计算 | [optional] 
**amount** | **str** | 根据汇率计算出最终金额，单位为对应币种的最小单位，不用填，由系统自动计算 | [optional] 
**wallet_id** | **str** | 目前要求是资金账户 | 
**note** | **str** |  | [optional] 
**timeout** | **int** | 审批单超时时间，超过时间后自动关闭，单位秒 | [optional] 
**user_submitted** | **bool** |  | [optional] 
**received** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.create_usdt_self_recharge_approval_dto import CreateUSDTSelfRechargeApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUSDTSelfRechargeApprovalDto from a JSON string
create_usdt_self_recharge_approval_dto_instance = CreateUSDTSelfRechargeApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateUSDTSelfRechargeApprovalDto.to_json())

# convert the object into a dict
create_usdt_self_recharge_approval_dto_dict = create_usdt_self_recharge_approval_dto_instance.to_dict()
# create an instance of CreateUSDTSelfRechargeApprovalDto from a dict
create_usdt_self_recharge_approval_dto_from_dict = CreateUSDTSelfRechargeApprovalDto.from_dict(create_usdt_self_recharge_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


