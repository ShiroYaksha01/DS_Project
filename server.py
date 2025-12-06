from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return int(a + b)

def subtract(a, b):
    return int(a - b)

def multiply(a, b):
    return int(a * b)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return (a / b)


# Start XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")

# Register all math operations
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

server.serve_forever()
