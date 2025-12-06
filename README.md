# About this project
<p>
This is a simple project of creating a simple application to implement RPC server in the app.
<p>

<p>  
Our programs (both client and server) were created in python language using xmlrpc package,  which provides modules for implementing the XML-RPC protocol for both clients and servers. XML-RPC is a Remote Procedure Call (RPC) method that utilizes XML over HTTP for communication. This allows a client to invoke methods on a remote server, passing parameters and receiving structured data in return.
<p>

<p>
In our application, the client can run the program in order to use a simple calculation that supports addition, subtraction, multiplication, anddivision. When the user click "Enter", the program will send the inputted numbers and operation sign to the server and let it does the maths operation, then send the result back to the client program.
<p>

# How to run the program

First run the server by writing this in the terminal
```
python server.py
```

After that run the client code
```
python client.py
```