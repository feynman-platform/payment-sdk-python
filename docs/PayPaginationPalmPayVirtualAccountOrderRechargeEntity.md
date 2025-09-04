# PayPaginationPalmPayVirtualAccountOrderRechargeEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**current** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**latest** | **bool** |  | [optional] 
**data** | [**List[PalmPayVirtualAccountOrderRechargeEntity]**](PalmPayVirtualAccountOrderRechargeEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_pagination_palm_pay_virtual_account_order_recharge_entity import PayPaginationPalmPayVirtualAccountOrderRechargeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayPaginationPalmPayVirtualAccountOrderRechargeEntity from a JSON string
pay_pagination_palm_pay_virtual_account_order_recharge_entity_instance = PayPaginationPalmPayVirtualAccountOrderRechargeEntity.from_json(json)
# print the JSON string representation of the object
print(PayPaginationPalmPayVirtualAccountOrderRechargeEntity.to_json())

# convert the object into a dict
pay_pagination_palm_pay_virtual_account_order_recharge_entity_dict = pay_pagination_palm_pay_virtual_account_order_recharge_entity_instance.to_dict()
# create an instance of PayPaginationPalmPayVirtualAccountOrderRechargeEntity from a dict
pay_pagination_palm_pay_virtual_account_order_recharge_entity_from_dict = PayPaginationPalmPayVirtualAccountOrderRechargeEntity.from_dict(pay_pagination_palm_pay_virtual_account_order_recharge_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


