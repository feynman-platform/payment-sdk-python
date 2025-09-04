# MerchantUpdateProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**tag** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.merchant_update_profile_dto import MerchantUpdateProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantUpdateProfileDto from a JSON string
merchant_update_profile_dto_instance = MerchantUpdateProfileDto.from_json(json)
# print the JSON string representation of the object
print(MerchantUpdateProfileDto.to_json())

# convert the object into a dict
merchant_update_profile_dto_dict = merchant_update_profile_dto_instance.to_dict()
# create an instance of MerchantUpdateProfileDto from a dict
merchant_update_profile_dto_from_dict = MerchantUpdateProfileDto.from_dict(merchant_update_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


