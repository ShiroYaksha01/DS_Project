import xmlrpc.client

# Connect to the remote server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

running = True

print("Welcome to our simple RPC client!")
print("This client allows you to add two numbers using a remote server.")
while running:
    # Get inputs from the user
    A = float(input("Input num A: "))
    B = float(input("Input num B: "))
    
    # Call the remote function
    result = proxy.add(A, B)
    print("Result from server:", result)

    # Ask user if they want to continue
    answer = input("Do you want to perform another addition? (yes/no): ")

    if answer.lower() != 'yes':
        running = False

print("Goodbye!")
