import django_subcommands

from django.core.management.base import BaseCommand

from leon.management.subcommands.docs import DocsCommand
from leon.management.subcommands.scaffold import ScaffoldCommand


class Command(django_subcommands.SubCommands):
    
    subcommands = {
        "docs": DocsCommand,
        "scaffold": ScaffoldCommand,
    }