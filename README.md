# lexicons-example
Public chat room example using the lexicons stateless websocket server framework.

The client Mac and Linux builds built from the Godot game engine. 

# Usage
Go to client/mac/chat-client.zip or client/linux/Lexicons-example-client.x86_64 and run the client.
(If on linux enter `$ ./Lexicons-example-client.x86_64` in the terminal)

Run the server using the following commands:
```
pip install lexicons
python3 main.py run
```

If you want to run the server across a different host than the localhost, set that in the `--host` argument. Such as:
```
python3 main.py run --host <YOUR DOMAIN HERE>
```

In the client, enter swap out the localhost with your new domain.

Enter a username and password.
(WARNING!! The password is easily visible in the logs of this example, do not use a real password!!!)

Click on register.

Click on Login.

Start chatting with other clients. :)
