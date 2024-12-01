from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class ConfiguredBaseModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
