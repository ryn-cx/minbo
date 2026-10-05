from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_key: UUID | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(default=None, union_mode='left_to_right')

class ParsedSitemapModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    titles: list[Title] | Any = Field(default=None, union_mode='left_to_right')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
