"""Conda tasks."""

import logging

from invoke import task

logger = logging.getLogger(__name__)


@task
def create(c):
    """Recreate the conda environment."""
    logger.info("Creating conda environment ")
    c.run("conda-merge environment.run.yml environment.dev.yml > environment.yml")
    c.run("mamba env create --force", pty=True)
    c.run("rm environment.yml", pty=True)


@task
def update(c):
    """Update the conda environment."""
    logger.info("Updating conda environment")
    c.run("conda-merge environment.run.yml environment.dev.yml > environment.yml")
    c.run("mamba env update --prune", pty=True)
    c.run("rm environment.yml", pty=True)
