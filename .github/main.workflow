workflow "basic workflow" {
  resolves = ["On check_run event, dump debug data"]
  on = "check_run"
}

action "On check_run event, dump debug data" {
  uses = "./.github/dump_debug_data"
  secrets = ["GITHUB_TOKEN"]
}
