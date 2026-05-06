"""
KYE Protocol™ URN — public format.

    kye:<entity-class>:<trust-domain>:<subclass>:<local>

Full normative URN spec:
    https://kye-protocol.github.io/protocol.html#urn-format
    https://github.com/KYE-Protocol/id-format
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Final

from .vocabulary import ENTITY_CLASSES

_URN_RE: Final = re.compile(
    r"^kye:([a-z][a-z0-9-]*):([a-z0-9.-]+):([a-z0-9-]+):([a-zA-Z0-9_-]+)$"
)


@dataclass(frozen=True, slots=True)
class KyeUrnParts:
    entity_class: str
    trust_domain: str
    subclass:     str
    local:        str


@dataclass(frozen=True, slots=True)
class KyeUrn:
    entity_class: str
    trust_domain: str
    subclass:     str
    local:        str

    @classmethod
    def parse(cls, urn: str) -> "KyeUrn":
        """Parse a URN string. Raises ValueError if malformed."""
        if not isinstance(urn, str):
            raise TypeError("URN must be a string")
        m = _URN_RE.match(urn)
        if not m:
            raise ValueError(f"Invalid KYE URN: {urn}")
        return cls(
            entity_class=m.group(1),
            trust_domain=m.group(2),
            subclass=m.group(3),
            local=m.group(4),
        )

    @staticmethod
    def is_valid(urn: str) -> bool:
        """True if the URN is well-formed."""
        return isinstance(urn, str) and bool(_URN_RE.match(urn))

    @staticmethod
    def is_public_class(urn: str) -> bool:
        """True if the entity class is one of the public-vocabulary classes."""
        if not KyeUrn.is_valid(urn):
            return False
        return KyeUrn.parse(urn).entity_class in ENTITY_CLASSES

    @classmethod
    def build(
        cls,
        entity_class: str,
        trust_domain: str,
        subclass:     str,
        local:        str,
    ) -> "KyeUrn":
        """Build a URN from its parts; validates each segment."""
        candidate = f"kye:{entity_class}:{trust_domain}:{subclass}:{local}"
        return cls.parse(candidate)

    def __str__(self) -> str:
        return f"kye:{self.entity_class}:{self.trust_domain}:{self.subclass}:{self.local}"
