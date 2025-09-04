# PayResponsePaginationPayoutEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationPayoutEntityDto**](PayPaginationPayoutEntityDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_payout_entity_dto import PayResponsePaginationPayoutEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationPayoutEntityDto from a JSON string
pay_response_pagination_payout_entity_dto_instance = PayResponsePaginationPayoutEntityDto.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationPayoutEntityDto.to_json())

# convert the object into a dict
pay_response_pagination_payout_entity_dto_dict = pay_response_pagination_payout_entity_dto_instance.to_dict()
# create an instance of PayResponsePaginationPayoutEntityDto from a dict
pay_response_pagination_payout_entity_dto_from_dict = PayResponsePaginationPayoutEntityDto.from_dict(pay_response_pagination_payout_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


