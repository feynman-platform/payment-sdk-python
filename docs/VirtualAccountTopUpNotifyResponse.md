# VirtualAccountTopUpNotifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**created_time** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**order_amount** | **int** |  | [optional] 
**reference** | **str** |  | [optional] 
**payer_account_no** | **str** |  | [optional] 
**payer_account_name** | **str** |  | [optional] 
**payer_bank_name** | **str** |  | [optional] 
**virtual_account_no** | **str** |  | [optional] 
**virtual_account_name** | **str** |  | [optional] 
**account_reference** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**sign** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.virtual_account_top_up_notify_response import VirtualAccountTopUpNotifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountTopUpNotifyResponse from a JSON string
virtual_account_top_up_notify_response_instance = VirtualAccountTopUpNotifyResponse.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountTopUpNotifyResponse.to_json())

# convert the object into a dict
virtual_account_top_up_notify_response_dict = virtual_account_top_up_notify_response_instance.to_dict()
# create an instance of VirtualAccountTopUpNotifyResponse from a dict
virtual_account_top_up_notify_response_from_dict = VirtualAccountTopUpNotifyResponse.from_dict(virtual_account_top_up_notify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


