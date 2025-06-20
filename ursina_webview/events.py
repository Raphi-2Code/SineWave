"""Input translation utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from ursina import held_keys, mouse
from cefpython3 import cefpython as cef


@dataclass
class MouseState:
    """Simplified mouse state."""

    x: int
    y: int
    buttons: Tuple[bool, bool, bool]


def build_cef_mouse_event(state: MouseState) -> dict:
    """Convert :class:`MouseState` to a CEF mouse event dictionary."""
    ev = {
        "x": state.x,
        "y": state.y,
        "modifiers": cef.EVENTFLAG_NONE,
    }
    return ev
