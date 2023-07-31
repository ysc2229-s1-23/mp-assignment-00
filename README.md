# Assignment 01 - Data Structures and Algorithms

This repository contains assignments that focus on various data structures and algorithms problems sourced from the CSES problem set.

## Problems

In all of the problems, remember to handle edge cases and extreme values appropriately.

## Poetry - Python Dependency Management# Assignment 01 - Data Structures and Algorithms

This repository contains assignments that focus on various data structures and algorithms problems sourced from the CSES problem set.

## Setting up Poetry - Python Dependency Management

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

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

We use GitHub Classroom's autograding feature for this assignment. The autograder runs all `pytest` tests and assigns a score based on the number of passing tests.

## Lecture Notes

Please refer to the link in the GitHub Classroom for the lecture notes related to these problems.

## Plagiarism Notice

We use sophisticated plagiarism detection software to ensure the integrity of the assignment submissions. Any attempt to plagiarize will result in a direct fail. Also, remember, using AI such as ChatGPT or similar to generate solutions for assignments is strictly prohibited and may also result in a direct fail.

Remember, the best way to learn programming and problem solving is by doing. Good luck!
