# CMRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**time_id** | **int** |  | [optional] 
**offset_multiply** | **int** |  | [optional] 
**offset_divide** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**bid_rate** | **int** |  | [optional] 
**ask_rate** | **int** |  | [optional] 
**unit** | **int** |  | [optional] 
**remark** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.cm_rate import CMRate

# TODO update the JSON string below
json = "{}"
# create an instance of CMRate from a JSON string
cm_rate_instance = CMRate.from_json(json)
# print the JSON string representation of the object
print(CMRate.to_json())

# convert the object into a dict
cm_rate_dict = cm_rate_instance.to_dict()
# create an instance of CMRate from a dict
cm_rate_from_dict = CMRate.from_dict(cm_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


