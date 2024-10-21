import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()





setuptools.setup(
    name="Potato_disease_predictor",
    version="0.0.0",
    author="Arun",
    author_email="erarunkumawat50@gmail.com",
    description="A small Python package for CNN app",
    long_description= long_description,
    long_description_content_type="text/markdown",



)