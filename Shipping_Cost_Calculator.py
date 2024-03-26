# Shipping Cost Calculator

## Input package
weight = float(input("Enter the package in kilograms: "))
rate = float(input("Enter the shipping in kilogram: "))

## Calculate
shipping_cost = weight * rate;

## Display
print(f"shipping Cost: {shipping_cost} USD")
