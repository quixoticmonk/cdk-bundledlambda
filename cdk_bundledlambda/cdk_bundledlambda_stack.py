from aws_cdk import core as cdk, aws_lambda as _lambda


class CdkBundledlambdaStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _lambda.Function(
            self,
            "fn1",
            handler="index.handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            timeout=cdk.Duration.seconds(10),
            tracing=_lambda.Tracing.ACTIVE,
            code=_lambda.Code.asset("src/")
        )
