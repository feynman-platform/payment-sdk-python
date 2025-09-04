# PayPaginationVirtualAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[VirtualAccountEntity]**](VirtualAccountEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_virtual_account_entity import PayPaginationVirtualAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationVirtualAccountEntity from a JSON string
pay_pagination_virtual_account_entity_instance = PayPaginationVirtualAccountEntity.from_json(json)
# print the JSON string representation of the object
print(PayPaginationVirtualAccountEntity.to_json())

# convert the object into a dict
pay_pagination_virtual_account_entity_dict = pay_pagination_virtual_account_entity_instance.to_dict()
# create an instance of PayPaginationVirtualAccountEntity from a dict
pay_pagination_virtual_account_entity_from_dict = PayPaginationVirtualAccountEntity.from_dict(pay_pagination_virtual_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


