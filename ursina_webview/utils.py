"""Utility helpers for ursina_webview."""

from __future__ import annotations

from typing import Optional

from panda3d.core import Texture


def upload_frame_to_texture(texture: Texture, width: int, height: int, data: bytes) -> None:
    """Upload raw BGRA frame bytes to a Panda3D texture."""
    if texture.get_x_size() != width or texture.get_y_size() != height:
        texture.setup_2d_texture(width, height, Texture.T_unsigned_byte, Texture.F_rgba8)
    memory_view = memoryview(data)
    texture.set_ram_image(memory_view)


def ensure_texture(texture: Optional[Texture], width: int, height: int) -> Texture:
    """Ensure a texture object exists and matches the required dimensions."""
    if texture is None:
        texture = Texture()
    if texture.get_x_size() != width or texture.get_y_size() != height:
        texture.setup_2d_texture(width, height, Texture.T_unsigned_byte, Texture.F_rgba8)
    return texture
