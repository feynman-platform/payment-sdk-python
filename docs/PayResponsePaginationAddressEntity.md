# PayResponsePaginationAddressEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationAddressEntity**](PayPaginationAddressEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_address_entity import PayResponsePaginationAddressEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationAddressEntity from a JSON string
pay_response_pagination_address_entity_instance = PayResponsePaginationAddressEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationAddressEntity.to_json())

# convert the object into a dict
pay_response_pagination_address_entity_dict = pay_response_pagination_address_entity_instance.to_dict()
# create an instance of PayResponsePaginationAddressEntity from a dict
pay_response_pagination_address_entity_from_dict = PayResponsePaginationAddressEntity.from_dict(pay_response_pagination_address_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


