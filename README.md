# Assignment 00 - Data Structures and Algorithms

This repository contains the first problem set for YSC2229: Introduction to Data Structures and Algorithms. This first PSET is designed to test your understanding of Python. You will not need any specific knowledge of advanced data structures or algorithms. The problems involve fundamental operations such as arithmetic calculations, basic data manipulation and simple decision-making processes. Again, I emphasize that you do not need any prior knowledge of data structures or algorithms, such as dynamic programming, hashmaps, or trees, to solve these problems. Furthermore, do not worry if any of the aforementioned terms sound unfamiliar. You will learn about them in the coming weeks.
## Problems
There are 14 problems in the questions folder. The respective tests are in the tests folder. You only need to pass all of the tests to achieve a perfect score on the assignment. Your grade is calculated based on how many of the total tests you pass. 

Please do not add, delete, or change any of the unit tests. I am able to know if you do so through my own program which scans all of your code. If you are found to have done so, you will receive a 0 on the assignment. If you have any questions, please message the student in charge of the problem set on Telegram @yokurang.

Remember to consider all edge cases and extreme values while writing your solutions. The goal is to ensure your function works correctly under all possible scenarios it might encounter.

A note on the PSET: This PSET contains some easier questions and much harder ones. Some of these problems might take a few minutes depending on your proficiency in Python, and others 2 hours or more. Please do not be discouraged if you are unable to solve some of the problems. In case you are stuck, you may

- Make a post in the GitHub classroom discussion board and I will answer them
- Email the peer tutors of the class.

Furthermore, there is no particular order in which you should solve the problem. In fact, in my personal opinion, there is no order that will make the PSET easier. You may choose to solve the problems in any order you wish.

## Submissions
To submit your assignment, you only need to push your code. The autograder will run all of the tests and assign a score based on the number of passing tests. You can push your code as many times as you want. The autograder will only consider your latest submission.

## Setting up Poetry - Python Dependency Management

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. We will use this tool to manage the dependencies for this class.

For further details and troubleshooting, refer to the official [Poetry Documentation](https://python-poetry.org/docs/).

### Installing Poetry

- On macOS/Linux/Unix:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

- On Windows:

    ```bash
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

### Add Poetry to your PATH

After installation, you should add the Poetry command to your PATH. The installer creates a poetry wrapper in a well-known, platform-specific directory:

- `$HOME/.local/bin` on Unix.
- `%APPDATA%\Python\Scripts` on Windows.
- `$POETRY_HOME/bin` if `$POETRY_HOME` is set.

On Unix-based systems (like Linux or MacOS), you can add Poetry to your PATH by appending the following to your `.bashrc` or `.zshrc` file:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then, source the file:

```bash
source ~/.bashrc  # or ~/.zshrc
```

On Windows, the Poetry executable should be automatically added to your PATH after installation. If it's not, you can manually add the directory `%APPDATA%\Python\Scripts` to your PATH.

### Using Poetry

Once Poetry is installed and in your PATH, you can execute the following to confirm the installation:

```bash
poetry --version
```

If you see something like `Poetry (version 1.2.0)`, your install is ready to use!

To update Poetry to the latest version, use the self-update command:

```bash
poetry self update
```

### Setting Up the Virtual Environment

Poetry creates a new virtual environment for each project. To use this environment, use:

```bash
poetry shell
```

This activates the virtual environment for your project.

### Running Pytest

With the virtual environment activated, you can run `pytest` with:

```bash
poetry run pytest
```
### Failure with Poetry Installation 

Try this:
```bash
# Uninstall poetry
curl -sSL https://install.python-poetry.org | python3 - --uninstall

# change to required python
pyenv local 3.10.8 #brew install pyenv if you have not done so already. For Windows users, you will need to install pyenv-win

# activate python
eval "$(pyenv init --path)"

# check python version
python --version

# Install latest poetry
curl -sSL https://install.python-poetry.org | python3 -
```



## Testing

This repository uses `pytest` for unit testing. Each problem has a corresponding test in the `tests` directory. To run the tests, navigate to the repository's root directory and run `pytest`. To run individual tests, run `pytest tests/test_<problem_number>.py`. For example, to run the tests for the weird algorithm problem, run `pytest tests/test_weird_algorithm.py`.

## Autograding

We use GitHub Classroom's autograding feature for this assignment. The autograder runs all `pytest` tests and assigns a score based on the number of passing tests. Please DO NOT change any of the function names or the tests will fail. Furthermore, DO NOT change anything in the .github/workflows directory. If you do so, the autograder will not work and you will receive a 0 on the assignment.

## Lecture Notes

You may reference the official lecture notes on Canvas.

## Plagiarism Notice

We use the Stanford Measure of Software Similarity (MOSS) to detect plagiarism. If your assignment is found to be similar to another student's assignment, both of you will receive a 0 on the assignment. We are serious.

## Contact
For any questions, please contact the student in charge of the problem set on Telegram @yokurang.
