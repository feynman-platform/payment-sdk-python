# SendPayoutNotifyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | 
**currency** | **str** |  | 
**order_status** | **int** |  | 
**verify_code** | **str** |  | 

## Example

```python
from buybtcpay.models.send_payout_notify_dto import SendPayoutNotifyDto

# TODO update the JSON string below
json = "{}"
# create an instance of SendPayoutNotifyDto from a JSON string
send_payout_notify_dto_instance = SendPayoutNotifyDto.from_json(json)
# print the JSON string representation of the object
print(SendPayoutNotifyDto.to_json())

# convert the object into a dict
send_payout_notify_dto_dict = send_payout_notify_dto_instance.to_dict()
# create an instance of SendPayoutNotifyDto from a dict
send_payout_notify_dto_from_dict = SendPayoutNotifyDto.from_dict(send_payout_notify_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


