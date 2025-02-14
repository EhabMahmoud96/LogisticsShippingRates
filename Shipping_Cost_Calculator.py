# Shipping Cost Calculator

## Input  package weight and shipping rate
weight = =float(input("Enter The package weight in kilograms :"))
rate = float (input("Enter shipping rate per kilogram: "))

## Calculate  shipping cost
shipping_cost = weight * rate

## Display the result
print(f"shipping COst: {shipping_cost} USD")
