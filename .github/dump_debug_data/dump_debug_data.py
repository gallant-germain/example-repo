#!/usr/bin/env python
# -*- encoding: utf-8

import json
import os


if __name__ == '__main__':
    github_event_path = os.environ["GITHUB_EVENT_PATH"]
    event_data = json.load(open(github_event_path))
    print(event_data)
