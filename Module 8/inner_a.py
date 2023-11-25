def some():
    def insome():
        print("samiul")
    def again():
        print('sam again')
    
    # Call the inner function and return it
    return insome

# Access the inner function by calling the outer function
inner_func = some()()

# Now you can call the inner function using the reference
#inner_func()  # Output: "samiul"
