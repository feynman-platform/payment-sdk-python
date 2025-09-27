# MerchantBillExtra

交易流水额外参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | 1: Payment NGN, 10: Payment NGN, 2: Payment Merchant to Merchant, 3: Merchant Recharge, 4: Virtual account recharge, 5: Refund by system, 51: Refund by approval, 6: Frozen by system, 61: Frozen by approval, 7: Unfrozen by system, 71: Unfrozen by approval, 8: Reversal Platform to Merchant, 81: Reversal Merchant to Merchant, 82: Reversal Merchant to Platform, 83: Reversal Platform to Bank, 90: currency conversion, 999: Unknown | [optional] 
**extra** | **Dict[str, object]** | 额外参数，不同的type对应不同的参数 | [optional] 

## Example

```python
from buybtcpay.models.merchant_bill_extra import MerchantBillExtra

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBillExtra from a JSON string
merchant_bill_extra_instance = MerchantBillExtra.from_json(json)
# print the JSON string representation of the object
print(MerchantBillExtra.to_json())

# convert the object into a dict
merchant_bill_extra_dict = merchant_bill_extra_instance.to_dict()
# create an instance of MerchantBillExtra from a dict
merchant_bill_extra_from_dict = MerchantBillExtra.from_dict(merchant_bill_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


