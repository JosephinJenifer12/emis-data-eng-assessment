# Data Pipeline Assessment Project:

This repository contains a data pipeline created using python to extract/transform patient related data from json files and load them into a relational database(postgres) with data integrity.

## High Level Design

![HLD](docs/images/HLD.jpg)

## Steps to be followed to run this project:
- Ensure Docker runs in your local
- Execute the following command from the root of the repository. This creates the postgres database and also executes the docker container which in turn triggers the data pipeline to process the data files
```
docker-compose up
```
- Data will be stored in the following tables in the postgres database:
    - Patient
    - Observation

## Data Model

![dataModel](docs/images/dataModel.png)
