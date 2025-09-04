# BuyBtcResponseLedgerTransactionAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**data** | [**LedgerTransactionAggregation**](LedgerTransactionAggregation.md) |  | [optional] 

## Example

```python
from buybtcpay.models.buy_btc_response_ledger_transaction_aggregation import BuyBtcResponseLedgerTransactionAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of BuyBtcResponseLedgerTransactionAggregation from a JSON string
buy_btc_response_ledger_transaction_aggregation_instance = BuyBtcResponseLedgerTransactionAggregation.from_json(json)
# print the JSON string representation of the object
print(BuyBtcResponseLedgerTransactionAggregation.to_json())

# convert the object into a dict
buy_btc_response_ledger_transaction_aggregation_dict = buy_btc_response_ledger_transaction_aggregation_instance.to_dict()
# create an instance of BuyBtcResponseLedgerTransactionAggregation from a dict
buy_btc_response_ledger_transaction_aggregation_from_dict = BuyBtcResponseLedgerTransactionAggregation.from_dict(buy_btc_response_ledger_transaction_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


