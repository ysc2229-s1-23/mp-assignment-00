# Assignment 00 - Data Structures and Algorithms

This repository contains the first problem set for YSC2229: Introduction to Data Structures and Algorithms. This first PSET is designed to test your understanding of Python. You will not need any specific knowledge of advanced data structures or algorithms. The problems involve fundamental operations such as arithmetic calculations, basic data manipulation and simple decision-making processes. Again, I emphasize that you do not need any prior knowledge of data structures or algorothms, such as dynamic programming, hashmaps, or trees, to solve these problems. Furthermore, do not worry of any of the aforementioned terms sound unfamiliar. You will learn about them in the coming weeks.
## Problems
There are 12 problems in the questions folder. The respective tests are in the tests folder. You only need to pass all of the tests to achieve a perfect score on the assignment. Your grade is calculated based on how many of the total tests you pass.

Please do not add, delete, or change any of the unit tests. I am able to know if you do so through my own program which scans all of your code. If you are found to have done so, you will receive a 0 on the assignment. If you have any questions, please message the student in charge of the problem set on Telegram @yokurang.

Remember to consider all edge cases and extreme values while writing your solutions. The goal is to ensure your function works correctly under all possible scenarios it might encounter.

## Submissions
To submit your assignment, you only need to push the code. The autograder will run all of the tests and assign a score based on the number of passing tests. You can push your code as many times as you want. The autograder will only consider your latest submission.

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
pytest
```

## Testing

This repository uses `pytest` for unit testing. Each problem has a corresponding test in the `tests` directory. To run the tests, navigate to the repository's root directory and run `pytest`.

## Autograding

We use GitHub Classroom's autograding feature for this assignment. The autograder runs all `pytest` tests and assigns a score based on the number of passing tests. Please DO NOT change any of the function names or the tests will fail. Furthermore, DO NOT change anything in the .github/workflows directory. If you do so, the autograder will not work and you will receive a 0 on the assignment.

## Lecture Notes

You may reference the official lecture notes on Canvas. However, if you wish to check out the unofficial lecture notes by @yokurang, you may do so [here](https://ysc2229-website.vercel.app/)

## Plagiarism Notice

We use sophisticated plagiarism detection software to ensure the integrity of the assignment submissions. Any attempt to plagiarize will result in a direct fail. Also, remember, using AI such as ChatGPT or similar to generate solutions for assignments is strictly prohibited and may also result in a direct fail.

## Contact
For any questions, please contact the student in charge of the problem set on Telegram @yokurang.
