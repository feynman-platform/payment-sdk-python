# CountPayoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.count_payout_dto import CountPayoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of CountPayoutDto from a JSON string
count_payout_dto_instance = CountPayoutDto.from_json(json)
# print the JSON string representation of the object
print(CountPayoutDto.to_json())

# convert the object into a dict
count_payout_dto_dict = count_payout_dto_instance.to_dict()
# create an instance of CountPayoutDto from a dict
count_payout_dto_from_dict = CountPayoutDto.from_dict(count_payout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


