# ApproveDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from buybtcpay.models.approve_dto import ApproveDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveDto from a JSON string
approve_dto_instance = ApproveDto.from_json(json)
# print the JSON string representation of the object
print(ApproveDto.to_json())

# convert the object into a dict
approve_dto_dict = approve_dto_instance.to_dict()
# create an instance of ApproveDto from a dict
approve_dto_from_dict = ApproveDto.from_dict(approve_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


