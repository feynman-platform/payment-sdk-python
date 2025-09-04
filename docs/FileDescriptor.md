# FileDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proto** | [**FileDescriptorProto**](FileDescriptorProto.md) |  | [optional] 
**message_types** | [**List[Descriptor]**](Descriptor.md) |  | [optional] 
**enum_types** | [**List[EnumDescriptor]**](EnumDescriptor.md) |  | [optional] 
**services** | [**List[ServiceDescriptor]**](ServiceDescriptor.md) |  | [optional] 
**extensions** | [**List[FieldDescriptor]**](FieldDescriptor.md) |  | [optional] 
**dependencies** | [**List[FileDescriptor]**](FileDescriptor.md) |  | [optional] 
**public_dependencies** | [**List[FileDescriptor]**](FileDescriptor.md) |  | [optional] 
**syntax** | **str** |  | [optional] 
**edition** | **str** |  | [optional] 
**edition_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**file** | [**FileDescriptor**](FileDescriptor.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**options** | [**FileOptions**](FileOptions.md) |  | [optional] 

## Example

```python
from buybtcpay.models.file_descriptor import FileDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of FileDescriptor from a JSON string
file_descriptor_instance = FileDescriptor.from_json(json)
# print the JSON string representation of the object
print(FileDescriptor.to_json())

# convert the object into a dict
file_descriptor_dict = file_descriptor_instance.to_dict()
# create an instance of FileDescriptor from a dict
file_descriptor_from_dict = FileDescriptor.from_dict(file_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


