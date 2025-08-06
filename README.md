# Python Repo Template

This is a **repository template** which can be used for a **Python** _project_ with name `package-name`, or as a standalone repository.
Within the [.github](.github) directory there are issue and pull request _templates_ and custom scripts for use within **GitHub** _workflows_.


## Documentation

The [docs](docs) directory contains documentation for the project, with [index.html]() contained within the [index.md](docs/index.md) **README** file.
We can create documentation for **Python** code automatically `mkdocstrings` plugin for **MkDocs**, within the _markdown_ file as such:

```markdown
::: src.package_name.folder.script
    handler: python
```

Creating subdirectories within the [docs](docs) directory will create subpages within the website.
We can configure the [mkdocs.yml](mkdocs.yml) file to change the theme, plugins and other settings for the documentation.
To create the documentation locally, we can run

```bash
mkdocs build
mkdocs serve
```

Then we can check the _local host_ at [http://localhost:8000](http://localhost:8000) to see the site.


## UV / Requirements

This project uses `uv` as the primary **Python** package dependency.
Within the [pyproject.toml](pyproject.toml) file, we can see the dependencies and other settings for the project.
When initialising a new project, we can run `uv init` and `uv venv` to initialise and create a new _virtual environment_ specific to the project.
To install the requirements, we can run

```bash
uv pip install -r pyproject.toml --extra test --extra docs
```

This will install the `dependencies` section of the [pyproject.toml](pyproject.toml) file, as well as the `test` and `docs` extras.
To add new dependencies or remove them, we can run the following:

```bash
uv add <package-name>
uv add <package-name> --optional <name>
```

and similarly for `remove`; this will automatically update the [pyproject.toml](pyproject.toml) file.
The [.python_version](.python-version) file contains the **Python** version to use for the project, which is set to `3.13`.
The [uv.lock](uv.lock) file contains the locked versions of the dependencies, which can be used to ensure reproducibility of the environment.


## Pre-Commit Hooks

This repository templates uses [pre-commit](https://pre-commit.com/) to run various _hooks_ on the codebase.
This is configured within the [.pre-commit-config.yaml](.pre-commit-config.yaml) file.
To actually initialise this to run, we need to install `pre-commit` (which can be done using `uv` and the [pyproject.toml](pyproject.toml) file).
Then we can run the following command:

```bash
pre-commit install
```

Then at each commit, the hooks will run automatically; we can see the _logs_ within the **git** logging console.
As standard this includes `ruff` for _linting_ and _formatting_ and also `mypy` for _static type checking_.
There are other basic hooks for checking conflicts, **JSON** files etc.


## Branching Strategy

This project uses a **Git** branching strategy based on the [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) model.
We develop _features_ or _bug fixes_ from the `develop` branch, and merge there when complete.
Then periodically updates from `develop` will be merged into the `main` branch.
To actually deploy those changes, we create `releases` in **GitHub** with _tags_ (which would deploy **IaC** changes or deploy to **PyPI** for a package say).
A push into the branch `develop` is set to trigger a deployment to **Test PyPI** for packages.
