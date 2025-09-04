# PaymentPalmPayParam

支付单PalmPay支付参数

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | 订单标题 | [optional] 
**description** | **str** | 订单描述 | [optional] 
**payee_name** | **str** | 收款人姓名 | [optional] 
**payee_bank_code** | **str** | 收款人银行编号 | 
**payee_bank_acc_no** | **str** | 收款人银行账号 | 
**payee_phone_no** | **str** | 收款人手机号 | [optional] 
**notify_url** | **str** | 支付消息通知地址 | [optional] 
**remark** | **str** | 订单备注 | [optional] 

## Example

```python
from buybtcpay.models.payment_palm_pay_param import PaymentPalmPayParam

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPalmPayParam from a JSON string
payment_palm_pay_param_instance = PaymentPalmPayParam.from_json(json)
# print the JSON string representation of the object
print(PaymentPalmPayParam.to_json())

# convert the object into a dict
payment_palm_pay_param_dict = payment_palm_pay_param_instance.to_dict()
# create an instance of PaymentPalmPayParam from a dict
payment_palm_pay_param_from_dict = PaymentPalmPayParam.from_dict(payment_palm_pay_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


