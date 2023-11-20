#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        print("Inside result: {}".format(result) if 'result' in locals() else "Division not performed")
        return result if 'result' in locals() else None
