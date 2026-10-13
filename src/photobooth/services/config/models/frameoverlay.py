import logging
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, FilePath, model_validator

logger = logging.getLogger(__name__)


class FrameOverlay(BaseModel):
    enable: bool = Field(
        default=False,
        description="Enable to overlay to be displayed.",
    )
    image: FilePath | None = Field(
        # factories are not part of json schema export. path is not json convertible so it would warn and not include the default. using factory, we skip the warning for same outcome.
        default=None,
        description="This image frame is overlayed the camera images. This image determines the output image size and aspect ratio during image processing. Photos are visible through transparant parts, so the overlay should be in PNG format usually.",
        json_schema_extra={"list_api": "/api/admin/enumerate/userfiles"},
    )
    mirror_effect: bool = Field(
        default=False,
        description="Flip the overlay image horizontally. This can be when the livestream is also flipped (mirror-effect on) as it helps users to gather and align in the scene. Text in the overlay appears in the wrong direction but the final image is correct as the effect is only applied during display, not job processing.",
    )

    @model_validator(mode="before")
    @classmethod
    def _disable_when_image_missing(cls, data: Any) -> Any:
        # a saved config may point at a frame that was removed (e.g. the dropped upstream demo frame);
        # failing validation would stop the app at startup with no way to fix it from the admin UI
        if isinstance(data, dict) and data.get("image") and not Path(data["image"]).is_file():
            logger.warning(f"frame overlay image '{data['image']}' not found, overlay disabled. Select another frame in the admin settings.")
            return {**data, "enable": False, "image": None}
        return data
