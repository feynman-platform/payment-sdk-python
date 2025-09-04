# ProcessingApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**approval_status** | **str** | 审批状态 | 
**approval_comment** | **str** |  | 

## Example

```python
from buybtcpay.models.processing_approval_dto import ProcessingApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingApprovalDto from a JSON string
processing_approval_dto_instance = ProcessingApprovalDto.from_json(json)
# print the JSON string representation of the object
print(ProcessingApprovalDto.to_json())

# convert the object into a dict
processing_approval_dto_dict = processing_approval_dto_instance.to_dict()
# create an instance of ProcessingApprovalDto from a dict
processing_approval_dto_from_dict = ProcessingApprovalDto.from_dict(processing_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


