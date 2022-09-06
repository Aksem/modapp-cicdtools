# Tools for CI/CD cross-platform configurations

Set of tools for simplifying CI/CD configuration for cross-platform builds.

- documented
- tested
- available as executable (see 'Releases' page)

**Motivation:** configuration of some typical operations in CI/CD for cross-platform applications are not as easy as it could be. Some are equal on UNIX, like macOS and Linux. However, parameters can differ. For Windows separate script is often required for cmd or powershell. This project aims to provide cross-platform tools to simplify CI/CD configuration for such applications and minimize the need for platform-specific scripts.

## Installation

If you use bash, you can use wget to get cicdtools binaries. Replace 'v0.1.3' with version you need and 'Linux' with OS you need cicdtools for.

```bash
wget https://github.com/Aksem/modapp-cicdtools/releases/download/v0.1.3/cicdtools_Linux.zip -O cicdtools.zip
unzip cicdtools.zip
```

Then you need either to add cicdtools to PATH, or you can use it as local executable:

```bash
# Add to PATH and then use as system tool
export PATH="$PATH:$PWD/cicdtools"
cicdtools --help

# or use as local executable
./cicdtools/cicdtools --help
```

Full example of usage cicdtools for CI/CD configuration of cross-platform build: [example](https://github.com/Aksem/modapp-cicdtools/blob/main/.github/workflows/ci.yml)

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

  Check whether a file or directory exists.

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

  Check whether the command(e.g., application) starts without errors. If the command doesn't fail in 'timeout' seconds(10 by default), its execution is interpreted as successful.

  Signature:

  ```bash
  cicdtools test-run [--timeout=10] [--cwd=""] [--print-on-failure=""] [--print-on-success=""] COMMAND
  ```

  Examples:

  ```bash
  # test run of 'output/app.AppImage' executing in 'output' directory.
  cicdtools test-run --cwd="$PWD/output" "app.AppImage"
  ```

All commands also support `--print-on-success="<message>"` and `--print-on-failure="<message>"` options that can be used to print messages on success or failure. This helps pass operation status to CI/CD system.

Also, `--help` option is available for each command to get its documentation.

## Development

- After changing the code, run `lint.sh` to check that your changes conform project rules.
  CI/CD will also check it, but the local run will save you time.

- `ordered-set` dependency is not used explicitly but is needed to speed up compilation with nuitka
