"""Example demonstrating CefWebViewSurface with a spinning cube."""

from ursina import Ursina, Entity, color, time
from ursina_webview import CefWebViewSurface


def main() -> None:
    app = Ursina(title="WebView Demo")
    CefWebViewSurface(
        url="https://panda3d.org",
        size=(1024, 768),
        position=(0, 2, 4),
        transparent=True,
    )
    cube = Entity(model="cube", color=color.azure, rotation=(0, 45, 0))

    def update() -> None:
        cube.rotation_y += time.dt * 30

    app.run()


if __name__ == "__main__":
    main()
