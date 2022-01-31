from setuptools import setup

with open("README.txt", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="retrogamelib3",
    version="3.0",
    description="Retro game library",
    author="pymike and saluk",
    license="LGPL 2.1",
    long_description=long_description,
    long_description_content_type="text",
    packages=["retrogamelib"],
    install_requires=["pygame"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
    ]
)
