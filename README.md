# Candidates Discovery

## What is it?
NLP API for documents indexing and semantic searching. Most endpoints are associated with a particular step in the user workflow, namely:

* `/insert`: Insert the data in the Weaviate Search.
* `/search`: Search the query from the database.
* `/get-text-from-id`: It get the candidate against its id.


There are also endpoints which are not exposed to the user, but are needed internally:

* `/healthcheck`: Checks whether the service is up and running.


## Project structure

The directory structure of documents-discovery is as follows:

```
├── Dockerfile              <- Dockerfile to build the Documents-Discovery project image
├── Makefile                <- Makefile with commands like `make install`
├── README.md               <- The top-level README for developers using this project
├── app                     <- Source code for the API
│   ├── configs             <- Configuration files for tests and constants
│   ├── core                <- Models and schemas shared across API
│   ├── routers             <- Source code for each endpoint
└── requirements.txt        <- The requirements file for reproducing the production environment
```

> Note: Application code is grouped such that files related to the same topic are localized, and not such that code that is functionally similar is localized.

## Getting started
To get the project running locally first create and spin up a conda environment as follows:

```bash
conda create python=3.8 --name candidates_discovery -y && conda activate candidates_discovery
```

Next from project's root folder install the required dependencies:




```bash
pip install -r requirements
```

Run the live server

```bash
uvicorn app.main:app --reload
```

and open your browser at [http://127.0.0.1:8000/healthcheck](http://127.0.0.1:8000/healthcheck) where you should see the JSON response as:

```json
{
  "status": "Documents-Discovery server is up",
  "timestamp": "2020-04-10T12:20:15.136543"
}
```

> Note: the `--reload` flag makes the server restart after code changes and should only use for development.

## Developer installation

### Install dependencies
To install the required dependencies,


## API documentation
FastAPI offers interactive documentation for the API that can be accessed by navigating to the following endpoint:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This documentation system is powered by the OpenAPI schema, which is generated automatically by FastAPI. You can view the raw OpenAPI schema by navigating to [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## Usage

You can try out the endpoints either via "Try it out" button in the Swagger UI or by sending requests from the command line.

## Validate OpenAPI specification

All schemas for requests and responses must adhere to the [OpenAPI specification](https://swagger.io/specification/). In practice this means making sure your schema only uses the data types allowed by the specification. You can test it locally by installing OpenAPI's [Generator CLI](https://openapi-generator.tech/docs/installation) and then running

```bash
openapi-generator validate -i http://localhost:8000/openapi.json --recommend
```

which should return

```bash
Validating spec (http://localhost:8000/openapi.json)
No validation issues detected.
```

if the schemas are valid.