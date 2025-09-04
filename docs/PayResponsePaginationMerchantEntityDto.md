# PayResponsePaginationMerchantEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationMerchantEntityDto**](PayPaginationMerchantEntityDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_merchant_entity_dto import PayResponsePaginationMerchantEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationMerchantEntityDto from a JSON string
pay_response_pagination_merchant_entity_dto_instance = PayResponsePaginationMerchantEntityDto.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationMerchantEntityDto.to_json())

# convert the object into a dict
pay_response_pagination_merchant_entity_dto_dict = pay_response_pagination_merchant_entity_dto_instance.to_dict()
# create an instance of PayResponsePaginationMerchantEntityDto from a dict
pay_response_pagination_merchant_entity_dto_from_dict = PayResponsePaginationMerchantEntityDto.from_dict(pay_response_pagination_merchant_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


