from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from uuid import UUID
from pydantic import BaseModel

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_key: UUID
    title: str
    url: str
    media_type: str

class ParsedSitemapModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    titles: list[Title]
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
