# PalmPayNotifyEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**status** | **int** | 0: NORMAL, 1: DELETE | [optional] 
**merchant_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 
**order_status** | **int** | 0: UNPAID, 1: PAYING, 2: SUCCESS, 3: FAIL, 4: CLOSE, 20: REFUNDED | [optional] 
**complete_time** | **datetime** |  | [optional] 
**error_code** | **str** |  | [optional] 
**sign** | **str** |  | [optional] 
**payer_bank_code** | **str** |  | [optional] 
**payer_bank_name** | **str** |  | [optional] 
**payer_account_no** | **str** |  | [optional] 
**payer_account_name** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_notify_entity import PalmPayNotifyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayNotifyEntity from a JSON string
palm_pay_notify_entity_instance = PalmPayNotifyEntity.from_json(json)
# print the JSON string representation of the object
print(PalmPayNotifyEntity.to_json())

# convert the object into a dict
palm_pay_notify_entity_dict = palm_pay_notify_entity_instance.to_dict()
# create an instance of PalmPayNotifyEntity from a dict
palm_pay_notify_entity_from_dict = PalmPayNotifyEntity.from_dict(palm_pay_notify_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


