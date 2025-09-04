# CreateMerchantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**tag** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.create_merchant_dto import CreateMerchantDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantDto from a JSON string
create_merchant_dto_instance = CreateMerchantDto.from_json(json)
# print the JSON string representation of the object
print(CreateMerchantDto.to_json())

# convert the object into a dict
create_merchant_dto_dict = create_merchant_dto_instance.to_dict()
# create an instance of CreateMerchantDto from a dict
create_merchant_dto_from_dict = CreateMerchantDto.from_dict(create_merchant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


