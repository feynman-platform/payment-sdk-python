# PayResponsePaginationApprovalEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationApprovalEntity**](PayPaginationApprovalEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_approval_entity import PayResponsePaginationApprovalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationApprovalEntity from a JSON string
pay_response_pagination_approval_entity_instance = PayResponsePaginationApprovalEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationApprovalEntity.to_json())

# convert the object into a dict
pay_response_pagination_approval_entity_dict = pay_response_pagination_approval_entity_instance.to_dict()
# create an instance of PayResponsePaginationApprovalEntity from a dict
pay_response_pagination_approval_entity_from_dict = PayResponsePaginationApprovalEntity.from_dict(pay_response_pagination_approval_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


