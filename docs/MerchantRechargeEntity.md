# MerchantRechargeEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**approval_status** | **int** | 0: Awaiting Approval, 1: Approved, 2: Rejected, 3: Canceled | [optional] 
**merchant** | [**MerchantEntity**](MerchantEntity.md) |  | [optional] 
**value** | **int** |  | [optional] 
**note** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**approval_time** | **datetime** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_recharge_entity import MerchantRechargeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantRechargeEntity from a JSON string
merchant_recharge_entity_instance = MerchantRechargeEntity.from_json(json)
# print the JSON string representation of the object
print(MerchantRechargeEntity.to_json())

# convert the object into a dict
merchant_recharge_entity_dict = merchant_recharge_entity_instance.to_dict()
# create an instance of MerchantRechargeEntity from a dict
merchant_recharge_entity_from_dict = MerchantRechargeEntity.from_dict(merchant_recharge_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


