# PalmPayVirtualAccountQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**virtual_account_name** | **str** |  | [optional] 
**virtual_account_no** | **str** |  | [optional] 
**account_status** | **str** |  | [optional] 
**identity_type** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_virtual_account_query import PalmPayVirtualAccountQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayVirtualAccountQuery from a JSON string
palm_pay_virtual_account_query_instance = PalmPayVirtualAccountQuery.from_json(json)
# print the JSON string representation of the object
print(PalmPayVirtualAccountQuery.to_json())

# convert the object into a dict
palm_pay_virtual_account_query_dict = palm_pay_virtual_account_query_instance.to_dict()
# create an instance of PalmPayVirtualAccountQuery from a dict
palm_pay_virtual_account_query_from_dict = PalmPayVirtualAccountQuery.from_dict(palm_pay_virtual_account_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


