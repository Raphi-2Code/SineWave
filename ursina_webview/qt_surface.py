"""PyQt6-based WebView fallback."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Tuple, Union

try:
    from PyQt6.QtWebEngineWidgets import QWebEngineView
    from PyQt6.QtWidgets import QApplication
    QT_AVAILABLE = True
except Exception:  # pragma: no cover - optional dependency
    QT_AVAILABLE = False

from ursina import Vec3

from .core import WebViewSurface


class QtWebViewSurface(WebViewSurface):
    """Fallback WebView surface using PyQt6."""

    def __init__(
        self,
        url: str,
        size: Tuple[int, int],
        position: Union[Vec3, Tuple[float, float, float]],
        *,
        transparent: bool = False,
        input_passthrough: bool = False,
    ) -> None:
        super().__init__(url, size, position, transparent=transparent, input_passthrough=input_passthrough)
        if not QT_AVAILABLE:
            raise RuntimeError("PyQt6 is not available")
        if QApplication.instance() is None:
            self.app = QApplication([])
        else:
            self.app = QApplication.instance()
        self.view = QWebEngineView()
        self.view.resize(*size)
        self.view.setAttribute(12, transparent)  # 12 = WA_TranslucentBackground
        self.load_url(url)

    def load_url(self, url: str) -> None:
        self.url = url
        self.view.setUrl(url)  # type: ignore[arg-type]

    def reload(self) -> None:
        self.view.reload()

    def execute_js(self, script: str) -> Any:
        return self.view.page().runJavaScript(script)

    def screenshot(self, path: Path) -> None:
        pixmap = self.view.grab()
        pixmap.save(str(path), "PNG")
