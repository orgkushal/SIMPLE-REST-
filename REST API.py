import json

# In-memory data store for company objects
companies = [
    {"id": 1, "name": "Company A", "location": "Location A"},
    {"id": 2, "name": "Company B", "location": "Location B"},
    {"id": 3, "name": "Company C", "location": "Location C"}
]

# Endpoint function to check if service is running or not
def status(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'running'})
    }

# Endpoint function to get company details by ID
def get_company(event, context):
    company_id = int(event['pathParameters']['id'])
    company = next((c for c in companies if c['id'] == company_id), None)
    if company:
        return {
            'statusCode': 200,
            'body': json.dumps(company)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Company not found'})
        }

# Endpoint function to compare company details and return delta
def compare_company(event, context):
    company_id_1 = int(event['pathParameters']['id'])
    company_id_2 = int(event['pathParameters']['id2'])
    company_1 = next((c for c in companies if c['id'] == company_id_1), None)
    company_2 = next((c for c in companies if c['id'] == company_id_2), None)
    if company_1 and company_2:
        delta = {k: company_1[k] for k in company_1 if company_1[k] != company_2.get(k)}
        return {
            'statusCode': 200,
            'body': json.dumps(delta)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'One or more companies not found'})
        }

# Endpoint function to insert a new company record
def insert_company(event, context):
    new_company = json.loads(event['body'])
    new_company_id = max(c['id'] for c in companies) + 1
    new_company['id'] = new_company_id
    companies.append(new_company)
    return {
        'statusCode': 200,
        'body': json.dumps({'id': new_company_id})
    }

# Endpoint function to update an existing company record
def update_company(event, context):
    company_id = int(event['pathParameters']['id'])
    updated_company = json.loads(event['body'])
    for i, company in enumerate(companies):
        if company['id'] == company_id:
            companies[i] = updated_company
            companies[i]['id'] = company_id  # Ensure ID is not changed
            return {
                'statusCode': 200,
                'body': json.dumps({'success': True})
            }
    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'Company not found'})
    }

# Endpoint function to get list of all companies
def get_companies(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(companies)
    }
