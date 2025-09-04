# PayoutOpenApiResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**amount** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**merchant_fee** | [**BuyBtcMoneyJsonValue**](BuyBtcMoneyJsonValue.md) |  | [optional] 
**order_status** | **int** | 0: UNPAID, 1: PAYING, 2: SUCCESS, 3: FAIL, 4: CLOSE, 20: REFUNDED | [optional] 
**session_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**error_msg** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.payout_open_api_response_dto import PayoutOpenApiResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutOpenApiResponseDto from a JSON string
payout_open_api_response_dto_instance = PayoutOpenApiResponseDto.from_json(json)
# print the JSON string representation of the object
print(PayoutOpenApiResponseDto.to_json())

# convert the object into a dict
payout_open_api_response_dto_dict = payout_open_api_response_dto_instance.to_dict()
# create an instance of PayoutOpenApiResponseDto from a dict
payout_open_api_response_dto_from_dict = PayoutOpenApiResponseDto.from_dict(payout_open_api_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


