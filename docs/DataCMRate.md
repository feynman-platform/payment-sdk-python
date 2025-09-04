# DataCMRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**list** | [**List[CMRate]**](CMRate.md) |  | [optional] 

## Example

```python
from buybtcpay.models.data_cm_rate import DataCMRate

# TODO update the JSON string below
json = "{}"
# create an instance of DataCMRate from a JSON string
data_cm_rate_instance = DataCMRate.from_json(json)
# print the JSON string representation of the object
print(DataCMRate.to_json())

# convert the object into a dict
data_cm_rate_dict = data_cm_rate_instance.to_dict()
# create an instance of DataCMRate from a dict
data_cm_rate_from_dict = DataCMRate.from_dict(data_cm_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


