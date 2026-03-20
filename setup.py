from setuptools import setup, find_packages

setup(
    name="mini-geometry-toolkit",
    version="0.0.1",
    description="A Python toolkit to calculate and visualize geometric shapes",
    author="Your Name",
    author_email="youremail@example.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "geometry-tool=mini_geometry_toolkit.cli:run"
        ],
    },
)