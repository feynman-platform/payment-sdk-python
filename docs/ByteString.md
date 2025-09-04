# ByteString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** |  | [optional] 
**valid_utf8** | **bool** |  | [optional] 

## Example

```python
from buybtcpay.models.byte_string import ByteString

# TODO update the JSON string below
json = "{}"
# create an instance of ByteString from a JSON string
byte_string_instance = ByteString.from_json(json)
# print the JSON string representation of the object
print(ByteString.to_json())

# convert the object into a dict
byte_string_dict = byte_string_instance.to_dict()
# create an instance of ByteString from a dict
byte_string_from_dict = ByteString.from_dict(byte_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


