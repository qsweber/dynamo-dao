import pathlib
from setuptools import setup  # type: ignore


setup(
    name="dynamo-dao",
    version="0.0.1",
    description="Dynamo Dao",
    author="Quinn Weber",
    maintainer="Quinn Weber",
    maintainer_email="quinn@quinnweber.com",
    license="MIT",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    package_data={"dynamo_dao": ["py.typed"]},
    packages=["dynamo_dao"],
    package_dir={"": "src"},
    install_requires=["Boto3"],
)
