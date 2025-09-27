# CreateFrozenApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | 货币标准计量单位，注意，此处是字符类型 | 
**wallet_id** | **str** | 商户钱包ID | 
**note** | **str** | 可选 | [optional] 
**dmerchant_id** | **str** |  | [optional] 
**dcurrency_type** | **str** | 货币类型 | [optional] 

## Example

```python
from buybtcpay.models.create_frozen_approval_dto import CreateFrozenApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFrozenApprovalDto from a JSON string
create_frozen_approval_dto_instance = CreateFrozenApprovalDto.from_json(json)
# print the JSON string representation of the object
print(CreateFrozenApprovalDto.to_json())

# convert the object into a dict
create_frozen_approval_dto_dict = create_frozen_approval_dto_instance.to_dict()
# create an instance of CreateFrozenApprovalDto from a dict
create_frozen_approval_dto_from_dict = CreateFrozenApprovalDto.from_dict(create_frozen_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


