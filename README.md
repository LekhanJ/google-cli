# google-cli

A simple command-line tool written in Python that lets you search Google directly from your terminal and opens the results in your default browser.

Instead of typing:

```bash
python3 main.py google what is the square root of 20
```

You can simply run:

```bash
google what is the square root of 20
```

## Features

- Search Google directly from your terminal.
- Automatically opens search results in your default web browser.
- Supports multi-word search queries.
- No third-party Python dependencies required.

## Requirements

- Python 3 installed.
- macOS with Zsh (the default shell on modern macOS).
- A web browser.

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd google-cli
```

Replace `<YOUR_REPOSITORY_URL>` with your repository's Git URL.

Alternatively, download the repository and navigate to its directory.

### 2. Make the script executable

```bash
chmod +x google
```

The script already includes a Python shebang:

```python
#!/usr/bin/env python3
```

This allows macOS to execute it directly without explicitly running `python3`.

### 3. Add the script directory to PATH

Your shell needs to know where to find the `google` executable.

Open your Zsh configuration file:

```bash
nano ~/.zshrc
```

Add the following line at the end:

```bash
export PATH="$HOME/projects/google:$PATH"
```

**Important:** Replace `$HOME/Lekhan/google` with the absolute path to the directory containing the `google` executable.

For example, if you cloned the repository into `~/projects/google-cli`, use:

```bash
export PATH="$HOME/projects/google-cli:$PATH"
```

Save the file using `Ctrl + O`, press `Enter`, and exit with `Ctrl + X`.

Reload your shell configuration:

```bash
source ~/.zshrc
```

### 4. Verify the installation

Run:

```bash
command -v google
```

It should print the full path to your executable, for example:

```text
/Users/your-username/projects/google/google
```

If it does, the command is ready to use.

## Usage

### Search Google

```bash
google what is the square root of 20
```

```bash
google best resources to learn Python
```

```bash
google how does consistent hashing work
```

The tool combines the words into a single search query, URL-encodes it, and opens the Google results page in your default browser.

### Search using quoted text

```bash
google "Python programming tutorials"
```

Both quoted and unquoted multi-word queries are supported.

## Troubleshooting

### `zsh: command not found: google`

Your executable's directory is probably missing from `PATH`.

1. Check that the file exists:

   ```bash
   ls -l /path/to/google-cli/google
   ```

2. Make it executable:

   ```bash
   chmod +x /path/to/google-cli/google
   ```

3. Ensure the correct directory is added to `~/.zshrc`.

4. Reload the configuration:

   ```bash
   source ~/.zshrc
   ```

5. Verify again:

   ```bash
   command -v google
   ```

### The command runs but the browser does not open

Try running the executable directly:

```bash
/path/to/google-cli/google what is the use of calcium
```

Check that Python is installed:

```bash
python3 --version
```

Also ensure that the script uses a valid Google search URL and calls:

```python
webbrowser.open(url)
```

### `Permission denied`

Run:

```bash
chmod +x /path/to/google-cli/google
```

## How it works

The tool uses Python's standard library:

- `sys` — reads command-line arguments.
- `urllib.parse` — encodes the search query for a URL.
- `webbrowser` — opens the Google search page.

No external Python packages or virtual environment are required.