"""Package tasks."""

from invoke import Collection

from . import conda
from .tasks import lab, lint, test

ns = Collection()
ns.add_task(lab)
ns.add_task(lint)
ns.add_task(test)
ns.add_collection(conda)
