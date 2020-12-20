# Dynamo Dao

Library for interacting with DynamoDb tables.

## Installation

pip install dynamo-dao

## Usage

```
from typing import NamedTuple

from dynamo_dao import Dao, DynamoObject

class Example(NamedTuple):
    foo: str
    bar: int

class ExampleDao(Dao[Example]):
    table_name = "example"
    unique_key = ["foo"]

    def convert_to_dynamo(self, var: Example) -> DynamoObject:
        return {"foo": var.foo, "bar": var.bar}

    def convert_from_dynamo(self, var: DynamoObject) -> Examle:
        return Example(foo=str(var["foo"]), bar=int(var["bar"]))


example_dao = ExampleDao()

example = Example(foo="hi", bar=1)

example_dao.create(example)
result = example_dao.read_one("foo", "hi")

assert example == result
```
