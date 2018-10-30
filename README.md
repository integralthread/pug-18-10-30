# pug-18-10-30
python user group meetup 

# Outline

- Automation - in what context
  - scripts you run locally
- A small example of bash vs python
  - ls -las
  - ip addr
  - ip addr show docker0
- prepared examples

# Other Ideas

- backups with a tool like restic

Previous client had a complicated validation workflow
that involved various test suites, docker and then 
using terraform to spin up or apply changes to infrastructure
and ansible to do some provisioning.

I used sh to tie all these things together. Extremely 
powerful tool for never writing bash scripts and automating 
complex workflows.
