# AddressForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | 交易地址 | [optional] 

## Example

```python
from buybtcpay.models.address_form import AddressForm

# TODO update the JSON string below
json = "{}"
# create an instance of AddressForm from a JSON string
address_form_instance = AddressForm.from_json(json)
# print the JSON string representation of the object
print(AddressForm.to_json())

# convert the object into a dict
address_form_dict = address_form_instance.to_dict()
# create an instance of AddressForm from a dict
address_form_from_dict = AddressForm.from_dict(address_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


