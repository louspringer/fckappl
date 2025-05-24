from setuptools import setup, find_packages

setup(
    name="fckappl",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # ✅ REQUIRED to map module location
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "fckappl = fckappl.__main__:app",
        ],
    },
)
