# PayoutPaginationQuery

支付订单分页查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**merchant_order_id** | **str** |  | [optional] 
**payee_bank_code** | **str** |  | [optional] 
**payee_bank_acc_no** | **str** |  | [optional] 
**amount** | **List[str]** | 金额范围，格式：最小值-最大值 | [optional] 
**currency** | **str** | NGN: Nigerian Naira, GHS: Ghanaian Cedi, ETH: Ethereum, BTC: Bitcoin, USDT: Tether | [optional] 
**order_status** | **List[int]** | 订单状态 | [optional] 

## Example

```python
from buybtcpay.models.payout_pagination_query import PayoutPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutPaginationQuery from a JSON string
payout_pagination_query_instance = PayoutPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(PayoutPaginationQuery.to_json())

# convert the object into a dict
payout_pagination_query_dict = payout_pagination_query_instance.to_dict()
# create an instance of PayoutPaginationQuery from a dict
payout_pagination_query_from_dict = PayoutPaginationQuery.from_dict(payout_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


