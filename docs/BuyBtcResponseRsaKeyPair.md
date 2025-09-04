# BuyBtcResponseRsaKeyPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**RsaKeyPair**](RsaKeyPair.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_rsa_key_pair import BuyBtcResponseRsaKeyPair

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseRsaKeyPair from a JSON string
buy_btc_response_rsa_key_pair_instance = BuyBtcResponseRsaKeyPair.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseRsaKeyPair.to_json())

# convert the object into a dict
buy_btc_response_rsa_key_pair_dict = buy_btc_response_rsa_key_pair_instance.to_dict()
# create an instance of BuyBtcResponseRsaKeyPair from a dict
buy_btc_response_rsa_key_pair_from_dict = BuyBtcResponseRsaKeyPair.from_dict(buy_btc_response_rsa_key_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


