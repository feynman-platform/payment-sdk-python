# SendTopUpNotifyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**virtual_account_no** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.send_top_up_notify_dto import SendTopUpNotifyDto

# TODO update the JSON string below
json = "{}"
# create an instance of SendTopUpNotifyDto from a JSON string
send_top_up_notify_dto_instance = SendTopUpNotifyDto.from_json(json)
# print the JSON string representation of the object
print(SendTopUpNotifyDto.to_json())

# convert the object into a dict
send_top_up_notify_dto_dict = send_top_up_notify_dto_instance.to_dict()
# create an instance of SendTopUpNotifyDto from a dict
send_top_up_notify_dto_from_dict = SendTopUpNotifyDto.from_dict(send_top_up_notify_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


