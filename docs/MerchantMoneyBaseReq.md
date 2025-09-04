# MerchantMoneyBaseReq

统计商户流水基础参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**start_time** | **str** | 开始-结束时间相差不能超过6个月 | 
**end_time** | **str** |  | 
**group_by_hour** | **bool** | 是否按小时分组，默认按天 | [optional] 

## Example

```python
from buybtcpay.models.merchant_money_base_req import MerchantMoneyBaseReq

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantMoneyBaseReq from a JSON string
merchant_money_base_req_instance = MerchantMoneyBaseReq.from_json(json)
# print the JSON string representation of the object
print(MerchantMoneyBaseReq.to_json())

# convert the object into a dict
merchant_money_base_req_dict = merchant_money_base_req_instance.to_dict()
# create an instance of MerchantMoneyBaseReq from a dict
merchant_money_base_req_from_dict = MerchantMoneyBaseReq.from_dict(merchant_money_base_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


