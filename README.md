# Communication Contract

How to REQUEST data from the microservice?

Endpoint URL: http://localhost:5000/analyze_expense
Method: POST
Content-Type: application/json

Request Structure
To interact with the microservice, you must send a JSON object with the following structure:

- user_id (string): Unique identifier for the user.
- month (string): The month for which data analysis is requested, in "MM-YYYY" format.
- expenses (array of objects): List of expense objects, where each object contains:
  - category (string): The category of the expense (e.g., "Food", "Transport").
  - amount (number): The amount spent for that category.

Example request:
POST /analyze_expense HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "user_id": "12345",
  "month": "11-2024",
  "expenses": [
    {"category": "Food", "amount": 200},
    {"category": "Transport", "amount": 50}
  ]
}

How to RECEIVE data from the microservice?

The microservice responds with a JSON object containing the results of the expense analysis.

Response Structure
- status (string): Indicates the success or failure of the request (e.g., "success", "error").
- categorized_expenses (object): A breakdown of total expenses by category.
- monthly_total (number): The total expenses for the specified month.
- recommendations (array of strings): Recommendations for optimizing spending.

Example response:
{
  "status": "success",
  "categorized_expenses": {
    "Food": 200,
    "Transport": 50
  },
  "monthly_total": 250,
  "recommendations": [
    "Consider reducing spending on dining out.",
    "Explore using public transport to save on fuel costs."
  ]
}

UML sequence diagram:

+-------------------+              +-----------------------------+
| Calling Program   |              | Expense Analysis Microservice|
+-------------------+              +-----------------------------+
          |                                      |
          |      POST /analyze_expense           |
          |------------------------------------->|
          |                                      |
          |    Validate and Process Request      |
          |                                      |
          |   Categorize Expenses, Summarize     |
          |   Generate Recommendations           |
          |                                      |
          |             Response                 |
          |<-------------------------------------|
          |     JSON Response (categorized       |
          |     expenses, monthly total, etc.)   |
          |                                      |

