# signed-evidence-pipeline

A proof-of-concept system that turns an AI agent's decision — a policy check
result plus an LLM judge evaluation — into a signed, hash-chained evidence
record. Built as a hands-on complement to AWS Certified Security – Specialty
prep, focused on applying real AWS security services (KMS, IAM, CloudTrail,
S3 Object Lock) to a genuine security engineering problem rather than a
toy CRUD app.

## What it does
1. A sample AI agent action is checked against a declared policy (pass/fail)
2. An LLM judge scores the action's output against a rubric
3. Both results are combined into a single record, signed with a KMS
   asymmetric key, and hash-chained to the previous record
4. Records are stored immutably (S3 Object Lock) and queryable via a
   minimal API
5. All pipeline activity is logged via CloudTrail for its own audit trail

## Why this project
Built to develop hands-on AWS security engineering skills — least-privilege
IAM, KMS signing, immutable storage, and audit logging — grounded in
3+ years of information security consulting experience assessing exactly
this kind of compliance evidence for enterprise clients.

## Architecture
[diagram placeholder — yet to add]

## Status
Work in progress — built incrementally as part of a 12-week AWS Security
Specialty study plan. See commit history for build progression.
