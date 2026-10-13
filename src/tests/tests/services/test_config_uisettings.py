import pytest
from pydantic import ValidationError

from photobooth.services.config.groups.actions import GroupActions
from photobooth.services.config.groups.uisettings import GroupUiSettings

PARTY = ["#ff4d2e", "#ff3d9a", "#ffc933", "#3d6bff", "#22d39a"]


def test_error_theme_palette_rejects_four_colors():
    with pytest.raises(ValidationError):
        GroupUiSettings(theme_palette=PARTY[:4])


def test_error_theme_palette_rejects_six_colors():
    with pytest.raises(ValidationError):
        GroupUiSettings(theme_palette=PARTY + ["#000000"])


def test_error_theme_palette_rejects_invalid_color():
    with pytest.raises(ValidationError):
        GroupUiSettings(theme_palette=PARTY[:4] + ["not-a-color"])


def test_edge_theme_palette_named_and_rgb_colors_serialize_as_long_hex():
    ui = GroupUiSettings(theme_palette=["red", "#fff", "rgb(0,0,255)", "#3d6bff", "#22d39a"])
    assert ui.model_dump(mode="json")["theme_palette"] == ["#ff0000", "#ffffff", "#0000ff", "#3d6bff", "#22d39a"]


def test_edge_theme_palette_schema_bounds():
    schema = GroupUiSettings.model_json_schema()["properties"]["theme_palette"]
    assert schema["minItems"] == 5 and schema["maxItems"] == 5
    assert schema["default"] == PARTY


def test_regression_livestream_frameoverlay_default_has_no_upstream_frame():
    overlay = GroupUiSettings().livestream_frameoverlay
    assert overlay.enable is False and overlay.image is None


def test_regression_image_action_default_has_no_upstream_frame_or_text():
    processing = GroupActions().image[0].processing
    assert processing.img_frame.enable is False and processing.img_frame.image is None
    assert processing.texts_enable is False
    assert all("photobooth-app" not in t.text for t in processing.texts)


def test_happy_theme_palette_default_is_party():
    assert GroupUiSettings().model_dump(mode="json")["theme_palette"] == PARTY


def test_happy_frontpage_text_default_is_plain_brand():
    assert GroupUiSettings().FRONTPAGE_TEXT == "Pick-a-Booth"
