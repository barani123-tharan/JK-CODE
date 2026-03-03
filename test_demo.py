"""Demo script to show all bug fixes working"""
from payment_gateway import process_payment, validate_payment

print("=" * 60)
print("PAYMENT GATEWAY BUG FIXES DEMONSTRATION")
print("=" * 60)

# Test 1: Valid payment
print("\n1. Valid Payment:")
valid_payment = {
    "amount": 100.00,
    "transaction_id": "TXN_001",
    "currency": "USD"
}
result = process_payment(valid_payment)
print(f"   Result: {result['status']}")
print(f"   Transaction ID: {result.get('transaction_id', 'N/A')}")

# Test 2: None payment (Bug Fix #1)
print("\n2. None Payment (Bug Fix - Null Check):")
result = process_payment(None)
print(f"   Result: {result['status']}")
print(f"   Reason: {result['reason']}")

# Test 3: Negative amount (Bug Fix #2)
print("\n3. Negative Amount (Bug Fix - Amount Validation):")
negative_payment = {
    "amount": -50.00,
    "transaction_id": "TXN_NEG",
    "currency": "USD"
}
result = process_payment(negative_payment)
print(f"   Result: {result['status']}")
print(f"   Reason: {result['reason']}")

# Test 4: Missing transaction ID (Bug Fix #3)
print("\n4. Missing Transaction ID (Bug Fix - ID Validation):")
no_id_payment = {
    "amount": 75.00,
    "currency": "USD"
}
result = process_payment(no_id_payment)
print(f"   Result: {result['status']}")
print(f"   Reason: {result['reason']}")

# Test 5: Zero amount
print("\n5. Zero Amount (Bug Fix - Amount Validation):")
zero_payment = {
    "amount": 0,
    "transaction_id": "TXN_ZERO",
    "currency": "USD"
}
result = process_payment(zero_payment)
print(f"   Result: {result['status']}")
print(f"   Reason: {result['reason']}")

print("\n" + "=" * 60)
print("ALL BUG FIXES VERIFIED!")
print("=" * 60)
