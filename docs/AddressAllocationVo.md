# AddressAllocationVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 主键ID | [optional] 
**address** | **str** | 分配的地址 | [optional] 
**amount** | **float** | 原始金额 | [optional] 
**tag_amount** | **float** | 标识金额 | [optional] 
**recharge_approval_id** | **int** | 绑定的充值审批id | [optional] 

## Example

```python
from buybtcpay.models.address_allocation_vo import AddressAllocationVo

# TODO update the JSON string below
json = "{}"
# create an instance of AddressAllocationVo from a JSON string
address_allocation_vo_instance = AddressAllocationVo.from_json(json)
# print the JSON string representation of the object
print(AddressAllocationVo.to_json())

# convert the object into a dict
address_allocation_vo_dict = address_allocation_vo_instance.to_dict()
# create an instance of AddressAllocationVo from a dict
address_allocation_vo_from_dict = AddressAllocationVo.from_dict(address_allocation_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


