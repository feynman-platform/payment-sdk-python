# TradeTransferAggregationDto

合并支付预付单，只支持商户到商户的支付

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**Verification**](Verification.md) |  | [optional] 
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**business_ids** | **List[str]** | 合并的预付单ID列表 | 
**new_business_id** | **str** | 新的业务ID | 
**payer** | **str** | 付款方，邮箱或merchantId | 
**payee** | **str** | 收款方，邮箱或merchantId | 
**payee_wallet_operator** | **str** | 收款方的钱包是谁在操作 | 
**operator** | **str** | 商户ID | 

## Example

```python
from buybtcpay.models.trade_transfer_aggregation_dto import TradeTransferAggregationDto

# TODO update the JSON string below
json = "{}"
# create an instance of TradeTransferAggregationDto from a JSON string
trade_transfer_aggregation_dto_instance = TradeTransferAggregationDto.from_json(json)
# print the JSON string representation of the object
print(TradeTransferAggregationDto.to_json())

# convert the object into a dict
trade_transfer_aggregation_dto_dict = trade_transfer_aggregation_dto_instance.to_dict()
# create an instance of TradeTransferAggregationDto from a dict
trade_transfer_aggregation_dto_from_dict = TradeTransferAggregationDto.from_dict(trade_transfer_aggregation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


