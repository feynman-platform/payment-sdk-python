# OneofDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**proto** | [**OneofDescriptorProto**](OneofDescriptorProto.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**containing_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**field_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**synthetic** | **bool** |  | [optional] 
**options** | [**OneofOptions**](OneofOptions.md) |  | [optional] 

## Example

```python
from buybtcpay.models.oneof_descriptor import OneofDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of OneofDescriptor from a JSON string
oneof_descriptor_instance = OneofDescriptor.from_json(json)
# print the JSON string representation of the object
print(OneofDescriptor.to_json())

# convert the object into a dict
oneof_descriptor_dict = oneof_descriptor_instance.to_dict()
# create an instance of OneofDescriptor from a dict
oneof_descriptor_from_dict = OneofDescriptor.from_dict(oneof_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


