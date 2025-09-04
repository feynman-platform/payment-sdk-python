# MerchantMoneyStateVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ngn** | [**List[MerchantMoneyUsageStateVo]**](MerchantMoneyUsageStateVo.md) |  | [optional] 
**ghs** | [**List[MerchantMoneyUsageStateVo]**](MerchantMoneyUsageStateVo.md) |  | [optional] 
**usdt** | [**List[MerchantMoneyUsageStateVo]**](MerchantMoneyUsageStateVo.md) |  | [optional] 
**payout** | [**List[CountPayoutDto]**](CountPayoutDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_money_state_vo import MerchantMoneyStateVo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantMoneyStateVo from a JSON string
merchant_money_state_vo_instance = MerchantMoneyStateVo.from_json(json)
# print the JSON string representation of the object
print(MerchantMoneyStateVo.to_json())

# convert the object into a dict
merchant_money_state_vo_dict = merchant_money_state_vo_instance.to_dict()
# create an instance of MerchantMoneyStateVo from a dict
merchant_money_state_vo_from_dict = MerchantMoneyStateVo.from_dict(merchant_money_state_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


