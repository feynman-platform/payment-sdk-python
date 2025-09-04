# PayPaginationPalmPayVirtualAccountOrderEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[PalmPayVirtualAccountOrderEntity]**](PalmPayVirtualAccountOrderEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_palm_pay_virtual_account_order_entity import PayPaginationPalmPayVirtualAccountOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationPalmPayVirtualAccountOrderEntity from a JSON string
pay_pagination_palm_pay_virtual_account_order_entity_instance = PayPaginationPalmPayVirtualAccountOrderEntity.from_json(json)
# print the JSON string representation of the object
print(PayPaginationPalmPayVirtualAccountOrderEntity.to_json())

# convert the object into a dict
pay_pagination_palm_pay_virtual_account_order_entity_dict = pay_pagination_palm_pay_virtual_account_order_entity_instance.to_dict()
# create an instance of PayPaginationPalmPayVirtualAccountOrderEntity from a dict
pay_pagination_palm_pay_virtual_account_order_entity_from_dict = PayPaginationPalmPayVirtualAccountOrderEntity.from_dict(pay_pagination_palm_pay_virtual_account_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


