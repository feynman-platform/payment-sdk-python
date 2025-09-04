# VirtualAccountData

虚拟账号创建响应参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_account_name** | **str** | 虚拟账号名称 | 
**virtual_account_no** | **str** | 虚拟账号号码 | 
**status** | **str** | 虚拟账号状态 | 
**identity_type** | **str** | 使用者身份类型 | 
**license_number** | **str** | 证件号码 | [optional] 
**email** | **str** | 邮箱 | [optional] 
**customer_name** | **str** | 使用者名称 | [optional] 
**account_reference** | **str** | 虚拟账户备注字段 | [optional] 

## Example

```python
from buybtcpay.models.virtual_account_data import VirtualAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAccountData from a JSON string
virtual_account_data_instance = VirtualAccountData.from_json(json)
# print the JSON string representation of the object
print(VirtualAccountData.to_json())

# convert the object into a dict
virtual_account_data_dict = virtual_account_data_instance.to_dict()
# create an instance of VirtualAccountData from a dict
virtual_account_data_from_dict = VirtualAccountData.from_dict(virtual_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


