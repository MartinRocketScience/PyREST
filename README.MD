
# PyREST

This is a ready-to-use framework template with integrated libraries and project structure for implementing automated REST API tests using Gherkin (Behave) and the JSON Model Pattern (similar to the Page Object Model). The framework also includes integrated OAUTH2 implementation.

Feel free to adapt it into your project.

## Setup Instructions

### 1. Create and activate a virtual environment

#### On Windows

```cmd
python -m venv PyREST
PyREST\Scripts\activate
```

#### On macOS/Linux

```bash
python -m venv PyREST
source PyREST/bin/activate
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Install the local module in editable mode

```bash
pip install -e .
```

### 4. Verify the installation

You can verify that the installation was successful by running a test or a sample script.

```bash
python -m unittest discover tests
```

## 5. Running the Tests

To run the tests, make sure your virtual environment is activated, then run:

```bash
behave
```

## Additional Information

- Ensure you have Python 3.8 or newer installed.
- For any issues, please create an issue on the GitHub repository.
