Microsoft Security DevOps is a command line application that integrates static analysis tools into the development lifecycle. Security DevOps installs, configures, and runs the latest versions of static analysis tools such as, SDL, security and compliance tools. Security DevOps is data-driven with portable configurations that enable deterministic execution across multiple environments.

Security DevOps uses the following Open Source tools:

name: MSDO windows-latest
on:
  push:
    branches:
      - main

jobs:
  sample:
    name: Microsoft Security DevOps Analysis

    # MSDO runs on windows-latest.
    # ubuntu-latest and macos-latest supporting coming soon
    runs-on: windows-latest

    steps:

      # Checkout your code repository to scan
    - uses: actions/checkout@v3

      # Install dotnet, used by MSDO
    - uses: actions/setup-dotnet@v3
      with:
        dotnet-version: |
          5.0.x
          6.0.x

      # Run analyzers
    - name: Run Microsoft Security DevOps Analysis
      uses: microsoft/security-devops-action@preview
      id: msdo

      # Upload alerts to the Security tab
    - name: Upload alerts to Security tab
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: ${{ steps.msdo.outputs.sarifFile }}

      # Upload alerts file as a workflow artifact
    - name: Upload alerts file as a workflow artifact
      uses: actions/upload-artifact@v3
      with:  
        name: alerts
        path: ${{ steps.msdo.outputs.sarifFile }}
