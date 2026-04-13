# API Testing Automation Suite

## Project Description
This project focuses on **Backend Testing** and **API Automation**. It demonstrates how to validate RESTful APIs using Python. The suite ensures that data exchange between systems is reliable, accurate, and follows the expected protocols.

## Technical Stack
* **Language:** Python 3.x
* **Testing Framework:** PyTest
* **Library:** Requests (for HTTP calls)
* **Data Format:** JSON

## Test Scenarios
1. **Status Code Validation:** Ensures the API returns `200 OK` for successful requests.
2. **Data Integrity:** Checks if the returned JSON contains mandatory fields like `name`, `email`, and `id`.
3. **Resource Specific Testing:** Validates fetching individual resources by ID and verifies the correctness of the returned data.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt