# CreateMerchantAccessTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.create_merchant_access_token_dto import CreateMerchantAccessTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantAccessTokenDto from a JSON string
create_merchant_access_token_dto_instance = CreateMerchantAccessTokenDto.from_json(json)
# print the JSON string representation of the object
print(CreateMerchantAccessTokenDto.to_json())

# convert the object into a dict
create_merchant_access_token_dto_dict = create_merchant_access_token_dto_instance.to_dict()
# create an instance of CreateMerchantAccessTokenDto from a dict
create_merchant_access_token_dto_from_dict = CreateMerchantAccessTokenDto.from_dict(create_merchant_access_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


