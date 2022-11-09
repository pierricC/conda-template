# Getting started

This a template repository for anyone that want to set up
a new project within a conda environment, mostly aimed for data science.

To get started, simply run:

```bash
./tasks/init.sh <envName>
```

This script does several things:
-  Install vscode extension.
-  Install conda if not installed.
-  Create the conda environment based on the user defined environment.run.yml and environment.dev.yml.
-  Install pre-commit hooks and configure git.

Note: Since we are using mamba in order to create the environment faster,
be sure the directory `/anaconda/pkg/cache/` has user permission.


# Tasks CLI

Once installed and within the new environment, 
User can start using the invoke cli command to perform several actions 
such as :
```
  invoke lab            Run Jupyter Lab.
  invoke lint           Lint this package.
  invoke test           Test this package.
  invoke conda.create   Recreate the conda environment.
  invoke conda.update   Update the conda environment.
```