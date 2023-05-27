import json

serialized_data = "{\"function\": \"<Function createProduct(uint256,uint256,uint8)>\", \"arguments\": {\"_prod_id\": 1, \"_prod_qty\": 1, \"_prod_qlt\": 1}}"
parsed_data = json.loads(serialized_data)

function_name = parsed_data['function']
print(function_name)
