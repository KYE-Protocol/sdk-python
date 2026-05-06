"""
KYE Protocol™ — Python SDK public entry point.

The v0.1.0a1 public-skeleton release exposes the URN parser/builder and
the public vocabulary constants. The runtime client (decision endpoint,
signing helpers, evidence-pack builder, OSCAL exporter) ships with v1.0 GA.

    from kye_protocol import KyeUrn, EntityClass, DecisionCode

Documentation: https://kye-protocol.github.io/concepts.html
"""
from .urn import KyeUrn, KyeUrnParts
from .vocabulary import (
    EntityClass,
    ENTITY_CLASSES,
    DecisionCode,
    SignalType,
    StateDimension,
    ConformanceLevel,
)

__all__ = [
    "KyeUrn",
    "KyeUrnParts",
    "EntityClass",
    "ENTITY_CLASSES",
    "DecisionCode",
    "SignalType",
    "StateDimension",
    "ConformanceLevel",
    "SPEC_VERSION",
    "SDK_VERSION",
]

#: Spec version this SDK targets.
SPEC_VERSION = "kye-protocol-1.0"
#: Public SDK release. The runtime client ships at v1.0 GA.
SDK_VERSION = "0.1.0a1"
