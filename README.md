
# Tiny URL Clone

A cool tiny URL clone that generate a Tiny URL for ANY links!!


## Tech Stack

**Frontend:** VueJs

**Server:** Flask, mySQL


## Environment Variables

To run this project, you will need to update the following environment variables to your .env file at root directory.

`DB_ACCOUNT_ID` : <mySQL username>

`DB_ACCOUNT_PASSWORD` : <mySQL password>

**Chances if env variables cannot be detected, might be buggy.**

Please navigate to `./App/settings.py`, edit `SQLALCHEMY_DATABASE_URI` variable to config for the DB database connection.
Replace `{os.environ.get("DB_ACCOUNT_ID")}` with DB account ID and `{os.environ.get("DB_ACCOUNT_PASSWORD")}` with DB password. <blank if needed>
Change hostname and DB port number if required.


## Requirements

**mySQL Database**

Navigate to `./App` directory and copy the contents in `schema.sql`.
Execute the SQL script in a XAMPP server of your choice to initiate the database tables and mock values.

**nodeJs**

Please have the latest version of node installed. https://nodejs.org/en/



    
## Run Locally

**Backend init**

#### Clone the project

```bash
git clone https://github.com/JarBarKar/URL-Shortening-Service.git
```

#### Go to the project directory

```bash
cd URL-Shortening-Service
```

#### Create virtual environment

-Mac-
```bash
python3 -m venv venv
```
-Windows-
```bash
py -3 -m venv venv
```

#### Activate virtual environment

-Mac-
```bash
. venv/bin/activate
```

-Windows-
```bash
venv\Scripts\activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Start the Flask server

```bash
flask --app App --debug run
```

**Frontend init**

#### Open another terminal.


#### Go to the project directory

```bash
cd ./vue-url-shortener/
```

#### Install latest dependencies

```bash
npm install
```

#### Compile and Hot-Reload for Development

```bash
npm run dev
```
## API Reference

#### Convert URL to tinyurl

```http
  POST /add_url
```

| Parameter     | Type     | Description                       |
| :--------     | :------- | :-------------------------------- |
| `url`| `string` | **Required** Full absolute path of URL to convert |


#### Retrieve current statistic of converted URL

```http
  GET /stats
```

#### Redirect from tinyurl to original URL

```http
  GET /<short_url>
```



## FAQ

#### Why no unit test and deployment?!

I want to focus on my time in enhancing and improving the core requirements first. 
And I am not comfortable in rushing out additional features given the limited time...

#### Can I contribute to this project?

Yes, anyone can! :D


## Authors

- [@JarBarKar](https://www.github.com/JarBarKar)

