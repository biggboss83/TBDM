# TBDM Final Project

## Overview
This project is a statistical analysis tool for League of Legends games. We can load JSON files into MongoDB, query the database with Trino and visualize the data with Superset.

## Prerequisites
Before you can run this application, you will need to have [Docker](https://docs.docker.com/get-docker/) installed on your system with [Docker Compose](https://docs.docker.com/compose/install/). Docker should take care of the rest of the dependencies.

## Installation
To install and run this application, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run `docker-compose pull` to download the required Docker images.
4. Run `docker-compose up` to start the application.
5. Navigate to `http://localhost:8088` in your web browser to access Superset.
6. Create a new database and collection in MongoDB by running the following commands in your terminal:
    - `docker exec -it mongo mongosh`
    - `use league`
    - `db.createCollection("matches")`
    - `exit`
7. To load all match data JSON files into MongoDB, cd into the `matches` folder with the JSON files and run 
    - `for filename in *; do docker exec mongo mongoimport -d league -c matches --file /tmp/matches/$filename;  done`

## Configuration
Once in `Superset` you will need to configure the database connection to `Trino`. To do this, navigate to `Settings > Database Connections` in the top menu bar. Then, click the `+ Databse` button in the top right corner and fill out the form with the following information:
- Database: `Trino`
- SQLAlchemy URI: `trino://trino@host.docker.internal:8080`

Go to the `Advanced` tab and under `SQL Lab` enable the following options:
- Expose database in SQL Lab
- Allow CREATE TABLE AS
- Allow CREATE VIEW AS
- Allow DML
- Allow this database to be explored


## Usage
Once the application is running, you can access it by navigating to `http://localhost:8088` in your web browser. From there, you can query the database and visualize the data.
Example queries:
- `SELECT info.gameCreation FROM mongo.league.matches;`

## Future Improvements
- Use the RIOT Games API to load data into MongoDB
- Create more visualizations with better domain knowledge of League of Legends
- Real-time data streaming and analysis
