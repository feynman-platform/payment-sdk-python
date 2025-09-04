# RateListRequestQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**RateListQueryOptions**](RateListQueryOptions.md) |  | [optional] 
**sort** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.rate_list_request_query import RateListRequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RateListRequestQuery from a JSON string
rate_list_request_query_instance = RateListRequestQuery.from_json(json)
# print the JSON string representation of the object
print(RateListRequestQuery.to_json())

# convert the object into a dict
rate_list_request_query_dict = rate_list_request_query_instance.to_dict()
# create an instance of RateListRequestQuery from a dict
rate_list_request_query_from_dict = RateListRequestQuery.from_dict(rate_list_request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


