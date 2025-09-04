# BuyBtcResponseMerchantEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantEntityDto**](MerchantEntityDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_entity_dto import BuyBtcResponseMerchantEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantEntityDto from a JSON string
buy_btc_response_merchant_entity_dto_instance = BuyBtcResponseMerchantEntityDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantEntityDto.to_json())

# convert the object into a dict
buy_btc_response_merchant_entity_dto_dict = buy_btc_response_merchant_entity_dto_instance.to_dict()
# create an instance of BuyBtcResponseMerchantEntityDto from a dict
buy_btc_response_merchant_entity_dto_from_dict = BuyBtcResponseMerchantEntityDto.from_dict(buy_btc_response_merchant_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


