# UpdateSelfServiceApprovalReceivedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**received** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.update_self_service_approval_received_dto import UpdateSelfServiceApprovalReceivedDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSelfServiceApprovalReceivedDto from a JSON string
update_self_service_approval_received_dto_instance = UpdateSelfServiceApprovalReceivedDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSelfServiceApprovalReceivedDto.to_json())

# convert the object into a dict
update_self_service_approval_received_dto_dict = update_self_service_approval_received_dto_instance.to_dict()
# create an instance of UpdateSelfServiceApprovalReceivedDto from a dict
update_self_service_approval_received_dto_from_dict = UpdateSelfServiceApprovalReceivedDto.from_dict(update_self_service_approval_received_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


