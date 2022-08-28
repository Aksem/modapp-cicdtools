# Tools for CI/CD cross-platform configurations

Set of tools for simplyfing CI/CD configuration for cross-platform builds.

- documented
- tested
- available as executable (see 'Releases' page)

**Motivation:** TODO

## Installation

... TODO

## Commands & Usage

- archive
  
  Archive either directory, directory content or file to a zip archive.

  Signature:

  ```bash
  cicdtools archive [--only-content] [--print-on-failure=""] [--print-on-success=""] PATH OUTPUT
  ```

  Examples:

  ```bash
  # archive the whole directory 'build/app_linux' in output/app_linux.zip archive
  cicdtools archive $PWD/build/app_linux $PWD/output/app_linux.zip

  # archive only content of the directory 'build/app_android' in output/app_android.zip archive
  cicdtools archive --only-content $PWD/build/app_android $PWD/output/app_android.zip

  # archive 'build/app.exe' file in output/app_windows.zip
  cicdtools archive $PWD/build/app.exe $PWD/output/app_windows.zip
  ```

- file-exists

  Check whether file or directory exists.

  Signature:

  ```bash
  cicdtools file-exists [--print-on-failure=""] [--print-on-success=""] FILEPATH
  ```

  Examples:

  ```bash
  # check whether 'output/app.AppImage' file exists
  cicdtools file-exists "$PWD/output/app.AppImage"
  ```

- test-run

  Check whether command(e.g. application) starts without errors. If command doesn't fail in 'timeout' seconds(10 by default), its execution is interpreted as successful.

  Signature:

  ```bash
  cicdtools test-run [--timeout=10] [--cwd=""] [--print-on-failure=""] [--print-on-success=""] COMMAND
  ```

  Examples:

  ```bash
  # test run of 'output/app.AppImage' executing in 'output' directory.
  cicdtools test-run --cwd="$PWD/output" "app.AppImage"
  ```

All comands also support `--print-on-success="<message>"` and `--print-on-failure="<message>"` options that can be used to print messages on success or failure. This is helpful to pass operation error to CI/CD system.

Also, `--help` option is available for each command to get its documentation.

## Development

- After changing the code, run `lint.sh` to check that you changes conform project rules.
  It will be also checked in the CI/CD, but local run will save your time.
