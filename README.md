# saman
Large file encryption


## Code Complexity
- [lizard](https://pypi.org/project/lizard/)
- [radon](https://pypi.org/project/radon/)

### Lizard
`lizard -x'*/tests/*' -l python -w saman`

### Radon
```
radon cc --min B --average --total-average saman 
radon mi --min B saman 

# ignore folders
# radon cc --min B --average --total-average -i "tests,migrations" saman 
# radon mi --min B -i "tests,migrations" saman 
```


## Documentation
- [sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html)

### Sphinx

```
cd docs
sphinx-quickstart
```

Answer the prompts, the defaults are fine.

For sphinx to detect the module directories correctly, edit conf.py and add the following:

```
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
```

To configure Markdown support:

```
pip install --upgrade recommonmark

# Edit conf.py
extensions = ['recommonmark']
```

Documentation can then be generated with:

```
cd docs
make html
```

## Development Tools
- [ipython](https://ipython.readthedocs.io/en/stable/)
- [ipdb](https://pypi.org/project/ipdb/)
- [pre-commit](https://pre-commit.com/)

### Pre-Commit

`pre-commit install` to add the hooks to the repo


## Formatting/Styling
- [black](https://black.readthedocs.io/en/stable/)
- [isort](https://pypi.org/project/isort/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [flake8-blind-except](https://pypi.org/project/flake8-blind-except/)
- [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
- [flake8-coding](https://pypi.org/project/flake8-coding/)
- [flake8-commas](https://pypi.org/project/flake8-commas/)
- [flake8-debugger](https://pypi.org/project/flake8-debugger/)
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
- [flake8-isort](https://pypi.org/project/flake8-isort/)
- [flake8-quotes](https://pypi.org/project/flake8-quotes/)
- [flake8-sfs](https://pypi.org/project/flake8-sfs/)
- [pydocstyle](https://pypi.org/project/pydocstyle/)

### Black

`black saman`

Configuration options are set in `pyproject.toml`.

### Isort

`isort saman/*.py`

### Flake8

`flake8 saman`

The following plugins are used:

- flake8-blind-except - Checks for blind/catch-all `except:` statements
- flake8-bugbear - Find common bugs and design problems
- flake8-coding - Ensure file contains magic `coding` comment
- flake8-commas - Checks commas exist in different places
- flake8-debugger - Checks for pdb/ipdb imports and set traces
- flake8-docstrings - Runs `pydocstyle` to check docstrings format
- flake8-isort - Check if the imports are sorted in the way you expect
- flake8-quotes - Check that a specific quote type is used. Prefer double.
- flake8-sfs - Check string format. Prefer f-strings.

### Pydocstyle

`pydocstyle saman` 

## Security
- [bandit](https://pypi.org/project/bandit/)

### Bandit

`bandit -r saman`

To exclude directories from checks, add a `.bandit` file:

```
[bandit]
exclude: tests
```

## Type Hints
- [mypy](https://mypy.readthedocs.io/en/latest/)

### Mypy

`mypy saman`
