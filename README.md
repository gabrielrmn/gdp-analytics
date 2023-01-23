## Stone Case - GDP Information

This project creates a REST API using Flask and Postgres to provide information about GDP for different countries.

## API Endpoints

### **/country**

Get information about the country, region, indicators, etc.

Params:

    - country: Country name or Country code.

### **/region**

Get GDP information about all countries from a specified region.

Params:

    - region: Region name.

### **/gdp**

Get GDP information about the specified country.

Params:

    - country: Country name or Country code.

### **/highest_avg_gdp**

Get the top 10 countries with the highest average GDP for the specified period.

Params:

    - start: Start year.
    - end: End year.

### **/lowest_avg_gdp**

Get the top 10 countries with the lowest average GDP for the specified period.

Params:

    - start: Start year.
    - end: End year.

## Running the project

In order to run the project, you need to install the `Make` in your machine and also `Docker`.
Then, you just need to execute:

`make build`

And after that:

`make up`

The API will be listening on port 5000, and the Postgres DB on port 5434.

## Request Example

`curl --location --request GET 'http://127.0.0.1:5000/lowest_avg_gdp?start=2000&end=2020' --data-raw ''`
