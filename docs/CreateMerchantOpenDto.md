# CreateMerchantOpenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_time** | **str** | 请注意，此处是字符类型，不是数值 | 
**version** | **str** | 保留字段，暂时无用 | 
**nonce** | **str** | 最大32位，用于防止重放攻击 | 
**name** | **str** |  | 
**email** | **str** |  | 
**tag** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.create_merchant_open_dto import CreateMerchantOpenDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMerchantOpenDto from a JSON string
create_merchant_open_dto_instance = CreateMerchantOpenDto.from_json(json)
# print the JSON string representation of the object
print(CreateMerchantOpenDto.to_json())

# convert the object into a dict
create_merchant_open_dto_dict = create_merchant_open_dto_instance.to_dict()
# create an instance of CreateMerchantOpenDto from a dict
create_merchant_open_dto_from_dict = CreateMerchantOpenDto.from_dict(create_merchant_open_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


