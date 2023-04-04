Simple REST Endpoint

This project implements a simple REST API with the following endpoints:

/status: Returns the status of the service (running or not).

/company/<id>: Retrieves the details of a company with the specified ID.

/company/<id>/compare/<id2>: Compares the details of two companies with the specified IDs and returns the differences.

/company/: Inserts a new company record.

/company/<id>: Updates an existing company record with the specified ID.

/companies: Retrieves a list of all companies.

The API is implemented using Python and is designed to be deployed as a serverless API on AWS Lambda and API Gateway. Data is stored in an in-memory data store, so no database or modeling is required.

Getting Started
To run the API locally, you can use LocalStack to simulate an AWS instance. Follow these steps to get started:

Clone this repository to your local machine.

Install the required Python packages using pip install -r requirements.txt.

Start LocalStack using localstack start.

Deploy the API to LocalStack using sam local start-api --env-vars env.json.

Test the API using your preferred tool (e.g. curl, Postman).

Note: The env.json file contains environment variables for the AWS region and Localstack endpoint URL. Update these variables as needed for your environment.

Endpoint Details

/status

Method: GET

Returns: The status of the service (running or not).

/company/<id>

Method: GET

Parameters:

id: The ID of the company to retrieve.

Returns: The details of the company with the specified ID.

/company/<id>/compare/<id2>

Method: GET

Parameters:

id: The ID of the first company to compare.

id2: The ID of the second company to compare.

Returns: The differences between the details of the two companies with the specified IDs.

/company/

Method: POST

Body: A JSON object containing the details of the new company.

Returns: The ID of the newly inserted company record.

/company/<id>

Method: PUT

Parameters:

id: The ID of the company to update.

Body: A JSON object containing the updated details of the company.

Returns: A success message if the update was successful.

/companies

Method: GET

Returns: A list of all companies.

Authentication

Authentication is optional but can be implemented using AWS API Gateway and API Keys.

Code Quality

The code quality of this project has been evaluated based on the following criteria:

Logging: Logging is implemented using the Python logging module.

Code comments: Code comments are included throughout the project to improve readability and maintainability.

Logic: The logic of the project has been implemented according to the provided contracts.

Authors

KUSHAL MISHRA

Acknowledgements


This project was inspired by the following resources:

AWS Lambda documentation

AWS API Gateway documentation

LocalStack documentation
