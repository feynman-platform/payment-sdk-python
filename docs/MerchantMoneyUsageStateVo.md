# MerchantMoneyUsageStateVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**count** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_money_usage_state_vo import MerchantMoneyUsageStateVo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantMoneyUsageStateVo from a JSON string
merchant_money_usage_state_vo_instance = MerchantMoneyUsageStateVo.from_json(json)
# print the JSON string representation of the object
print(MerchantMoneyUsageStateVo.to_json())

# convert the object into a dict
merchant_money_usage_state_vo_dict = merchant_money_usage_state_vo_instance.to_dict()
# create an instance of MerchantMoneyUsageStateVo from a dict
merchant_money_usage_state_vo_from_dict = MerchantMoneyUsageStateVo.from_dict(merchant_money_usage_state_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


