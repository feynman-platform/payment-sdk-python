# PayResponsePaginationRefreshTokenEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationRefreshTokenEntity**](PayPaginationRefreshTokenEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_refresh_token_entity import PayResponsePaginationRefreshTokenEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationRefreshTokenEntity from a JSON string
pay_response_pagination_refresh_token_entity_instance = PayResponsePaginationRefreshTokenEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationRefreshTokenEntity.to_json())

# convert the object into a dict
pay_response_pagination_refresh_token_entity_dict = pay_response_pagination_refresh_token_entity_instance.to_dict()
# create an instance of PayResponsePaginationRefreshTokenEntity from a dict
pay_response_pagination_refresh_token_entity_from_dict = PayResponsePaginationRefreshTokenEntity.from_dict(pay_response_pagination_refresh_token_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


