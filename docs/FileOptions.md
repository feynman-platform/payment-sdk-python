# FileOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_fields** | [**UnknownFieldSet**](UnknownFieldSet.md) |  | [optional] 
**java_string_check_utf8** | **bool** |  | [optional] 
**features_or_builder** | [**FeatureSetOrBuilder**](FeatureSetOrBuilder.md) |  | [optional] 
**uninterpreted_option_list** | [**List[UninterpretedOption]**](UninterpretedOption.md) |  | [optional] 
**uninterpreted_option_or_builder_list** | [**List[UninterpretedOptionOrBuilder]**](UninterpretedOptionOrBuilder.md) |  | [optional] 
**uninterpreted_option_count** | **int** |  | [optional] 
**java_package** | **str** |  | [optional] 
**java_package_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**java_outer_classname** | **str** |  | [optional] 
**java_outer_classname_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**java_multiple_files** | **bool** |  | [optional] 
**java_generate_equals_and_hash** | **bool** |  | [optional] 
**go_package** | **str** |  | [optional] 
**go_package_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**cc_generic_services** | **bool** |  | [optional] 
**java_generic_services** | **bool** |  | [optional] 
**py_generic_services** | **bool** |  | [optional] 
**php_generic_services** | **bool** |  | [optional] 
**cc_enable_arenas** | **bool** |  | [optional] 
**objc_class_prefix** | **str** |  | [optional] 
**objc_class_prefix_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**csharp_namespace** | **str** |  | [optional] 
**csharp_namespace_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**swift_prefix** | **str** |  | [optional] 
**swift_prefix_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**php_class_prefix** | **str** |  | [optional] 
**php_class_prefix_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**php_namespace** | **str** |  | [optional] 
**php_namespace_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**php_metadata_namespace** | **str** |  | [optional] 
**php_metadata_namespace_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**ruby_package** | **str** |  | [optional] 
**ruby_package_bytes** | [**ByteString**](ByteString.md) |  | [optional] 
**features** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**serialized_size** | **int** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**parser_for_type** | **object** |  | [optional] 
**default_instance_for_type** | [**FileOptions**](FileOptions.md) |  | [optional] 
**optimize_for** | **str** |  | [optional] 
**initialization_error_string** | **str** |  | [optional] 
**descriptor_for_type** | [**Descriptor**](Descriptor.md) |  | [optional] 
**all_fields** | **Dict[str, object]** |  | [optional] 
**all_fields_raw** | **Dict[str, object]** |  | [optional] 
**memoized_serialized_size** | **int** |  | [optional] 

## Example

```python
from buybtcpay.models.file_options import FileOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FileOptions from a JSON string
file_options_instance = FileOptions.from_json(json)
# print the JSON string representation of the object
print(FileOptions.to_json())

# convert the object into a dict
file_options_dict = file_options_instance.to_dict()
# create an instance of FileOptions from a dict
file_options_from_dict = FileOptions.from_dict(file_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


