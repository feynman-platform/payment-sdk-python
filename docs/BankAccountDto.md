# BankAccountDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**bank_account** | **str** |  | [optional] 
**bank_code** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.bank_account_dto import BankAccountDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDto from a JSON string
bank_account_dto_instance = BankAccountDto.from_json(json)
# print the JSON string representation of the object
print(BankAccountDto.to_json())

# convert the object into a dict
bank_account_dto_dict = bank_account_dto_instance.to_dict()
# create an instance of BankAccountDto from a dict
bank_account_dto_from_dict = BankAccountDto.from_dict(bank_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


