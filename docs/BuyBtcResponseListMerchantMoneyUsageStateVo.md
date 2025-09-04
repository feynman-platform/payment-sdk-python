# BuyBtcResponseListMerchantMoneyUsageStateVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**List[MerchantMoneyUsageStateVo]**](MerchantMoneyUsageStateVo.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_list_merchant_money_usage_state_vo import BuyBtcResponseListMerchantMoneyUsageStateVo

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseListMerchantMoneyUsageStateVo from a JSON string
buy_btc_response_list_merchant_money_usage_state_vo_instance = BuyBtcResponseListMerchantMoneyUsageStateVo.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseListMerchantMoneyUsageStateVo.to_json())

# convert the object into a dict
buy_btc_response_list_merchant_money_usage_state_vo_dict = buy_btc_response_list_merchant_money_usage_state_vo_instance.to_dict()
# create an instance of BuyBtcResponseListMerchantMoneyUsageStateVo from a dict
buy_btc_response_list_merchant_money_usage_state_vo_from_dict = BuyBtcResponseListMerchantMoneyUsageStateVo.from_dict(buy_btc_response_list_merchant_money_usage_state_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


