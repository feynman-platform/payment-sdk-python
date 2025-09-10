# ApprovalPaginationQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**applicant_id** | **str** |  | [optional] 
**approval_status** | **int** | 0: Awaiting Approval, 1: Approved, 2: Rejected, 3: Canceled | [optional] 
**approval_time_since** | **str** |  | [optional] 
**approval_time_until** | **str** |  | [optional] 
**approval_type** | **int** | 0: Platform Recharge, 1: Merchant Recharge, 11: Virtual Account Recharge, 12: Merchant Self Service Recharge, 13: Virtual Account Self Service Recharge, 14: Merchant Self Service Recharge by PalmPay Virtual Account, 15: Virtual merchant Self Service Recharge by PalmPay Virtual Account, 2: Refund, 3: Frozen, 4: Unfrozen, 100: Reversal platform to merchant, 101: Reversal merchant to platform, 102: Reversal merchant to merchant | [optional] 
**approval_types** | **List[int]** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.approval_pagination_query import ApprovalPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalPaginationQuery from a JSON string
approval_pagination_query_instance = ApprovalPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(ApprovalPaginationQuery.to_json())

# convert the object into a dict
approval_pagination_query_dict = approval_pagination_query_instance.to_dict()
# create an instance of ApprovalPaginationQuery from a dict
approval_pagination_query_from_dict = ApprovalPaginationQuery.from_dict(approval_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


