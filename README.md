# App string

Create a long string with all file paths and contents from an application.

## A thing with AI

The motivation for is is that currently I see some difficuties for local coding assistants to read the application code and help with contextual code.

The ordinary AI chat (even those running locally) already do a good job helping with code, though its are not designed for this specific task. So, given to those AIs chats piece of code, giving them some context before asking for help is a very effectively way to got some AI help in the code.

## How to use

This is a Python script. In terminal, just run `python generate`, and after this it will ask a path for your application. Then, it will send to the stdout the whole application code from the path provided in the prompt.
