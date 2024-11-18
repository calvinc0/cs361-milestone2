# Communication Contract

How to REQUEST data from the microservice?

Endpoint URL: http://localhost:5000/launch_browser
Method: POST
Content-Type: application/json

Request Structure
The microservice expects a JSON object with the following fields:

- command (string): The command to execute (e.g., "open_url").
- url (string): The URL to be opened.

Example request:
{
  "command": "open_url",
  "url": "https://www.example.com"
}

How to RECEIVE data from the microservice?

The microservice responds with a JSON object containing the result of the operation.

Response Structure
- status (string): Indicates the status of the operation (e.g., "success" or "error").
- message (string): A message describing the result of the request.

Example response:
{
  "status": "success",
  "message": "Browser opened to https://www.example.com"
}

UML sequence diagram:

+-------------------+              +-----------------------------+
| Calling Program   |              | Browser Launcher Microservice|
+-------------------+              +-----------------------------+
          |                                      |
          |     POST /launch_browser             |
          |------------------------------------->|
          |                                      |
          |   Validate Request (Check command)   |
          |------------------------------------->|
          |                                      |
          |  Open Web Browser with URL (if valid)|
          |------------------------------------->|
          |                                      |
          |        Prepare Response              |
          |------------------------------------->|
          |                                      |
          |       Return JSON Response           |
          |<-------------------------------------|
          |                                      |
          |   Process and Display Response       |
          |                                      |

