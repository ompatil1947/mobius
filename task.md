# Mobius: Completion Criteria

## Objective
Bring the repository to a fully healthy state so all checks pass in CI and the generated output is consistent with the project reference.

## Expected Outcome
Your work is considered complete when all of the following are true:

1. The project installs successfully in a clean Python environment.
2. The site builds successfully.
3. The local test suite passes.
4. The generated site output matches the reference output already present in the repository.
5. Workflow validation passes.

## Required Work
- Identify and fix issues that prevent a successful build and test run.
- Ensure command-line usage works as expected for build and serve commands.
- Make only necessary code/configuration changes; keep project structure intact.

## Constraints
- Do not remove tests or weaken assertions.
- Do not hardcode outputs to bypass checks.
- Do not disable workflows or validation steps.