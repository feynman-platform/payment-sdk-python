# PayResponsePaginationPayoutResponseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationPayoutResponseEntity**](PayPaginationPayoutResponseEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_payout_response_entity import PayResponsePaginationPayoutResponseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationPayoutResponseEntity from a JSON string
pay_response_pagination_payout_response_entity_instance = PayResponsePaginationPayoutResponseEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationPayoutResponseEntity.to_json())

# convert the object into a dict
pay_response_pagination_payout_response_entity_dict = pay_response_pagination_payout_response_entity_instance.to_dict()
# create an instance of PayResponsePaginationPayoutResponseEntity from a dict
pay_response_pagination_payout_response_entity_from_dict = PayResponsePaginationPayoutResponseEntity.from_dict(pay_response_pagination_payout_response_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


