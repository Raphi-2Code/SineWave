import sys
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest


class DummyBrowser:
    def __init__(self) -> None:
        self.loaded_url: str | None = None
        self.frame = MagicMock()

    def LoadUrl(self, url: str) -> None:
        self.loaded_url = url

    def Reload(self) -> None:
        pass

    def GetMainFrame(self) -> MagicMock:
        return self.frame


class DummyCEF:
    def __init__(self) -> None:
        self.settings: dict | None = None

    def GetAppSetting(self, name: str) -> bool:
        return False

    def Initialize(self, settings: dict) -> None:
        self.settings = settings

    def CreateBrowserSync(self, **kwargs) -> DummyBrowser:
        return DummyBrowser()


@pytest.fixture
def mock_cef(monkeypatch: pytest.MonkeyPatch) -> DummyCEF:
    dummy = DummyCEF()
    monkeypatch.setitem(sys.modules, "cefpython3", SimpleNamespace(cefpython=dummy))
    yield dummy
    sys.modules.pop("cefpython3", None)


def test_load_url_updates_browser(mock_cef: DummyCEF) -> None:
    from ursina_webview.cef_surface import CefWebViewSurface

    surface = CefWebViewSurface.__new__(CefWebViewSurface)
    WebViewSurface_init = CefWebViewSurface.__mro__[1].__init__
    WebViewSurface_init(surface, "about:blank", (640, 480), (0, 0, 0))
    surface.browser = DummyBrowser()
    surface.load_url("https://example.com")
    assert surface.browser.loaded_url == "https://example.com"
