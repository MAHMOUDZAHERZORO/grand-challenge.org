from typing import Tuple

import magic
import os
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MimeTypeValidator(object):
    allowed_types = ()

    def __init__(self, *, allowed_types: Tuple[str, ...]):
        self.allowed_types = tuple(x.lower() for x in allowed_types)
        super(MimeTypeValidator, self).__init__()

    def __call__(self, value):
        mimetype = magic.from_buffer(value.read(1024), mime=True)
        value.seek(0)

        if mimetype.lower() not in self.allowed_types:
            raise ValidationError(f'File of type {mimetype} is not supported. '
                                  'Allowed types are '
                                  f'{", ".join(self.allowed_types)}.')

    def __eq__(self, other):
        return (
            isinstance(other, MimeTypeValidator) and
            set(self.allowed_types) == set(other.allowed_types)
        )

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(MimeTypeValidator) + 7 * hash(self.allowed_types)


@deconstructible
class ExtensionValidator(object):
    """
    Performs soft validation of the filename. Usage:

        validators=[
            ExtensionValidator(
                allowed_extensions=(
                    '.tar',
                    )
                ),
            ],

    """
    allowed_extensions = ()

    def __init__(self, *, allowed_extensions: Tuple[str, ...]):
        self.allowed_extensions = tuple(x.lower() for x in allowed_extensions)
        super(ExtensionValidator, self).__init__()

    def __call__(self, value):
        try:
            self._validate_filepath(value.name)
        except AttributeError:
            # probably passed a list
            for v in value:
                self._validate_filepath(v.name)

    def _validate_filepath(self, s):
        _, extension = os.path.splitext(s)

        if extension.lower() not in self.allowed_extensions:
            raise ValidationError(f'File of type {extension} is not supported.'
                                  ' Allowed types are '
                                  f'{", ".join(self.allowed_extensions)}.')

    def __eq__(self, other):
        return (
            isinstance(other, ExtensionValidator) and
            set(self.allowed_extensions) == set(other.allowed_extensions)
        )

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(ExtensionValidator) + 7 * hash(self.allowed_extensions)
