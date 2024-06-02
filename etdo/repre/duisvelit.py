try:
    # code that may raise an exception
except (ValueError, IndexError) as e:
    # code to handle both ValueError and IndexError
    print(f"An error occurred: {e}")
else:
    # code to run if no exceptions were raised
    print("Operation successful.")
finally:
    # cleanup code that runs no matter what
    print("Cleanup actions completed.")
