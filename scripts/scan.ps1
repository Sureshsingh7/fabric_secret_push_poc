Write-Host "Running gitleaks scan..." -ForegroundColor Cyan
gitleaks detect --source . --config gitleaks.toml --redact

Write-Host "\nGitHub push-protection test:" -ForegroundColor Cyan
Write-Host "1) git checkout -b secret-scan-test"
Write-Host "2) git add ."
Write-Host "3) git commit -m 'test: secret scan patterns'"
Write-Host "4) git push -u origin secret-scan-test"
