import datetime

import dateutil.parser
import pydantic
import yaml

data = yaml.safe_load(
    """
task: do stuff
date: "2023-02-16"
"""
)


class Task(pydantic.BaseModel):
    task: str
    date: datetime.datetime

    @pydantic.validator("date", pre=True)
    def parse_date_as_datetime_obj(cls, v):
        dt = dateutil.parser.parse(v)
        return dt


task = Task(**data)
print(task)
