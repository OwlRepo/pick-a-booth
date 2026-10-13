import logging

import pytest

from photobooth.services.config.groups.uisettings import GroupUiSettings
from photobooth.services.config.models.frameoverlay import FrameOverlay

DELETED_UPSTREAM_FRAME = "userdata/demoassets/frames/frame_image_photobooth-app.png"
EXISTING_FRAME = "userdata/demoassets/frames/pixabay-poster-2871536_1920.png"


def test_error_missing_frame_file_disables_overlay_instead_of_failing():
    overlay = FrameOverlay.model_validate({"enable": True, "image": DELETED_UPSTREAM_FRAME, "mirror_effect": True})
    assert overlay.enable is False
    assert overlay.image is None
    assert overlay.mirror_effect is True


def test_edge_missing_frame_file_logs_a_warning(caplog: pytest.LogCaptureFixture):
    with caplog.at_level(logging.WARNING):
        FrameOverlay.model_validate({"enable": True, "image": DELETED_UPSTREAM_FRAME})
    assert DELETED_UPSTREAM_FRAME in caplog.text


def test_regression_saved_uisettings_with_deleted_upstream_frame_still_loads():
    ui = GroupUiSettings.model_validate({"livestream_frameoverlay": {"enable": True, "image": DELETED_UPSTREAM_FRAME, "mirror_effect": True}})
    assert ui.livestream_frameoverlay.enable is False
    assert ui.livestream_frameoverlay.image is None


def test_happy_existing_frame_file_is_kept():
    overlay = FrameOverlay.model_validate({"enable": True, "image": EXISTING_FRAME})
    assert overlay.enable is True
    assert overlay.image is not None and overlay.image.as_posix() == EXISTING_FRAME
