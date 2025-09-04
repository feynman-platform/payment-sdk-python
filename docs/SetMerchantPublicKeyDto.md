# SetMerchantPublicKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | 

## Example

```python
from buybtcpay.models.set_merchant_public_key_dto import SetMerchantPublicKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetMerchantPublicKeyDto from a JSON string
set_merchant_public_key_dto_instance = SetMerchantPublicKeyDto.from_json(json)
# print the JSON string representation of the object
print(SetMerchantPublicKeyDto.to_json())

# convert the object into a dict
set_merchant_public_key_dto_dict = set_merchant_public_key_dto_instance.to_dict()
# create an instance of SetMerchantPublicKeyDto from a dict
set_merchant_public_key_dto_from_dict = SetMerchantPublicKeyDto.from_dict(set_merchant_public_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


