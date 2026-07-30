from aws_cdk import (
    Stack, Duration,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
)
from constructs import Construct

class SignedEvidencePipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Hash-chain index table
        chain_table = dynamodb.Table(
            self, "EvidenceChainTable",
            partition_key=dynamodb.Attribute(
                name="record_id", type=dynamodb.AttributeType.STRING
            ),
            point_in_time_recovery=True,
        )

        # Lambda: policy check + LLM judge score → write to chain table
        evidence_fn = _lambda.Function(
            self, "EvidenceProcessor",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler.process",
            code=_lambda.Code.from_asset("lambda/evidence_processor"),
            timeout=Duration.seconds(30),
            environment={
                "TABLE_NAME": chain_table.table_name,
            },
        )
        chain_table.grant_read_write_data(evidence_fn)