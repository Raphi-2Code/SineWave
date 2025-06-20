"""CEF-based implementation of :class:`WebViewSurface`."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Tuple, Union

from ursina import Entity, Vec3
from panda3d.core import Texture

from cefpython3 import cefpython as cef

from .core import WebViewSurface
from .utils import upload_frame_to_texture


class CefWebViewSurface(WebViewSurface):
    """Browser surface implemented with cefpython3."""

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
        self.browser = None
        self._init_cef()
        self._create_browser()
        self.load_url(url)

    def _init_cef(self) -> None:
        settings = {
            "windowless_rendering_enabled": True,
            "multi_threaded_message_loop": False,
            "external_message_pump": False,
        }
        if not cef.GetAppSetting("initialized"):
            cef.Initialize(settings=settings)

    def _on_paint(self, browser: cef.PyBrowser, element_type: int, paint_buffer: bytes, width: int, height: int) -> None:
        """Handle paint events from CEF."""
        if element_type != cef.PET_VIEW:
            return
        upload_frame_to_texture(self.texture, width, height, paint_buffer)

    def _create_browser(self) -> None:
        """Create the off-screen browser."""
        window_info = cef.WindowInfo()
        window_info.SetAsOffscreen(0)
        self.browser = cef.CreateBrowserSync(
            window_info=window_info,
            settings={"windowless_frame_rate": 60},
            url="about:blank",
        )
        self.browser.SetClientHandler(PaintHandler(self))
        self.browser.SendFocusEvent(True)
        self.browser.WasResized()

    def load_url(self, url: str) -> None:
        self.url = url
        if self.browser:
            self.browser.LoadUrl(url)

    def reload(self) -> None:
        if self.browser:
            self.browser.Reload()

    def execute_js(self, script: str) -> Any:
        if self.browser:
            frame = self.browser.GetMainFrame()
            return frame.EvaluateJavaScript(script)
        return None

    def screenshot(self, path: Path) -> None:
        if self.texture:
            self.texture.write(path.as_posix())


class PaintHandler(object):
    """CEF client handler that forwards paint events to the surface."""

    def __init__(self, surface: CefWebViewSurface) -> None:
        self.surface = surface

    def OnPaint(self, browser: cef.PyBrowser, element_type: int, paint_buffer: bytes, width: int, height: int) -> None:
        self.surface._on_paint(browser, element_type, paint_buffer, width, height)
