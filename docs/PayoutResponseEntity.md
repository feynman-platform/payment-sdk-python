# PayoutResponseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**merchant_order_id** | **str** |  | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**order_status** | **int** | 0: UNPAID, 1: PAYING, 2: SUCCESS, 3: FAIL, 4: CLOSE, 20: REFUNDED | [optional] 
**session_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**error_msg** | **str** |  | [optional] 
**merchant_fee** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**resp_code** | **str** |  | [optional] 
**resp_msg** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.payout_response_entity import PayoutResponseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutResponseEntity from a JSON string
payout_response_entity_instance = PayoutResponseEntity.from_json(json)
# print the JSON string representation of the object
print(PayoutResponseEntity.to_json())

# convert the object into a dict
payout_response_entity_dict = payout_response_entity_instance.to_dict()
# create an instance of PayoutResponseEntity from a dict
payout_response_entity_from_dict = PayoutResponseEntity.from_dict(payout_response_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


