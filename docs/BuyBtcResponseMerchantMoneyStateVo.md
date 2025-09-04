# BuyBtcResponseMerchantMoneyStateVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantMoneyStateVo**](MerchantMoneyStateVo.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_money_state_vo import BuyBtcResponseMerchantMoneyStateVo

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantMoneyStateVo from a JSON string
buy_btc_response_merchant_money_state_vo_instance = BuyBtcResponseMerchantMoneyStateVo.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantMoneyStateVo.to_json())

# convert the object into a dict
buy_btc_response_merchant_money_state_vo_dict = buy_btc_response_merchant_money_state_vo_instance.to_dict()
# create an instance of BuyBtcResponseMerchantMoneyStateVo from a dict
buy_btc_response_merchant_money_state_vo_from_dict = BuyBtcResponseMerchantMoneyStateVo.from_dict(buy_btc_response_merchant_money_state_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


