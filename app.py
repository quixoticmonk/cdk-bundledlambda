#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from cdk_bundledlambda.cdk_bundledlambda_stack import CdkBundledlambdaStack

app = cdk.App()
CdkBundledlambdaStack(app, "CdkBundledlambdaStack"
                      )

app.synth()
