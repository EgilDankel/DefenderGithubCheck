#   .DefenderGithubCheck
# 
#   by Egil Dankel 2023
#   

###   DefenderGithubCheck purpose: ###
Create a connection between Defender and Github Checking for testing Security vulnerabilites.

### Secrets ###
GitHub scans repositories for known types of secrets, to prevent fraudulent use of secrets that were accidentally committed to repositories. 
Secret scanning will scan the entire Git history on all branches present in the GitHub repository for any secrets. Examples of secrets are tokens 
and private keys that a service provider can issue for authentication. If a secret is checked into a repository, anyone who has read access to the repository
can use the secret to access the external service with those privileges. Secrets should be stored in a dedicated, secure location outside the repository for the project.

### Dependabot scanning ###

GitHub sends Dependabot alerts when it detects vulnerabilities in code dependencies that affect repositories. A vulnerability
is a problem in a project's code that could be exploited to damage the confidentiality, integrity, or availability of the project or other projects that use its code.
Vulnerabilities vary in type, severity, and method of attack. When code depends on a package that has a security vulnerability,
this vulnerable dependency can cause a range of problems.

### Code Scannning ####
GitHub uses code scanning to analyze code in order to find security vulnerabilities and errors in code. 
Code scanning can be used to find, triage, and prioritize fixes for existing problems in your code. 
Code scanning can also prevent developers from introducing new problems. Scans can be scheduled for specific days and times, 
or scans can be triggered when a specific event occurs in the repository, such as a push. If code scanning finds a potential 
vulnerability or error in code, GitHub displays an alert in the repository. A vulnerability is a problem in a project's code 
that could be exploited to damage the confidentiality, integrity, or availability of the project.
