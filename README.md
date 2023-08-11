# CSP-update-checker

[![GitHub stars](https://img.shields.io/github/stars/rishuranjanofficial/CSP-update-checker?logoColor=blue&style=social)](https://github.com/rishuranjanofficial/CSP-update-checker/stargazers)   [![GitHub forks](https://img.shields.io/github/forks/rishuranjanofficial/CSP-update-checker?logoColor=blue&style=social)](https://github.com/rishuranjanofficial/CSP-update-checker/network)

## Introduction
Content Security Policy(CSP) is additional layer of protection to detect and remediate attack like Cross-Site Scripting (XSS) and injection attacks. Since XSS being commonly found vulnerability and it is always preferred to patched by code level. However, having effective and efficient CSP in place can give a breather for DevSecOps of an organization. 

## Use Case
Suppose you have multiple domains to manage. There is any change or new 3rd party domain is added in CSP policy without discussing with security team in some of the domains. With the help of this tool, you can find out which domain's CSP policy is changed from last time in the input list of domains.

The main purpose of this tool is to provide list of domains whose CSP is changed from last time.

## Requirements
- pip3 install validators
- echo '&&&'>Domain_Hash.txt

## Features
- Supports single domain or domains list input
- Check for CSP on input domain(s)
- Captures the domain(s), CSP hash, timestamp along with CSP in file
- Compare CSP with stored data and update


## Download Link 
**[CSP-update-checker.py](https://rishuranjanofficial.github.io/CSP-update-checker/CSP-update-checker.py)**

## Flowchart
<p align="center">
  <img src="Resources/Flowchart%20of%20CSP%20update%20checker%20script.png?raw=true" alt="Flow chart of CSP update checker script"/>
</p>

## Working POC
<p align="center">
  <img src="Resources/output.png?raw=true" alt="Flow chart of CSP update checker script"/>
</p>

## Issues and Suggestions
[![GitHub issues](https://img.shields.io/github/issues/rishuranjanofficial/CSP-update-checker?label=Contribution&style=social)](https://github.com/rishuranjanofficial/CSP-update-checker/issues)

## Author
**Rishu Ranjan**
> [![](https://img.shields.io/twitter/follow/secureit_rrj?style=social)](https://twitter.com/intent/follow?screen_name=secureit_rrj)   [![](https://static-exp1.licdn.com/sc/h/95o6rrc5ws6mlw6wqzy0xgj7y)](https://www.linkedin.com/in/rishuranjan/)
