"""
Payment Gateway Module
PRODUCTION CODE - Handle with care!
"""

import json
import os
from datetime import datetime


def load_config():
    """Load configuration from config.json"""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)


def validate_payment(payment):
    """
    Validate payment object
    """
    # Check for None payment
    if payment is None:
        raise ValueError("Payment cannot be None")
    
    # Validate amount exists and is positive
    amount = payment.get('amount')
    if amount is None:
        raise ValueError("Amount is required")
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    # Validate transaction_id
    transaction_id = payment.get('transaction_id')
    if not transaction_id:
        raise ValueError("Transaction ID required")
    
    return True


def process_payment(payment):
    """
    Process a payment transaction
    """
    config = load_config()
    
    timeout = config['API_TIMEOUT']
    max_retry = config['MAX_RETRY']
    
    # Validate payment with proper error handling
    try:
        validate_payment(payment)
    except ValueError as e:
        return {"status": "error", "reason": str(e)}
    except Exception as e:
        return {"status": "error", "reason": f"Validation error: {str(e)}"}
    
    # Simulate API call
    try:
        if timeout > 10:
            print(f"Using extended timeout: {timeout}")
        
        # Process transaction
        result = execute_transaction(payment, max_retry)
        return result
        
    except Exception as e:
        return {"status": "error", "reason": f"Transaction processing error: {str(e)}"}


def execute_transaction(payment, max_retry):
    """
    Execute the actual transaction
    """
    amount = payment['amount']
    transaction_id = payment['transaction_id']
    
    # Simulate transaction
    print(f"Processing transaction {transaction_id} for ${amount}")
    
    # Handle transaction failure with rollback
    if amount < 0:
        print(f"Rolling back transaction {transaction_id}")
        return {
            "status": "failed",
            "reason": "Negative amount - transaction rolled back",
            "rolled_back": True,
            "transaction_id": transaction_id
        }
    
    return {
        "status": "success",
        "transaction_id": transaction_id,
        "amount": amount,
        "timestamp": datetime.now().isoformat()
    }


def get_transaction_status(transaction_id):
    """Get status of a transaction"""
    # BUG 10: Hidden bonus - no validation of transaction_id
    if not transaction_id:
        return None
    
    # Simulate database lookup
    return {
        "transaction_id": transaction_id,
        "status": "pending"
    }


# BONUS BUG: Memory leak simulation
_error_cache = []

def log_error(error_message):
    """Log error message"""
    # BUG: Never clears the cache - memory leak!
    _error_cache.append({
        "message": error_message,
        "timestamp": datetime.now().isoformat()
    })
    print(f"ERROR: {error_message}")


if __name__ == "__main__":
    # Test case that should work
    payment = {
        "amount": 100.00,
        "transaction_id": "TXN_001",
        "currency": "USD"
    }
    
    result = process_payment(payment)
    print(f"Result: {result}")
