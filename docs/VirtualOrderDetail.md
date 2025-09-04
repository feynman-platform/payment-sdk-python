# VirtualOrderDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **str** |  | [optional] 
**order_status** | **str** |  | [optional] 
**created_time** | **int** |  | [optional] 
**update_time** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**order_amount** | **int** |  | [optional] 
**reference** | **str** |  | [optional] 
**payer_account_no** | **str** |  | [optional] 
**payer_account_name** | **str** |  | [optional] 
**payer_bank_name** | **str** |  | [optional] 
**virtual_account_no** | **str** |  | [optional] 
**virtual_account_name** | **str** |  | [optional] 
**account_reference** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.virtual_order_detail import VirtualOrderDetail

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualOrderDetail from a JSON string
virtual_order_detail_instance = VirtualOrderDetail.from_json(json)
# print the JSON string representation of the object
print(VirtualOrderDetail.to_json())

# convert the object into a dict
virtual_order_detail_dict = virtual_order_detail_instance.to_dict()
# create an instance of VirtualOrderDetail from a dict
virtual_order_detail_from_dict = VirtualOrderDetail.from_dict(virtual_order_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


