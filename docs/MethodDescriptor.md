# MethodDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**proto** | [**MethodDescriptorProto**](MethodDescriptorProto.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**service** | [**ServiceDescriptor**](ServiceDescriptor.md) |  | [optional] 
**input_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**output_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**client_streaming** | **bool** |  | [optional] 
**server_streaming** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**MethodOptions**](MethodOptions.md) |  | [optional] 

## Example

```python
from buybtcpay.models.method_descriptor import MethodDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of MethodDescriptor from a JSON string
method_descriptor_instance = MethodDescriptor.from_json(json)
# print the JSON string representation of the object
print(MethodDescriptor.to_json())

# convert the object into a dict
method_descriptor_dict = method_descriptor_instance.to_dict()
# create an instance of MethodDescriptor from a dict
method_descriptor_from_dict = MethodDescriptor.from_dict(method_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


