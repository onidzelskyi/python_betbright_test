Python test for BetBright company
=================================

## Project' structure ##
```
docs/
    PythonDeveloperTest.pdf     Test task description document

python_betbright_test/
    __init__.py                 Package file
    tools.py                    Implementation of test tasks

tests/
    test_tools.py               Tests of product category classification model

main.py                         Examples of using

LICENSE                         License file

README.md                       This file with short description of project

requirements.txt                Requirements of libraries and packages

setup.py                        Setup file for package installation
```

## Environment setup ##

Install virtualenv

```bash
sudo apt install python-pip
pip install virtualenvwrapper
```

Add next lines to ~/.bashrc (~/.profile)

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel

# load virtualenvwrapper for python (after custom PATHs)
venvwrap="virtualenvwrapper.sh"
/usr/bin/which $venvwrap
if [ $? -eq 0 ]; then
    venvwrap=`/usr/bin/which $venvwrap`
    source $venvwrap
fi
```

Run script

```bash
. ~/.local/bin/virtualenvwrapper.sh
```

Create virtual environment

```bash
mkvirtualenv -p python2.7 betbright
```

## Install dependencies ##

```bash
pip install -r requirements.txt
```

## install the package locally (for use on our system) ##

```bash
pip install -e .
```

## Run tests ##

```bash
pytest tests
```

## Run demo app ##

```bash
python main.py
```

## Check PEP008 code style ##

```bash
flake8  --max-line-length=120 .
```