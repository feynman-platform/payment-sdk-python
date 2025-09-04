# MerchantMoneyUsageStatisticsReq

统计商户币种消耗情况

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**start_time** | **str** | 开始-结束时间相差不能超过6个月 | 
**end_time** | **str** |  | 
**group_by_hour** | **bool** | 是否按小时分组，默认按天 | [optional] 
**currency** | **str** | 货币类型 | 

## Example

```python
from buybtcpay.models.merchant_money_usage_statistics_req import MerchantMoneyUsageStatisticsReq

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantMoneyUsageStatisticsReq from a JSON string
merchant_money_usage_statistics_req_instance = MerchantMoneyUsageStatisticsReq.from_json(json)
# print the JSON string representation of the object
print(MerchantMoneyUsageStatisticsReq.to_json())

# convert the object into a dict
merchant_money_usage_statistics_req_dict = merchant_money_usage_statistics_req_instance.to_dict()
# create an instance of MerchantMoneyUsageStatisticsReq from a dict
merchant_money_usage_statistics_req_from_dict = MerchantMoneyUsageStatisticsReq.from_dict(merchant_money_usage_statistics_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


