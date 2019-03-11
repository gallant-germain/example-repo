#!/usr/bin/env python
# -*- encoding: utf-8

import json
import os
import subprocess
import sys


def get_session(github_token):
    import requests

    sess = requests.Session()
    sess.headers = {
        "Accept": "; ".join([
            "application/vnd.github.v3+json",
            "application/vnd.github.antiope-preview+json",
        ]),
        "Authorization": f"token {github_token}",
        "User-Agent": f"GitHub Actions script in {__file__}"
    }

    def raise_for_status(resp, *args, **kwargs):
        try:
            resp.raise_for_status()
        except Exception:
            print(resp.text)
            sys.exit("Error: Invalid repo, token or network issue!")

    sess.hooks["response"].append(raise_for_status)
    return sess



if __name__ == '__main__':
    subprocess.check_call(["pip3", "install", "requests"])
    import requests

    github_token = os.environ["GITHUB_TOKEN"]
    github_repository = os.environ["GITHUB_REPOSITORY"]

    github_event_path = os.environ["GITHUB_EVENT_PATH"]
    event_data = json.load(open(github_event_path))

    sess = get_session(github_token)

    pull_request = check_run["pull_requests"][0]
    merge_url = pull_request["url"] + "/merge"
    sess.put(merge_url)
