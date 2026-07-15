# Intentional Jenkins failure demo

This small project is designed to make the Jenkins **Run tests** stage fail.

Run locally:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The Jenkinsfile installs `pytest` and runs the same test suite. Use the resulting
test output to ask an AI for the root cause. The pipeline configuration is valid;
the failure originates in the Python calculation logic.
