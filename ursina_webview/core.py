"""Core abstractions for ursina_webview."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Tuple, Union

from ursina import Entity, Vec3
from panda3d.core import Texture


class WebViewSurface(Entity):
    """Base class for browser surfaces."""

    def __init__(
        self,
        url: str,
        size: Tuple[int, int],
        position: Union[Vec3, Tuple[float, float, float]],
        *,
        transparent: bool = False,
        input_passthrough: bool = False,
    ) -> None:
        super().__init__(position=position)
        self.url = url
        self.size = size
        self.transparent = transparent
        self.input_passthrough = input_passthrough
        self.texture = Texture()

    def load_url(self, url: str) -> None:
        raise NotImplementedError

    def reload(self) -> None:
        raise NotImplementedError

    def execute_js(self, script: str) -> Any:
        raise NotImplementedError

    def screenshot(self, path: Path) -> None:
        raise NotImplementedError
