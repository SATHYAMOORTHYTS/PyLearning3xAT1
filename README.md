List of topics covered in the document that you can add to a README.md file:

# Python Learning

- Introduction to Python
- Python Installation
- Writing Your First Code
- Comments in Python
- Keywords and Identifiers
- Variables and Data Types
- Operators
- Conditions and Loops
- Functions and Strings
- Type Conversions
- Lambda Functions
- Map and Filter Functions
- Recursion
- Lists
- Tuples
- Sets
- Dictionaries
- Object-Oriented Programming (OOP)
  - Classes and Objects
  - Constructors
  - Encapsulation
  - Polymorphism
  - Inheritance
  - Abstraction
- Exception Handling
- Modules in Python
- Collections in Python
  - Counters
  - OrderedDict
- Regular Expressions (Regex)

# How to work with a Pytest?

**PyTest**

- Install pytest - **pip install pytest**
- Create your first test -** test_name.py , test_**
- Run multiple tests -> **-k, -m **
- Assert that a certain exception is raised - **assert AR == ER**
- Group multiple tests in a class ->  **-k, pattern smoke **
- Allure Report - allure-pytest


# How to run the pytest
--> selct all code --> right click --> run


## pytest commands

- pytest -h - 
- pytest - To run all teh testcases
- To run specific test 
   - pytest PyLearning3xAT/Api Automation/test_lab002.py

- To run spedfic testcases with pattern
   - pytest -k "2"

- To run a specific test case use annotation
  - @pytest.mark.regression
  - pytest -m "regression" PyLearning3xAT/Api Automation/test_lab003.py




**How to see the Report of the PyTest Testcases?**

- Make sure that allure commandline is installed

- Download the Node JS

- node -v

- npm install -g npm allure-commandline

- Verify that allure -> options

- Run your Pytestcase - pytest ex02_July/22072024/test_Lab183.py --alluredir=allure_result

- allure serve allure_result

## How to add requests 
- pip install requests