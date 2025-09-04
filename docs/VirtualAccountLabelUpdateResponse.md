# VirtualAccountLabelUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp_code** | **str** |  | [optional] 
**resp_msg** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.virtual_account_label_update_response import VirtualAccountLabelUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountLabelUpdateResponse from a JSON string
virtual_account_label_update_response_instance = VirtualAccountLabelUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountLabelUpdateResponse.to_json())

# convert the object into a dict
virtual_account_label_update_response_dict = virtual_account_label_update_response_instance.to_dict()
# create an instance of VirtualAccountLabelUpdateResponse from a dict
virtual_account_label_update_response_from_dict = VirtualAccountLabelUpdateResponse.from_dict(virtual_account_label_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


