#!/usr/bin/env python3

import os
from aws_cdk import core
from eks.eks_construct import EksConstruct

app = core.App()



name = app.node.try_get_context("name")
region = app.node.try_get_context("region")

aws_env = core.Environment(region=region)
stack = core.Stack(scope=app,id=f"{name}-stack",env=aws_env)

cluster_construct = EksConstruct(
    scope=stack,
    id=f"{name}-cluster",
    cluster_name=f"{name}-cluster"
)

app.synth()
