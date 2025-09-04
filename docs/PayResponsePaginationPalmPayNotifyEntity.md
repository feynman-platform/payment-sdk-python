# PayResponsePaginationPalmPayNotifyEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**PayPaginationPalmPayNotifyEntity**](PayPaginationPalmPayNotifyEntity.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_pagination_palm_pay_notify_entity import PayResponsePaginationPalmPayNotifyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponsePaginationPalmPayNotifyEntity from a JSON string
pay_response_pagination_palm_pay_notify_entity_instance = PayResponsePaginationPalmPayNotifyEntity.from_json(json)
# print the JSON string representation of the object
print(PayResponsePaginationPalmPayNotifyEntity.to_json())

# convert the object into a dict
pay_response_pagination_palm_pay_notify_entity_dict = pay_response_pagination_palm_pay_notify_entity_instance.to_dict()
# create an instance of PayResponsePaginationPalmPayNotifyEntity from a dict
pay_response_pagination_palm_pay_notify_entity_from_dict = PayResponsePaginationPalmPayNotifyEntity.from_dict(pay_response_pagination_palm_pay_notify_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


