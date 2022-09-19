# WE-HUB bot

Code for the chatbot we're working on

## Table of contents

- [Requirements](#requirements)
- [Built with](#built-with)
- [Set Up](#set-up)
    - [Get and activate a sandbox](#get-a-sandbox)
    - [Create an Ngrok account](#ngrok-account)
    - [Setting up javascript server](#js-set-up)
    - [Setting up the python server](#py-set-up)
- [Customisation](#customisation)
- [How to Use](#how-to-use)
    - [Start Ngrok](#start-ngrok) 
    - [Add your link to your twilio console](#adding-link-to-twilio-console)
    - [Run Python](#run-python)
    - [Run JavaScript](#run-js)

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

To do this, Create an account [here](https://www.twilio.com/docs/whatsapp/sandbox) and complete the process. After that, you go to your *console > Messaging > settings > Whatsapp Sandbox Settings* and follow the instructions you see there

### Ngrok account

Create an Ngrok account and download the software [here](https://ngrok.com/)

### JS Set-Up

**Note: To do this, you should have NodeJS installed**

*** In your Terminal ***
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

*** In your Terminal ***
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

## Customisation

*Individual READMEs will be provided in the individual folders*
- [For Javascript](node-backend_bot/README.md)
- [For Python](python_bot/README.md)

## How to use

### Start Ngrok

- In the ngrok terminal, run;
```shell
    ngrok http 5000
```

### Adding link to twilio console

#### ***Very Important***
- **Copy the tunnel link gotten from the ngrok terminal**
![Tz8X34.png](https://imgpile.com/images/Tz8X34.png)

- **Update the link in your sandbox settings**
![Tz8Fzg.png](https://imgpile.com/images/Tz8Fzg.png)

- **Click save at the bottom of the page to save your settings***
![Tz8B9R.png](https://imgpile.com/images/Tz8B9R.png)


### Run JS

*** In your Terminal ***
- Navigate to the folder in your terminal;

```shell
    cd ./node-backend_bot
```

- start the application

```shell
    npm run server
```


### Run Python

```shell
    cd ./python_bot
```

*** In your Terminal ***
- Activate the Environment

```shell
    pipenv shell
```
- In the Virtual Environment, Run the program

```shell
    python main.py
```