# Shipping Cost Problem

# Cost per kilo is $5

def shipping_cost(weight):
    index = 5 * weight
    return index

customer_total = shipping_cost(int(input()))
print(customer_total)