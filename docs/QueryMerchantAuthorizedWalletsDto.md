# QueryMerchantAuthorizedWalletsDto

查询商户已授权的钱包列表参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | 商户ID | 
**wallet_types** | **List[str]** | 钱包类型列表 | [optional] 
**permissions** | **List[str]** | 已授权的钱包功能列表 | [optional] 

## Example

```python
from buybtcpay.models.query_merchant_authorized_wallets_dto import QueryMerchantAuthorizedWalletsDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMerchantAuthorizedWalletsDto from a JSON string
query_merchant_authorized_wallets_dto_instance = QueryMerchantAuthorizedWalletsDto.from_json(json)
# print the JSON string representation of the object
print(QueryMerchantAuthorizedWalletsDto.to_json())

# convert the object into a dict
query_merchant_authorized_wallets_dto_dict = query_merchant_authorized_wallets_dto_instance.to_dict()
# create an instance of QueryMerchantAuthorizedWalletsDto from a dict
query_merchant_authorized_wallets_dto_from_dict = QueryMerchantAuthorizedWalletsDto.from_dict(query_merchant_authorized_wallets_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


