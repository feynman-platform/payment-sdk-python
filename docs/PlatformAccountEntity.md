# PlatformAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**account_code** | **object** | 平台账户类型 | [optional] 
**account_name** | **str** |  | [optional] 
**balance** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.platform_account_entity import PlatformAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformAccountEntity from a JSON string
platform_account_entity_instance = PlatformAccountEntity.from_json(json)
# print the JSON string representation of the object
print(PlatformAccountEntity.to_json())

# convert the object into a dict
platform_account_entity_dict = platform_account_entity_instance.to_dict()
# create an instance of PlatformAccountEntity from a dict
platform_account_entity_from_dict = PlatformAccountEntity.from_dict(platform_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


