# RefreshTokenPaginationQuery

查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.refresh_token_pagination_query import RefreshTokenPaginationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenPaginationQuery from a JSON string
refresh_token_pagination_query_instance = RefreshTokenPaginationQuery.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenPaginationQuery.to_json())

# convert the object into a dict
refresh_token_pagination_query_dict = refresh_token_pagination_query_instance.to_dict()
# create an instance of RefreshTokenPaginationQuery from a dict
refresh_token_pagination_query_from_dict = RefreshTokenPaginationQuery.from_dict(refresh_token_pagination_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


