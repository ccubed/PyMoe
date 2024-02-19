# Building
This is a short document explaining the build pipeline I have setup for this project in case you want to build from source.

## Tools Used
!!! note inline end "Required Tools"

    The only required tool for building is Poetry. You can technically skip this requirement, but the project is setup to use Poetry's build pipeline so you're on your own for configuring another build pipeline.

* [Poetry](https://python-poetry.org/)
* [Task](https://taskfile.dev/)
* [Black Code Formatter](https://github.com/psf/black)
* [isort Code Formatter](https://github.com/PyCQA/isort)

## Building
### Using Poetry
Clone the repository into a folder, CD into that folder and then...
```python
poetry install --sync
poetry build
cd dist
pip install pymoe-2.2-py3-none-any.whl # Or whatever your whl ends up being named
```

### Using Task
If you have Task installed on your machine, you can run a task to build the project. This method still requires Poetry as Task will run poetry commands to ensure a clean build environment.

```
task run make-build
```

This might take a bit to run as it will clean the environment, setup the cleaning environment, run Black and isort against the code, clean the environment, and finally build the sdist and wheel.

There are a few other tasks you might be interested in:

* __serve-docs__ will build and serve the documentation locally.
* __run-pytest__ will setup a testing environment and run through the unit tests.

You can get a full list of available tasks by running `task --list` in the directory you cloned. The unittests take around five minutes because there is a forced two second waiting period between each request to lessen the impact on the API providers.