# RateListQueryOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**currency** | **str** |  | [optional] 
**status** | **List[int]** |  | [optional] 
**has_total** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.rate_list_query_options import RateListQueryOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RateListQueryOptions from a JSON string
rate_list_query_options_instance = RateListQueryOptions.from_json(json)
# print the JSON string representation of the object
print(RateListQueryOptions.to_json())

# convert the object into a dict
rate_list_query_options_dict = rate_list_query_options_instance.to_dict()
# create an instance of RateListQueryOptions from a dict
rate_list_query_options_from_dict = RateListQueryOptions.from_dict(rate_list_query_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


