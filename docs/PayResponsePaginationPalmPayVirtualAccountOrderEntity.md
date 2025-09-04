# PayResponsePaginationPalmPayVirtualAccountOrderEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationPalmPayVirtualAccountOrderEntity**](PayPaginationPalmPayVirtualAccountOrderEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_palm_pay_virtual_account_order_entity import PayResponsePaginationPalmPayVirtualAccountOrderEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationPalmPayVirtualAccountOrderEntity from a JSON string
pay_response_pagination_palm_pay_virtual_account_order_entity_instance = PayResponsePaginationPalmPayVirtualAccountOrderEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationPalmPayVirtualAccountOrderEntity.to_json())

# convert the object into a dict
pay_response_pagination_palm_pay_virtual_account_order_entity_dict = pay_response_pagination_palm_pay_virtual_account_order_entity_instance.to_dict()
# create an instance of PayResponsePaginationPalmPayVirtualAccountOrderEntity from a dict
pay_response_pagination_palm_pay_virtual_account_order_entity_from_dict = PayResponsePaginationPalmPayVirtualAccountOrderEntity.from_dict(pay_response_pagination_palm_pay_virtual_account_order_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


