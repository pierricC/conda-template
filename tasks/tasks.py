"""Main tasks."""
import logging
import os

from invoke import task

logger = logging.getLogger(__name__)
REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


@task
def lint(c):
    """Lint this package."""
    logger.info("Running pre-commits checks...")
    c.run("pre-commit run --all-files --color always", pty=True)


@task
def lab(c):
    """Run Jupyter Lab."""
    notebooks_path = os.path.join(REPO_PATH, "notebooks")
    os.makedirs(notebooks_path, exist_ok=True)
    with c.cd(notebooks_path):
        c.run("jupyter lab --allow-root", pty=True)


@task
def test(c):
    """Test this package."""
    logger.info("Running Pytest...")
    c.run(
        "pytest --cov=src tests",
        pty=True,
    )
