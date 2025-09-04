# PalmPayVirtualAccountOrderQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**order_no** | **str** |  | [optional] 
**order_status** | **int** | 0: Init, 1: Success(Only this status will receive pay in order notifications), 2: Failed, 3: Processing, 4: Closed, 5: Refunded, 999: Unknown | [optional] 
**order_created_time_since** | **str** |  | [optional] 
**order_created_time_until** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**order_amount** | **List[str]** | 订单金额范围 | [optional] 
**reference** | **str** |  | [optional] 
**payer_account_no** | **str** |  | [optional] 
**payer_account_name** | **str** |  | [optional] 
**payer_bank_name** | **str** |  | [optional] 
**virtual_account_no** | **str** |  | [optional] 
**virtual_account_name** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_virtual_account_order_query import PalmPayVirtualAccountOrderQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayVirtualAccountOrderQuery from a JSON string
palm_pay_virtual_account_order_query_instance = PalmPayVirtualAccountOrderQuery.from_json(json)
# print the JSON string representation of the object
print(PalmPayVirtualAccountOrderQuery.to_json())

# convert the object into a dict
palm_pay_virtual_account_order_query_dict = palm_pay_virtual_account_order_query_instance.to_dict()
# create an instance of PalmPayVirtualAccountOrderQuery from a dict
palm_pay_virtual_account_order_query_from_dict = PalmPayVirtualAccountOrderQuery.from_dict(palm_pay_virtual_account_order_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


