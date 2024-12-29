<header>

<!--
  <<< Author notes: Course header >>>
  Read <https://skills.github.com/quickstart> for more information about how to build courses using this template.
  Include a 1280×640 image, course name in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Next to "About", add description & tags; disable releases, packages, & environments.
  Add your open source license, GitHub uses the MIT license.
-->

</header>

<!--
  <<< Author notes: Step 1 >>>
  Choose 3-5 steps for your course.
  The first step is always the hardest, so pick something easy!
  Link to docs.github.com for further explanations.
  Encourage users to open new tabs for steps!
  TBD-step-1-notes.
-->


# Week 1: Introduction to testing in Python

In the first part of the course, we will learn basic information about testing 
of the code, in particular testing in Python.

## 1 :book: Why do we test the code?

Testing software is an important step in the development process.
A good set of tests can help you to ensure that the code:
- fulfills its requirements; 
- provides reliable output under various conditions; 
- is compatible with different systems and environments. 

Additionally, tests can help you to:
- makes you think about desirable output;
- improves readability of your code.


## 2 :book: Various types of tests

### Unit tests

- work on isolated parts (units) of the program
- verify that units operate correctly in various scenarios
- usually compare observed results to well known expected results

### Integration tests

- combine individual software modules and test as a group;
- similar structure as unit tests: compare observed results to expected results, 
but the expected result can be more complicated to represent.

### Regression tests

- verify that software previously developed and tested still performs correctly 
even after it was changed or interfaced with other software;
- you don't have to know the expected result, the assumption is that the past results were correct.

## 3 :book: Science and software testing

- We all question/test many things in our scientific work

- When writing a program, we often execute a simple example first and check the output

Writing software tests for your scientific code is:
- translating your ideas for verification to programming code
- automating the process of verification, so you can do it on a regular basis

In case you are still not convinced, I recommend reading the following articles: 
- [The most infamous bugs in the history of software development](https://historyofcomputers.eu/software/historys-worst-software-error-top-9-disasters/)
- [A Prof. Geoffrey Chang story who had to retract 5 articles (3 from Science, PNAS, J.Mol.Biol.)](https://www.science.org/doi/10.1126/science.314.5807.1856)


## 4 :book: The `assert` statement

The simplest way of testing in Python is using the `assert` statement.
The `assert` statement is used to check the condition. 
If the condition is `True`, the program will continue to execute.
If the condition is `False`, the program will raise an `AssertionError`.
For example, if you run:

```python
assert 2 == 1 + 1
```
the program will continue to execute, because `2 == 1 + 1` is `True`.
However, if you run:
```python
assert 3 == 1 +1
```
the program will raise an `AssertionError`, because `3 == 1 + 1` is `False`.

However, the `assert` statement doesn't have to be used only for simple conditions, 
where you compare if two values are equal by using `==`.
You can use the `assert` statement to check:
  - if one value is bigger than the other, e.g., `assert 3 > 2`
  - if one value is in the list, e.g., `assert 'a' in ['a', 'b', 'c']`
  - if one value is NOT in the list, e.g., `assert 'd' not in ['a', 'b', 'c']`
  - if the length of the list is equal to 3, e.g., `assert len(['a', 'b', 'c']) == 3`
  - if the key is in the dictionary, e.g., `assert 'key' in {'key': 'value'}`
  - if a value is an instance of a class, e.g., `assert isinstance(3, int)`


## 5 :keyboard: Practicing using the assert command in Python

> [!TIP]
> - I recommend opening another browser tab with this repository, so you can keep these instructions open for reference all the time.
> - In case you haven't used Codespace before, I will provide very detailed steps for this first exercise.

1. Open Codespace on `week1` branch.
  <details>
  <summary>If you don't remember how to open the Codespace, expand this line to see all steps</summary>
    
    - Start from the landing page of your repository opened in new tab.
    - Change the branch to "week1" (you should see a new content that was not in the `main` branch)
    - Click the green "Code" button located in the middle of the page.
    - Select the Codespaces tab in the box that pops up and then click the "Create codespace on week1" button.
    - Verify your codespace is running. The browser should contain a VS Code web-based editor and a terminal.
    - In the terminal, move to the `week1` directory that is the working directory for this week.
    (if you don't see this directory, you're likely in a wrong branch).    
  </details>


2. Open a Python interpreter (run `python` command in the terminal)
3. Practice using the `assert` statement, for example:
   - check if letter "a" in your name
   - create a list and check if the length of the list is 3
   - create a dictionary and check if the key `name` is in the dictionary
   - if the key `name` exists, check if its value is "John"
   - check if the sum of two numbers is equal to 10
   - check if a number is even
   - check if `pi` from the `math` module is a float
   - check if `pi` from the `math` module is equal to 3.14

## 6 :book: Using the assert statement to test a function
Similarly, you can use the `assert` statement to test your functions.
Let's say your task is to write a function that finds prime factors
of a number, `prime_factors`, you could use the `assert` statement to check if the
function works correctly for an example:
```python
assert prime_factors(8) == [2, 2, 2]
```
You will get no output if the function `prime_factors` works correctly for the example.
If you get an output, it means that the function `prime_factors` does not return the expected output.
The simplest way of using the `assert` doesn't give too much information in case the function doesn't work correctly.

In order to get any meaningful information, you would have to add a message to the `assert` statement, e.g.
```python
assert prime_factors(8) == [2, 2, 2], f"The prime factors of 8 should be [2, 2, 2], but it is {prime_factors(8)}"
```
This way, you will get a meaningful message if the function doesn't work as expected.

Of course, this is only one example, you would likely want to check the function for more examples, e.g.
```python
assert prime_factors(8) == [2, 2, 2], f"The prime factors of 8 should be [2, 2, 2], but it is {prime_factors(8)}"
assert prime_factors(18) == [2, 3, 3], f"The prime factors of 18 should be [2, 3, 3], but it is {prime_factors(18)}"
assert prime_factors(108) == [2, 2, 3, 3, 3], f"The prime factors of 108 should be [2, 2, 3, 3, 3],  but it is {prime_factors(108)}"
```

In order to automate the process, we can create a function `test_prime_factors` that will check 
if the function returns the expected output for all the examples and run this function in the `__main__` block 
in order to run the tests when the script is executed, e.g.:
```python
def test_prime_factors():
    assert prime_factors(8) == [2, 2, 2], f"The prime factors of 8 should be [2, 2, 2], but it is {prime_factors(8)}"
    assert prime_factors(18) == [2, 3, 3], f"The prime factors of 18 should be [2, 3, 3], but it is {prime_factors(18)}"
    assert prime_factors(108) == [2, 2, 3, 3, 3], f"The prime factors of 108 should be [2, 2, 3, 3, 3],  but it is {prime_factors(108)}"

if __name__ == "__main__":
    test_prime_factors()
```

## 7. :keyboard: :white_check_mark: Exercise 1: Creating the first test function
> [!TIP]
> - This exercise has :keyboard: and :white_check_mark:, that means you will have a specific task and the output will be checked by automatic tests I wrote for this course, and the repository will move to **Part 2** after the task is completed.
> - This is our first exercise of this type in this course, so I will provide very detailed steps to guide you.

1. Go to terminal in Codespace (you can use the one that you opened in part 5, or follow the instruction from that part to open again)
2. Run the script `week1/prime_factors.py`:
  - Go to `week1` directory (if you don't see this directory, you're likely in a wrong branch)
  - Check the content of `prime_factors.py`, you should see the function `prime_factors` that finds prime factors of a number,
and the function `test_prime_factors` that checks if the function works correctly for the number `8`.
  - Run the script `prime_factors.py` by executing `python prime_factors.py` in the terminal. Do you see any output?
3. Update the script `week1/prime_factors.py`:
  - It is nice to have some confirmations that the tests actually run and all results were as expected. 
Let's add a print statement after the execution `test_prime_factors` and run the script again.
  - Add additional examples to the test function `test_prime_factors`, check the output for the numbers `18` and `108`, and run the script again. What do you see? 
  - Add a message to the `assert` statement for each example in the `test_prime_factors` function, in order to see more information about the error, and run the script again.
4. Fix the function `prime_factors`:

Now you should know that the function doesn't work correctly for number `18`.
It is pretty common situation, that your function works well for one example, but doesn't work for all. 
You have to find what causes it, and fix the function.
**One important thing to notice is that you actually don't know if the function works correctly for the number `108`,
since your testing function rises an `AssertionError` for the number `18` and stops the execution.**
  - Try to read carefully the function `prime_factors` and find the reason it doesn't work for the number `18`.
  - Try to fix the function `prime_factors` and with every change, run the script `prime_factors.py` to check if the function works correctly for all the examples.
  - If you can't find the reason the function doesn't work, you can take a look at the solution in the `week1/solutions` directory, and correct the function in the `week1/prime_factors.py` file. Don't forget to run the script again to check if the function works correctly for all the examples!
5. Commit your changes:
  - Use Codespace to commit your changes (you can either use terminal or the "Source Control" tab that is in the main panel on the left)
6. Create a Pull Request to the `main` branch:
  - Use GitHub interface to create a Pull Request
  - Check the status of tests
  - If all tests pass, merge the Pull Request, this should update a new `README.md` on the main page of the repository (you can reload the page after 30-60s if you don't see the new content)


## 8. Summary
Today you learned about the importance of testing in software development, and you practiced using the `assert` statement in Python.
You also learned how to use the `assert` statement to test your functions, and you created a test function that checks if the function `prime_factors` works correctly for the examples.

**Good job for today! Next time we will learn more about testing in Python, and we will use the `pytest` library.**

> [!IMPORTANT]
> Following all the steps from part 7, including creating and merging the Pull Request, is necessary to move to the next parts of the course.

<footer>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Submit an issue](https://github.com/scientific-software-lessons/pytest-introduction/issues)

Work was founded by [BSSw Fellowship Program](https://bssw.io/pages/bssw-fellowship-program)

[MIT License](https://gh.io/mit)

</footer>
