# AllocationForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | 原始金额 | [optional] 

## Example

```python
from buybtcpay.models.allocation_form import AllocationForm

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationForm from a JSON string
allocation_form_instance = AllocationForm.from_json(json)
# print the JSON string representation of the object
print(AllocationForm.to_json())

# convert the object into a dict
allocation_form_dict = allocation_form_instance.to_dict()
# create an instance of AllocationForm from a dict
allocation_form_from_dict = AllocationForm.from_dict(allocation_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


