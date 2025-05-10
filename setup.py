#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="pyagentmesh",
    version=open("pyproject.toml").readlines()[2].split('"')[-2],
    keywords="epsilla",
    author="Epsilla Team",
    author_email="info@epsilla.com",
    description="Epsilla AgentMesh",
    long_description="Epsilla AgentMesh",
    license="Apache License",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "sentry_sdk", "pydantic"],
    url="https://github.com/epsilla-cloud/agentmesh",
    project_urls={
        "Source": "https://github.com/epsilla-cloud/agentmesh",
    },
)
