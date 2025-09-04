# QueryBankAccountDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_code** | **str** |  | 
**bank_account** | **str** |  | 

## Example

```python
from buybtcpay.models.query_bank_account_dto import QueryBankAccountDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBankAccountDto from a JSON string
query_bank_account_dto_instance = QueryBankAccountDto.from_json(json)
# print the JSON string representation of the object
print(QueryBankAccountDto.to_json())

# convert the object into a dict
query_bank_account_dto_dict = query_bank_account_dto_instance.to_dict()
# create an instance of QueryBankAccountDto from a dict
query_bank_account_dto_from_dict = QueryBankAccountDto.from_dict(query_bank_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


