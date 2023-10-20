import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barycentricvelocity",
    version="0.0.1",
    author="Allison Youngblood",
    author_email="allison.a.youngblood@nasa.gov",
    description="Calculating Earth's Velocity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allisony/barycentricvelocity",
    project_urls={
        "Bug Tracker": "https://github.com/allisony/barycentricvelocity/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

