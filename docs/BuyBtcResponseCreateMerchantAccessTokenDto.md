# BuyBtcResponseCreateMerchantAccessTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**CreateMerchantAccessTokenDto**](CreateMerchantAccessTokenDto.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_create_merchant_access_token_dto import BuyBtcResponseCreateMerchantAccessTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseCreateMerchantAccessTokenDto from a JSON string
buy_btc_response_create_merchant_access_token_dto_instance = BuyBtcResponseCreateMerchantAccessTokenDto.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseCreateMerchantAccessTokenDto.to_json())

# convert the object into a dict
buy_btc_response_create_merchant_access_token_dto_dict = buy_btc_response_create_merchant_access_token_dto_instance.to_dict()
# create an instance of BuyBtcResponseCreateMerchantAccessTokenDto from a dict
buy_btc_response_create_merchant_access_token_dto_from_dict = BuyBtcResponseCreateMerchantAccessTokenDto.from_dict(buy_btc_response_create_merchant_access_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


