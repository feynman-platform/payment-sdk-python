# PayResponseListPalmPayBank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | [**List[PalmPayBank]**](PalmPayBank.md) |  | [optional] 

## Example

```python
from buybtcpay.models.pay_response_list_palm_pay_bank import PayResponseListPalmPayBank

# TODO update the JSON string below
json = "{}"
# create an instance of PayResponseListPalmPayBank from a JSON string
pay_response_list_palm_pay_bank_instance = PayResponseListPalmPayBank.from_json(json)
# print the JSON string representation of the object
print(PayResponseListPalmPayBank.to_json())

# convert the object into a dict
pay_response_list_palm_pay_bank_dict = pay_response_list_palm_pay_bank_instance.to_dict()
# create an instance of PayResponseListPalmPayBank from a dict
pay_response_list_palm_pay_bank_from_dict = PayResponseListPalmPayBank.from_dict(pay_response_list_palm_pay_bank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


