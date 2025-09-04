# RsaKeyPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from buybtcpay.models.rsa_key_pair import RsaKeyPair

# TODO update the JSON string below
json = "{}"
# create an instance of RsaKeyPair from a JSON string
rsa_key_pair_instance = RsaKeyPair.from_json(json)
# print the JSON string representation of the object
print(RsaKeyPair.to_json())

# convert the object into a dict
rsa_key_pair_dict = rsa_key_pair_instance.to_dict()
# create an instance of RsaKeyPair from a dict
rsa_key_pair_from_dict = RsaKeyPair.from_dict(rsa_key_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


