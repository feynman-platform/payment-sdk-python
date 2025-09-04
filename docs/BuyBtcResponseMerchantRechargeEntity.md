# BuyBtcResponseMerchantRechargeEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**MerchantRechargeEntity**](MerchantRechargeEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_merchant_recharge_entity import BuyBtcResponseMerchantRechargeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseMerchantRechargeEntity from a JSON string
buy_btc_response_merchant_recharge_entity_instance = BuyBtcResponseMerchantRechargeEntity.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseMerchantRechargeEntity.to_json())

# convert the object into a dict
buy_btc_response_merchant_recharge_entity_dict = buy_btc_response_merchant_recharge_entity_instance.to_dict()
# create an instance of BuyBtcResponseMerchantRechargeEntity from a dict
buy_btc_response_merchant_recharge_entity_from_dict = BuyBtcResponseMerchantRechargeEntity.from_dict(buy_btc_response_merchant_recharge_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


