# MerchantInAndOutQuery

商户收支查询条件

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**order_by_create_at** | **str** |  | [optional] 
**create_at_since** | **str** |  | [optional] 
**create_at_until** | **str** |  | [optional] 
**currency** | **str** | 货币类型 | [optional] 
**amount** | **List[str]** | 金额 | [optional] 
**balance** | **List[str]** | 余额 | [optional] 

## Example

```python
from buybtcpay.models.merchant_in_and_out_query import MerchantInAndOutQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInAndOutQuery from a JSON string
merchant_in_and_out_query_instance = MerchantInAndOutQuery.from_json(json)
# print the JSON string representation of the object
print(MerchantInAndOutQuery.to_json())

# convert the object into a dict
merchant_in_and_out_query_dict = merchant_in_and_out_query_instance.to_dict()
# create an instance of MerchantInAndOutQuery from a dict
merchant_in_and_out_query_from_dict = MerchantInAndOutQuery.from_dict(merchant_in_and_out_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


