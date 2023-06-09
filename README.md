`   .DefenderGithubCheck Last revision: 07.07.2023 Egil Dankel`

## Relevant links ##
https://github.com/equinor/Solum/issues/12069
https://portal.azure.com/#view/Microsoft_Azure_Security/SecurityMenuBlade/~/DevOpsSecurity  

  
##   DefenderGithubCheck purpose: ##
Create a connection between Defender and Github Checking for testing Security vulnerabilites. This will extend Defender for Cloud security feature aoming these Defender for Clouds cloud Security Posture management (CSPM). 

## Recommendations from Microsoft ##

Check reference https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-reference. 

##Most relevant findings from the recommendations from Microsoft related to GitHub Security ##

## 1- GitHub repositories should have Code scanning enabled. ##
Impact: Medium 
GitHub uses code scanning to analyze code in order to find security vulnerabilities and errors in code. Code scanning can be used to find, triage, and prioritize fixes for existing problems in your code. Code scanning can also prevent developers from introducing new problems. Scans can be scheduled for specific days and times, or scans can be triggered when a specific event occurs in the repository, such as a push. If code scanning finds a potential vulnerability or error in code, GitHub displays an alert in the repository. A vulnerability is a problem in a project's code that could be exploited to damage the confidentiality, integrity, or availability of the project.

## 2- GitHub repositories should have Dependabot scanning enabled. ##
Impact: Medium
GitHub sends Dependabot alerts when it detects vulnerabilities in code dependencies that affect repositories. A vulnerability is a problem in a project's code that could be exploited to damage the confidentiality, integrity, or availability of the project or other projects that use its code. Vulnerabilities vary in type, severity, and method of attack. When code depends on a package that has a security vulnerability, this vulnerable dependency can cause a range of problems.
## 3 - GitHub repositories should have Secret scanning enabled ##
Impact: High 
GitHub scans repositories for known types of secrets, to prevent fraudulent use of secrets that were accidentally committed to repositories. Secret scanning will scan the entire Git history on all branches present in the GitHub repository for any secrets. Examples of secrets are tokens and private keys that a service provider can issue for authentication. If a secret is checked into a repository, anyone who has read access to the repository can use the secret to access the external service with those privileges. Secrets should be stored in a dedicated, secure location outside the repository for the project.

## Folder structure: ##

## Issue information: ##

Goal
Solum assessment for github repositories using Defender for DevOps
Reason- Defender for DevOps has the purpose of assuring healthy Github repos:
- Exposed secrets
- OSS vulnerabilities
- IaC scanning vulnerabilities
- Code scanning vulnerabilities

Definition of Done
 Connection to GitHub organisation and setup connector for Defender for DevOps
https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-github
Integrating Defender for Devops with GitHub https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Labs/Modules/Module%2015%20-%20Integrating%20Defender%20for%20DevOps%20with%20GitHub%20Advanced%20Security.md

 Successfully integrated with the GitHub repository.

 Try the enablement through SPN, managed identity.
Connection has to be done on the repo with a dedicated account

 The integration is tested and verified to be working as expected.

 Defender for DevOps workflows is successfully configured.
https://learn.microsoft.com/en-us/azure/defender-for-cloud/iac-vulnerabilities
Configured CodeQL Analysis - security analysis for several languages, Dependency review - for resolution of vulnerable dependencies, Microsoft Defender for DevOps workflow. 

 Setup build validation policy for repo and create a policy.
Enable CodeQL (a feature of GitHub AdvancedSecurity which does code scanning to find security issues in your code and created a CVE policy

 Setup and discover misconfigurations in Infrastructure as code.
Enabled code scanning to GithubCheck repo

 Select a candidate repo based on a risk assessment and scan code for vulnerabilities.

 Configure and remediate secrets using DevOps Github actions.

 How to configure and detect keyvault secrets.

 Create credential scanner and add visible secrets and test if Defender shows them as unhealthy.

 Provide a reflection on findings from the usage of it so far:

How is this relevant?
DevOps for Github enables awareness of vulnerable code, secrets and threats.
Is this adding valuable feedback to developers?
Like Snyk, DevOps for Github can indicate code flaws that could be remediated by running PR in the specific repo. There is also possibilities to set up Defender for DevOps for GitHub in specific repositories.
Based on the on findings setup for repos in the organization and should it be mandatory?
It would strenghten security for the repos. There will be possibilities to see the security issues and also presented in a graphical user interface using Workbooks in Azure. However, there will be more actions running as the system is built on configuring YML files that will run and check the repos
 Explore further managing PR, security recommendations, might one set up logic apps as remediation?

Describe alternatives you've considered
A clear and concise description of any alternative solutions or features you've considered.

There are some other good alternatives, but however Defender for DevOps and Github is inbuilt into Azure and also Github owned by Microsoft so better to go with the internal connection between the two companies.

The alternatives we looked into are the following:

- Github advanced security https://www.gitguardian.com/lps/github-advanced-security
- Mend https://www.mend.io/repo-integration/
- Snyk https://docs.snyk.io/integrations/git-repository-scm-integrations

### GithubCheck capabilies ###

### Secrets: ###
GitHub scans repositories for known types of secrets, to prevent fraudulent use of secrets that were accidentally committed to repositories. 
Secret scanning will scan the entire Git history on all branches present in the GitHub repository for any secrets. Examples of secrets are tokens 
and private keys that a service provider can issue for authentication. If a secret is checked into a repository, anyone who has read access to the repository
can use the secret to access the external service with those privileges. Secrets should be stored in a dedicated, secure location outside the repository for the project.

### Dependabot scanning: ###

GitHub sends Dependabot alerts when it detects vulnerabilities in code dependencies that affect repositories. A vulnerability
is a problem in a project's code that could be exploited to damage the confidentiality, integrity, or availability of the project or other projects that use its code.
Vulnerabilities vary in type, severity, and method of attack. When code depends on a package that has a security vulnerability,
this vulnerable dependency can cause a range of problems.

### Code Scannning: ####
GitHub uses code scanning to analyze code in order to find security vulnerabilities and errors in code. 
Code scanning can be used to find, triage, and prioritize fixes for existing problems in your code. 
Code scanning can also prevent developers from introducing new problems. Scans can be scheduled for specific days and times, 
or scans can be triggered when a specific event occurs in the repository, such as a push. If code scanning finds a potential 
vulnerability or error in code, GitHub displays an alert in the repository. A vulnerability is a problem in a project's code 
that could be exploited to damage the confidentiality, integrity, or availability of the project.
