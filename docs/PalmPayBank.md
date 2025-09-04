# PalmPayBank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_url** | **str** |  | [optional] 
**bg2_url** | **str** |  | [optional] 
**bg_url** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_bank import PalmPayBank

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayBank from a JSON string
palm_pay_bank_instance = PalmPayBank.from_json(json)
# print the JSON string representation of the object
print(PalmPayBank.to_json())

# convert the object into a dict
palm_pay_bank_dict = palm_pay_bank_instance.to_dict()
# create an instance of PalmPayBank from a dict
palm_pay_bank_from_dict = PalmPayBank.from_dict(palm_pay_bank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


