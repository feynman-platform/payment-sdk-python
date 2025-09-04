# PayResponseMerchantRechargeEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**MerchantRechargeEntity**](MerchantRechargeEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_merchant_recharge_entity import PayResponseMerchantRechargeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponseMerchantRechargeEntity from a JSON string
pay_response_merchant_recharge_entity_instance = PayResponseMerchantRechargeEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponseMerchantRechargeEntity.to_json())

# convert the object into a dict
pay_response_merchant_recharge_entity_dict = pay_response_merchant_recharge_entity_instance.to_dict()
# create an instance of PayResponseMerchantRechargeEntity from a dict
pay_response_merchant_recharge_entity_from_dict = PayResponseMerchantRechargeEntity.from_dict(pay_response_merchant_recharge_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


