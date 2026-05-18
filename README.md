# Secret Scanning Test Sample App

This repository contains a multi-file Python sample app with intentionally fake secrets to test scanner behavior.

## Project layout

- app.py: root entrypoint
- sample_app/main.py: tiny HTTP app
- sample_app/secrets_fixture.py: fake provider-style secrets
- fixtures/demo.env: fake env-style secrets
- gitleaks.toml: custom gitleaks rules
- scripts/scan.ps1: scan helper script

## Run the sample app

```powershell
python app.py
```

Test endpoints:

```powershell
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/demo-secrets
```

## Run local secret scan

```powershell
./scripts/scan.ps1
```

or directly:

```powershell
gitleaks detect --source . --config gitleaks.toml --redact
```

## Test GitHub push protection

```powershell
git checkout -b secret-scan-test
git add .
git commit -m "test: secret scan patterns"
git push -u origin secret-scan-test
```

If push protection is enabled for the repo, GitHub should block push or warn on supported patterns.

## Important

All secrets in this repo are fake and for testing only.
Do not add real credentials to this project.
