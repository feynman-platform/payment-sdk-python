# PalmPayVirtualAccountOrderRechargeQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**order_currency** | **str** | 货币类型 | [optional] 
**order_amount** | **List[str]** | 订单金额区间 | [optional] 
**recharge_merchant_id** | **str** |  | [optional] 
**recharge_business_id** | **str** |  | [optional] 
**recharge_status** | **int** | 0: Init, 1: Success, 2: Failed, 3: Closed, 4: Refunded | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_virtual_account_order_recharge_query import PalmPayVirtualAccountOrderRechargeQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayVirtualAccountOrderRechargeQuery from a JSON string
palm_pay_virtual_account_order_recharge_query_instance = PalmPayVirtualAccountOrderRechargeQuery.from_json(json)
# print the JSON string representation of the object
print(PalmPayVirtualAccountOrderRechargeQuery.to_json())

# convert the object into a dict
palm_pay_virtual_account_order_recharge_query_dict = palm_pay_virtual_account_order_recharge_query_instance.to_dict()
# create an instance of PalmPayVirtualAccountOrderRechargeQuery from a dict
palm_pay_virtual_account_order_recharge_query_from_dict = PalmPayVirtualAccountOrderRechargeQuery.from_dict(palm_pay_virtual_account_order_recharge_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


