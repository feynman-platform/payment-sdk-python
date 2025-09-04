# SelfServiceApprovalSubmitedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_id** | **str** | 审批单ID | [optional] 
**submited** | **bool** | 是否已经转账 | [optional] 

## Example

```python
from buybtcpay.models.self_service_approval_submited_dto import SelfServiceApprovalSubmitedDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServiceApprovalSubmitedDto from a JSON string
self_service_approval_submited_dto_instance = SelfServiceApprovalSubmitedDto.from_json(json)
# print the JSON string representation of the object
print(SelfServiceApprovalSubmitedDto.to_json())

# convert the object into a dict
self_service_approval_submited_dto_dict = self_service_approval_submited_dto_instance.to_dict()
# create an instance of SelfServiceApprovalSubmitedDto from a dict
self_service_approval_submited_dto_from_dict = SelfServiceApprovalSubmitedDto.from_dict(self_service_approval_submited_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


