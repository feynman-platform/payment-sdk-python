# PayPaginationPayoutEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[PayoutEntityDto]**](PayoutEntityDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_payout_entity_dto import PayPaginationPayoutEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationPayoutEntityDto from a JSON string
pay_pagination_payout_entity_dto_instance = PayPaginationPayoutEntityDto.from_json(json)
# print the JSON string representation of the object
print(PayPaginationPayoutEntityDto.to_json())

# convert the object into a dict
pay_pagination_payout_entity_dto_dict = pay_pagination_payout_entity_dto_instance.to_dict()
# create an instance of PayPaginationPayoutEntityDto from a dict
pay_pagination_payout_entity_dto_from_dict = PayPaginationPayoutEntityDto.from_dict(pay_pagination_payout_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


