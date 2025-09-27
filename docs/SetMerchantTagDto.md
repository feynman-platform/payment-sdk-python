# SetMerchantTagDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | 商户ID | 
**tag** | **str** |  | 

## Example

```python
from buybtcpay.models.set_merchant_tag_dto import SetMerchantTagDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetMerchantTagDto from a JSON string
set_merchant_tag_dto_instance = SetMerchantTagDto.from_json(json)
# print the JSON string representation of the object
print(SetMerchantTagDto.to_json())

# convert the object into a dict
set_merchant_tag_dto_dict = set_merchant_tag_dto_instance.to_dict()
# create an instance of SetMerchantTagDto from a dict
set_merchant_tag_dto_from_dict = SetMerchantTagDto.from_dict(set_merchant_tag_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


