from setuptools import setup, find_packages

setup(
    name="firebase_fastapi_wrapper",
    version="0.1.0",
    description="Use FastAPI inside Firebase Functions with full HTTP forwarding",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/firebase_fastapi_wrapper",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.110.0",
        "starlette>=0.36.3",
        "firebase-functions>=0.2.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: FastAPI",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.8",
)
