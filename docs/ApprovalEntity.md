# ApprovalEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**applicant_id** | **str** |  | [optional] 
**approval_status** | **int** | 0: Awaiting Approval, 1: Approved, 2: Rejected, 3: Canceled | [optional] 
**approval_time** | **datetime** |  | [optional] 
**approver_id** | **str** |  | [optional] 
**approval_comment** | **str** |  | [optional] 
**approval_type** | **int** | 0: Platform Recharge, 1: Merchant Recharge, 11: Virtual Account Recharge, 12: Merchant Self Service Recharge, 13: Virtual Account Self Service Recharge, 14: Merchant Self Service Recharge by PalmPay Virtual Account, 15: Virtual merchant Self Service Recharge by PalmPay Virtual Account, 2: Refund, 3: Frozen, 4: Unfrozen, 100: Reversal platform to merchant, 101: Reversal merchant to platform, 102: Reversal merchant to merchant | [optional] 
**business_id** | **str** |  | [optional] 
**apply_content** | **str** |  | [optional] 
**bill_ids** | **List[int]** |  | [optional] 

## Example

```python
from buybtcpay.models.approval_entity import ApprovalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalEntity from a JSON string
approval_entity_instance = ApprovalEntity.from_json(json)
# print the JSON string representation of the object
print(ApprovalEntity.to_json())

# convert the object into a dict
approval_entity_dict = approval_entity_instance.to_dict()
# create an instance of ApprovalEntity from a dict
approval_entity_from_dict = ApprovalEntity.from_dict(approval_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


