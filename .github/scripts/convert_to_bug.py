import os
import re

from ghapi.all import GhApi, context_github, github_token, user_repo

owner, repo = user_repo()
api = GhApi(owner=owner, repo=repo, token=github_token())

# obtain the pr number that triggered the event
pull_request = context_github.event.pull_request
pr_number = pull_request.number

# Retrieve the issue data
issues = api.issues.list_comments(issue_numer=pr_number)

for issue in issues:
    msg_body = issue[-1].body # get the content of the most recent comment

    if results:= re.search('/bug', msg_body):
        api.issues.add_label(owner=owner, repo=repo, issue_number=pr_number, label='BUG')

