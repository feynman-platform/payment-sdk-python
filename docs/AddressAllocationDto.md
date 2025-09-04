# AddressAllocationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 主键ID | [optional] 
**recharge_approval_id** | **int** | 绑定的充值审批id | [optional] 

## Example

```python
from buybtcpay.models.address_allocation_dto import AddressAllocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddressAllocationDto from a JSON string
address_allocation_dto_instance = AddressAllocationDto.from_json(json)
# print the JSON string representation of the object
print(AddressAllocationDto.to_json())

# convert the object into a dict
address_allocation_dto_dict = address_allocation_dto_instance.to_dict()
# create an instance of AddressAllocationDto from a dict
address_allocation_dto_from_dict = AddressAllocationDto.from_dict(address_allocation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


