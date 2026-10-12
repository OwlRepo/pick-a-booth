# Workflow Test Cases

## Test 1: New feature

Input: add a configurable countdown sound.

Expected: NEW → TRIAGED → ANALYZING → PLANNED → READY → BUILDING → REVIEW → QA → PR_READY → WAITING_APPROVAL

## Test 2: Existing feature

Input: add a feature that already exists (e.g. WLED countdown signalling).

Expected: NEW → TRIAGED → ANALYZING → SKIPPED_ALREADY_IMPLEMENTED → REPORTED

## Test 3: Missing requirement

Input: feature request without acceptance criteria.

Expected: NEW → TRIAGED → BLOCKED_REQUIREMENT

## Test 4: Security change

Input: change admin authentication.

Expected: architect review required; security-auditor in the QA fan-out; human approval required.
