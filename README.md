# App string

Create a long string with all file paths and contents from an application.

## A thing with AI

The motivation for is is that currently I see some difficuties for local coding assistants to read the application code and help with contextual code.

The ordinary AI chat (even those running locally) already do a good job helping with code, though its are not designed for this specific task. So, given to those AIs chats piece of code, giving them some context before asking for help is a very effectively way to got some AI help in the code.

## How to use

This is a Python installable package script.

First, install it with:
```
pip install . --break-system-packages
```
Then in terminal, just run `app-string`, and after this it will ask a path for your application. Then, it will send to the stdout the whole application code from the path provided in the prompt.

## `.app-string-ignore`

Maybe you have an application that is a little complicated if excluding all non-relevant files, like node_modules, vendor, builds artifacts, dist, etc and there's alot of things that you need to put in `--regex-ignore`

In your project folder, you can put a file called `.app-string-ignore`. In its content, set line by line each of terms that would be put in `--regex-ignore`. So every time that you list the contents, you don't need to provider then exclusion terms again.

## How to debug (In VSCodium)

1. Install debugpy:
```
pip3 install debugpy --break-system-packages
```

2. Add or implement an entry for `./.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Python Debugger: Command",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5679
            },
            "justMyCode": false
        }
    ]
}
```

3. Run:

```
python3 -m debugpy --listen 5679 --wait-for-client app_string/cli.py
```

## How to use

### Basic usage (prompts for path)
app-string

### Specify path directly
app-string /path/to/directory

### Don't ignore .git directories
app-string --no-ignore-git /path/to/directory

### Only show paths, not contents
app-string --only-path /path/to/directory

### Use regex to ignore files
app-string --regex-ignore ".*\.pyc|__pycache__" /path/to/directory

### Multiple options
app-string --no-ignore-git --no-ignore-node-modules --only-path /path/to/directory
