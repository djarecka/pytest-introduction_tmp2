<!--
  <<< Author notes: Step 3 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
  TBD-step-3-notes.
-->

# Week 3: Introduction to `fixtures`

In the third week we will review what we learned about testing and pytest in the previous weeks, 
and we will introduce the concept of `fixtures` in `pytest`.

## 1 :book: Review of the testing and pytest

Let's start from reading more about the testing and pytest to review and expand what we learned in the previous weeks:

- [Real Python: Effective Python thesting with pytest](https://realpython.com/pytest-python-testing)
  - read the content of [What makes pytest so useful](https://realpython.com/pytest-python-testing/#what-makes-pytest-so-useful)
for a great overview of the reasons why `pytest` is so popular
  - read the content of [Parametrization: combining test](https://realpython.com/pytest-python-testing/#parametrization-combining-tests)
to review the concept of parametrization
- [Real Python: Getting started with testing in Python](https://realpython.com/python-testing/)
  - you can read or just skim through the content of first 2 sections in order to see the difference between `unittest` and `pytest`


## 2 :book: What are fixtures in `pytest`?

Fixtures are a powerful feature of `pytest` that allows you to define a set of data that you can reuse across multiple tests.
Fixtures are especially useful when you need to set up some data before running a test and clean up after the test is done.

You should read more from [Real Python: Effective Python thesting with pytest](https://realpython.com/pytest-python-testing/#fixtures-managing-state-and-dependencies)
to learn more about fixtures.

## 3 :keyboard: :white_check_mark: Exercise 1: Using fixtures in `pytest`
In the `week3` branch you will find a new directory `week3` that will be used as a working directory for this week.
The file `week3/personal_info.py` contains functions to extract important information from the dictionary with personal information.
1. Create a new file `week3/test_personal_info.py` and write a test for the function `get_address`
2. Create a ficture `personal_info` that can be used in the test file
  - create a new file `week3/conftest.py` and define a fixture `personal_info`
  - modify the test to use the fixture
3. Create a new test for the function `get_name` that will use the same fixture
4. Think if you could parametrize the fixture to test multiple cases

## 4 :book: Using `mark.parametrize` with fixtures
Last time we learned about parametrization of the testing functions when using `pytest`. 
You can also parametrize fixtures to test multiple cases.
  - read more about [parametrizing fixtures](https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures) in the `pytest` documentation

## 5 :keyboard: :white_check_mark: Exercise 2: Parametrize the fixture  
Use the `mark.parametrize` to parametrize the fixture `personal_info` from the Exercise 1.

todo: setup and finalizer (file from cvs), tmpdir


> [!IMPORTANT]
> Update the repository in order to move to the next week/part of the course:
>  - After finishing all the exercises, create a Pull Request from the `week3` branch to the `main` branch
>  - Check the status of tests
>  - If all tests pass, merge the Pull Request, this should update a new `README.md` on the main page of the repository 
> (you can reload the page after 30-60s if you don't see the new content)
