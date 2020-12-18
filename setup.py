from setuptools import setup

setup(
    name="dynamo-dao",
    version="0.0.1",
    description="Service Template",
    author="Quinn Weber",
    maintainer="Quinn Weber",
    maintainer_email="quinn@quinnweber.com",
    package_dir={"": "src"},
    install_requires=["Boto3"],
)
