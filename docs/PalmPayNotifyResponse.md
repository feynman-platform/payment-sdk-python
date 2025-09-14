# PalmPayNotifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**order_status** | **int** |  | [optional] 
**complete_time** | **int** |  | [optional] 
**error_code** | **str** |  | [optional] 
**sign** | **str** |  | [optional] 
**player** | [**PalmPayPlayer**](PalmPayPlayer.md) |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_notify_response import PalmPayNotifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayNotifyResponse from a JSON string
palm_pay_notify_response_instance = PalmPayNotifyResponse.from_json(json)
# print the JSON string representation of the object
print(PalmPayNotifyResponse.to_json())

# convert the object into a dict
palm_pay_notify_response_dict = palm_pay_notify_response_instance.to_dict()
# create an instance of PalmPayNotifyResponse from a dict
palm_pay_notify_response_from_dict = PalmPayNotifyResponse.from_dict(palm_pay_notify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


