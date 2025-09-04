# ServiceDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**proto** | [**ServiceDescriptorProto**](ServiceDescriptorProto.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**methods** | [**List[MethodDescriptor]**](MethodDescriptor.md) |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**ServiceOptions**](ServiceOptions.md) |  | [optional] 

## Example

```python
from buybtcpay.models.service_descriptor import ServiceDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDescriptor from a JSON string
service_descriptor_instance = ServiceDescriptor.from_json(json)
# print the JSON string representation of the object
print(ServiceDescriptor.to_json())

# convert the object into a dict
service_descriptor_dict = service_descriptor_instance.to_dict()
# create an instance of ServiceDescriptor from a dict
service_descriptor_from_dict = ServiceDescriptor.from_dict(service_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


