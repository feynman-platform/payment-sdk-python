# CreateReversalPlatfromToMerchantApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | 向谁转账 | 
**amount** | **str** | 货币标准计量单位，注意，此处是字符类型。金额不能大于平台的充值金额 | 
**currency_type** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | 
**note** | **str** | 可选 | [optional] 

## Example

```python
from buybtcpay.models.create_reversal_platfrom_to_merchant_approval_dto import CreateReversalPlatfromToMerchantApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReversalPlatfromToMerchantApprovalDto from a JSON string
create_reversal_platfrom_to_merchant_approval_dto_instance = CreateReversalPlatfromToMerchantApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateReversalPlatfromToMerchantApprovalDto.to_json())

# convert the object into a dict
create_reversal_platfrom_to_merchant_approval_dto_dict = create_reversal_platfrom_to_merchant_approval_dto_instance.to_dict()
# create an instance of CreateReversalPlatfromToMerchantApprovalDto from a dict
create_reversal_platfrom_to_merchant_approval_dto_from_dict = CreateReversalPlatfromToMerchantApprovalDto.from_dict(create_reversal_platfrom_to_merchant_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


