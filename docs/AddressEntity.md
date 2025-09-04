# AddressEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id | [optional] 
**create_at** | **datetime** | 创建时间 | [optional] 
**update_at** | **datetime** | 更新时间 | [optional] 
**is_del** | **int** | 是否删除 | [optional] 
**address** | **str** | 交易地址 | [optional] 

## Example

```python
from buybtcpay.models.address_entity import AddressEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddressEntity from a JSON string
address_entity_instance = AddressEntity.from_json(json)
# print the JSON string representation of the object
print(AddressEntity.to_json())

# convert the object into a dict
address_entity_dict = address_entity_instance.to_dict()
# create an instance of AddressEntity from a dict
address_entity_from_dict = AddressEntity.from_dict(address_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


