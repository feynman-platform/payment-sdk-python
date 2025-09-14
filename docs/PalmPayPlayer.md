# PalmPayPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**account_no** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.palm_pay_player import PalmPayPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of PalmPayPlayer from a JSON string
palm_pay_player_instance = PalmPayPlayer.from_json(json)
# print the JSON string representation of the object
print(PalmPayPlayer.to_json())

# convert the object into a dict
palm_pay_player_dict = palm_pay_player_instance.to_dict()
# create an instance of PalmPayPlayer from a dict
palm_pay_player_from_dict = PalmPayPlayer.from_dict(palm_pay_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


