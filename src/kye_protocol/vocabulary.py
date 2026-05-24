"""
KYE Protocol™ — public vocabulary constants.

Mirrors `public/vocabulary/` in the spec repo. These values are stable
across the v1.x series and used as discriminators in every KYE Protocol™
schema.
"""
from __future__ import annotations

from typing import Final


class EntityClass:
    HUMAN:      Final = "human"
    BUSINESS:   Final = "business"
    AGENT:      Final = "agent"
    SERVICE:    Final = "service"
    MODEL:      Final = "model"
    TOOL:       Final = "tool"
    WORKFLOW:   Final = "workflow"
    RESOURCE:   Final = "resource"
    CAPABILITY: Final = "capability"
    CREDENTIAL: Final = "credential"
    TRUST:      Final = "trust"
    CARD:       Final = "card"
    WALLET:     Final = "wallet"


ENTITY_CLASSES: Final = (
    EntityClass.HUMAN,
    EntityClass.BUSINESS,
    EntityClass.AGENT,
    EntityClass.SERVICE,
    EntityClass.MODEL,
    EntityClass.TOOL,
    EntityClass.WORKFLOW,
    EntityClass.RESOURCE,
    EntityClass.CAPABILITY,
    EntityClass.CREDENTIAL,
    EntityClass.TRUST,
    EntityClass.CARD,
    EntityClass.WALLET,
)


class DecisionCode:
    """The three canonical decision codes returned by POST /v1/runtime/authorize."""
    ALLOW_WITH_CONSTRAINTS: Final = "allow_with_constraints"
    REQUIRE_APPROVAL:       Final = "require_approval"
    DENY:                   Final = "deny"


class SignalType:
    """Signal types emitted by the protocol's runtime control surface.

    The specific signal-type enumeration and the propagation construction
    are part of the patent track and are not disclosed in this repository.
    """
    STOP:       Final = "stop"
    QUARANTINE: Final = "quarantine"
    REVOKE:     Final = "revoke"
    RESTORE:    Final = "restore"
    REPLAY:     Final = "replay"


class StateDimension:
    """State-dimension labels used by the canonical state vector.

    The specific dimension enumeration, per-dimension state alphabets,
    and the composition rule used at decision time are part of the
    patent track and are not disclosed in this repository.
    """
    LIFECYCLE:  Final = "lifecycle"
    AUTHORITY:  Final = "authority"
    DELEGATION: Final = "delegation"
    CREDENTIAL: Final = "credential"
    RECOVERY:   Final = "recovery"
    RISK:       Final = "risk"


class ConformanceLevel:
    """The 5-tier KYE Conformance & Certification Programme™ ladder."""
    L0_DECLARED:      Final = "L0_declared"
    L1_SELF_TESTED:   Final = "L1_self_tested"
    L2_SELF_ATTESTED: Final = "L2_self_attested"
    L3_CONFORMANT:    Final = "L3_conformant"
    L4_CERTIFIED:     Final = "L4_certified"
