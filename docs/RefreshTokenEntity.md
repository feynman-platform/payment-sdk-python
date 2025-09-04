# RefreshTokenEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**create_at** | **datetime** |  | [optional] 
**update_at** | **datetime** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**jwt_id** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 

## Example

```python
from buybtcpay.models.refresh_token_entity import RefreshTokenEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenEntity from a JSON string
refresh_token_entity_instance = RefreshTokenEntity.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenEntity.to_json())

# convert the object into a dict
refresh_token_entity_dict = refresh_token_entity_instance.to_dict()
# create an instance of RefreshTokenEntity from a dict
refresh_token_entity_from_dict = RefreshTokenEntity.from_dict(refresh_token_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


