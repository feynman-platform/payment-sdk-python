# PayResponsePaginationMerchantRechargeEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationMerchantRechargeEntity**](PayPaginationMerchantRechargeEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_merchant_recharge_entity import PayResponsePaginationMerchantRechargeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationMerchantRechargeEntity from a JSON string
pay_response_pagination_merchant_recharge_entity_instance = PayResponsePaginationMerchantRechargeEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationMerchantRechargeEntity.to_json())

# convert the object into a dict
pay_response_pagination_merchant_recharge_entity_dict = pay_response_pagination_merchant_recharge_entity_instance.to_dict()
# create an instance of PayResponsePaginationMerchantRechargeEntity from a dict
pay_response_pagination_merchant_recharge_entity_from_dict = PayResponsePaginationMerchantRechargeEntity.from_dict(pay_response_pagination_merchant_recharge_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


