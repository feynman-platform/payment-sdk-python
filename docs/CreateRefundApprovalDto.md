# CreateRefundApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | 可选 | [optional] 
**damount** | **str** |  | [optional] 
**dcurrency_type** | **str** | 货币类型 | [optional] 

## Example

```python
from buybtcpay.models.create_refund_approval_dto import CreateRefundApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRefundApprovalDto from a JSON string
create_refund_approval_dto_instance = CreateRefundApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateRefundApprovalDto.to_json())

# convert the object into a dict
create_refund_approval_dto_dict = create_refund_approval_dto_instance.to_dict()
# create an instance of CreateRefundApprovalDto from a dict
create_refund_approval_dto_from_dict = CreateRefundApprovalDto.from_dict(create_refund_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


