# ursina_webview

Browser WebView integration for Ursina using `cefpython3` with optional PyQt6 fallback.

**Note**: `cefpython3` ships with an old Chromium build. Consider using the Qt fallback if you need newer web features.

## Running the example

```bash
pip install ursina cefpython3
python -m ursina_webview.examples.spinning_cube_with_webview
```
