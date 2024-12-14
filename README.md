#  Automation Project with Playwright

There is a test project to try [Playwright](https://playwright.dev/python/) 
as a framework for web automation. There is also implemented reporting
with [Allure Report](https://allurereport.org/).

### Object for automation

As an object for automation I chose this page: https://www.saucedemo.com/.

## 🛠️ Tech Stack

1. Programming language - `Python`
2. Automation frameworks:
   1. to launch the tests - `Pytest`
   2. to operate the browser - `Playwright`
3. Tool for reporting - `Allure Report`

## 🚀 How to run the tests

1. Clone the repository.
2.  Go to the project directory.
3. Install dependencies using the command:
```shell
pip install -r requirements.txt
```
4. Install the browsers
```shell
playwright install
```
5. Run tests in the console using the command:<br>
```shell
pytest .\tests\
```

## 📄 How to check the test results report
1. Generate the report.
```shell
allure generate --clean reports
```
2. Open the report.
```shell
allure open  
```