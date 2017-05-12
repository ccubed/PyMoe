#Testing

##Running tests
1. Clone this repository.
1. Navigate into the PyMoe folder.
1. Run the tests, which use Python's `unittest`.

```zsh
$ git clone https://github.com/ccubed/PyMoe.git
$ cd PyMoe
$ python -m unittest Pymoe/tests/Hummingbird/Hummingbird_tests.py
```

One goal is to reduce running the tests to `python -m unittest Pymoe/tests` or,
if specificicity is desired, `python -m unittest Pymoe/tests/Hummingbird`
