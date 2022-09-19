# WE-HUB bot

Code for the chatbot we're working on

## Table of contents

- [Requirements](#requirements)
- [Built with](#built-with)
- [Set Up](#set-up)
    - [Get a sandbox](#get-a-sandbox)
    - [Create an Ngrok account](#ngrok-account)
    - [Setting up javascript server](#js-set-up)
    - [Setting up the python server](#py-set-up)
- [How to Use](#how-to-use)
    - [Start Ngrok](#start-ngrok) 
- [Customisation]

## Requirements

Before proceeding, you should install;

- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/)
- Node JS 14 and above - [download](https://nodejs.org/en/download/)
- A reverse proxy agent. Preferably [Ngrok](https://ngrok.com/)
- A twilio sandbox - register for one [here](https://www.twilio.com/docs/whatsapp/sandbox)
- MongoDB - Cloud or [MongoDB Compass](https://www.mongodb.com/try/download/compass)

## Built with

- Python
- Javacript

## Set Up

### Get a Sandbox

To do this, Create an account [here](https://www.twilio.com/docs/whatsapp/sandbox) and complete the process.

### Ngrok account

Create an Ngrok account and download the software [here](https://ngrok.com/)

### JS Set-Up

**Note: To do this, you should have NodeJS installed**
- Navigate to the folder in your terminal;

```shell
    cd ./node-backend_bot
```

- Install necessary packages by running;

```shell
    npm install
```

### Py Set-Up

**Note: To do this, you should have Python and the *pipenv python package* installed**
- Navigate to the folder in your terminal;

```shell
    cd ./python_bot
```
- If you do not have pipenv, install it by running;

```shell
    pip install pipenv
```

- Install necessary packages by running;

```shell
    pipenv sync
```

## How to use

### Start Ngrok

- In the ngrok terminal, run;
```shell
    ngrok http 5000 *(Or whatever port you choose for the python application)*
```

## Customisation

*Individual READMEs will be provided in the individual folders*
- [Javascript](node-backend_bot/README.md)
- [Python](python_bot/README.md)