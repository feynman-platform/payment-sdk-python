# UpdateSelfServiceApprovalReceviedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**received** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.update_self_service_approval_recevied_dto import UpdateSelfServiceApprovalReceviedDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSelfServiceApprovalReceviedDto from a JSON string
update_self_service_approval_recevied_dto_instance = UpdateSelfServiceApprovalReceviedDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSelfServiceApprovalReceviedDto.to_json())

# convert the object into a dict
update_self_service_approval_recevied_dto_dict = update_self_service_approval_recevied_dto_instance.to_dict()
# create an instance of UpdateSelfServiceApprovalReceviedDto from a dict
update_self_service_approval_recevied_dto_from_dict = UpdateSelfServiceApprovalReceviedDto.from_dict(update_self_service_approval_recevied_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


