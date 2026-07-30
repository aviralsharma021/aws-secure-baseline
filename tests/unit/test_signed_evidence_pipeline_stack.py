import aws_cdk as core
import aws_cdk.assertions as assertions

from signed_evidence_pipeline.signed_evidence_pipeline_stack import SignedEvidencePipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in signed_evidence_pipeline/signed_evidence_pipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SignedEvidencePipelineStack(app, "SignedEvidencePipelineStack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
