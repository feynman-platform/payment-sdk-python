# PaymentOrderPaginationQuery

支付单分页查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**order_id** | **str** | 订单号 | [optional] 
**merchant_id** | **str** | 所属商户ID | [optional] 
**channel_id** | **str** | 支付链路ID | [optional] 
**type** | **int** | 0: Merchant to merchant, 1: Withdrawal | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 
**amount** | **List[str]** | 支付金额区间 | [optional] 
**fee** | **List[str]** | 手续费 | [optional] 
**order_status** | **int** | 0: UNPAID, 1: PAYING, 2: SUCCESS, 3: FAIL, 4: CLOSE, 20: REFUNDED | [optional] 
**prepayment_order_id** | **str** | 预付单号 | [optional] 

## Example

```python
from buybtcpay.models.payment_order_pagination_query import PaymentOrderPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOrderPaginationQuery from a JSON string
payment_order_pagination_query_instance = PaymentOrderPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(PaymentOrderPaginationQuery.to_json())

# convert the object into a dict
payment_order_pagination_query_dict = payment_order_pagination_query_instance.to_dict()
# create an instance of PaymentOrderPaginationQuery from a dict
payment_order_pagination_query_from_dict = PaymentOrderPaginationQuery.from_dict(payment_order_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


