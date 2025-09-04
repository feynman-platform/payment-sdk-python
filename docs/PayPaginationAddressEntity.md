# PayPaginationAddressEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[AddressEntity]**](AddressEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_address_entity import PayPaginationAddressEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationAddressEntity from a JSON string
pay_pagination_address_entity_instance = PayPaginationAddressEntity.from_json(json)
# print the JSON string representation of the object
print(PayPaginationAddressEntity.to_json())

# convert the object into a dict
pay_pagination_address_entity_dict = pay_pagination_address_entity_instance.to_dict()
# create an instance of PayPaginationAddressEntity from a dict
pay_pagination_address_entity_from_dict = PayPaginationAddressEntity.from_dict(pay_pagination_address_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


