# PayPaginationMerchantEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[MerchantEntityDto]**](MerchantEntityDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_merchant_entity_dto import PayPaginationMerchantEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationMerchantEntityDto from a JSON string
pay_pagination_merchant_entity_dto_instance = PayPaginationMerchantEntityDto.from_json(json)
# print the JSON string representation of the object
print(PayPaginationMerchantEntityDto.to_json())

# convert the object into a dict
pay_pagination_merchant_entity_dto_dict = pay_pagination_merchant_entity_dto_instance.to_dict()
# create an instance of PayPaginationMerchantEntityDto from a dict
pay_pagination_merchant_entity_dto_from_dict = PayPaginationMerchantEntityDto.from_dict(pay_pagination_merchant_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


