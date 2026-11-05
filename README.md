# .run-task-run-db7ec1ce635347f2b55ebfff07d69cdd

Initialized by PR Pilot for empty repositories.

## CI Commands

To ensure that every change is checked consistently, the following commands are executed in the CI pipeline:

- **Lint:** Run code linting to check for errors and maintain code quality.
- **Typecheck:** Execute `tsc --noEmit` to ensure TypeScript code is type-safe without emitting files.
- **Unit Tests:** Run tests using Vitest to validate the functionality of the code.
- **Build:** Execute `vite build` to compile the project for production use. 

The CI job will fail if any of these steps encounter issues.