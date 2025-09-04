# PalmPayVirtualAccountEntity

PalmPay虚拟账户

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**virtual_account_name** | **str** | 账户名称 | [optional] 
**virtual_account_no** | **str** | 账号 | [optional] 
**account_status** | **str** | Disabled: DISABLED, Enabled: ENABLED, Deleted: DELETED | [optional] 
**identity_type** | **str** | personal: PERSIONAL, company: COMPANY | [optional] 
**license_number** | **str** | 证件号码 | [optional] 
**email** | **str** | 使用者邮箱 | [optional] 
**customer_name** | **str** | 使用者姓名 | [optional] 
**account_reference** | **str** | 备注 | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_virtual_account_entity import PalmPayVirtualAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayVirtualAccountEntity from a JSON string
palm_pay_virtual_account_entity_instance = PalmPayVirtualAccountEntity.from_json(json)
# print the JSON string representation of the object
print(PalmPayVirtualAccountEntity.to_json())

# convert the object into a dict
palm_pay_virtual_account_entity_dict = palm_pay_virtual_account_entity_instance.to_dict()
# create an instance of PalmPayVirtualAccountEntity from a dict
palm_pay_virtual_account_entity_from_dict = PalmPayVirtualAccountEntity.from_dict(palm_pay_virtual_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


