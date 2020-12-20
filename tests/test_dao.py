from dynamo_dao import Dao, DynamoObject


class ExampleDao(Dao[str]):
    table_name = "foo"
    unique_key = ["bar"]

    def convert_to_dynamo(self, var: str) -> DynamoObject:
        return {"bar": var}

    def convert_from_dynamo(self, var: DynamoObject) -> str:
        return str(var["bar"])


def test_convert_to_dynamo() -> None:
    a = ExampleDao()

    result = a.convert_to_dynamo("hi")

    assert result == {"bar": "hi"}


def test_convert_from_dynamo() -> None:
    a = ExampleDao()

    result = a.convert_from_dynamo({"bar": "hi"})

    assert result == "hi"
