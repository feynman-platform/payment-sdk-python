# PrepaymentOrderPaginationQuery

预付订单分页查询参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**business_id** | **str** | 业务ID | [optional] 
**merchant_id** | **str** | 所属商户ID | [optional] 
**channel_id** | **str** | 链接ID | [optional] 
**amount** | **List[str]** | 金额，传对应币种的标准单位 | [optional] 
**currency** | **str** | 货币类型 | [optional] 
**order_status** | **str** | 预付款订单状态 | [optional] 
**payment_order_id** | **str** | 支付订单ID | [optional] 

## Example

```python
from buybtcpay.models.prepayment_order_pagination_query import PrepaymentOrderPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PrepaymentOrderPaginationQuery from a JSON string
prepayment_order_pagination_query_instance = PrepaymentOrderPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(PrepaymentOrderPaginationQuery.to_json())

# convert the object into a dict
prepayment_order_pagination_query_dict = prepayment_order_pagination_query_instance.to_dict()
# create an instance of PrepaymentOrderPaginationQuery from a dict
prepayment_order_pagination_query_from_dict = PrepaymentOrderPaginationQuery.from_dict(prepayment_order_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


