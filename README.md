# TRSF

A tool that provides human readable suggestions to terminal errors in real-time. TRSF runs in the background and automatically intercepts cryptic terminal errors, providing clear, actionable explanations.

## Installation

Using `uv`:

```bash
uv pip install trsf
```

## Usage

1. Start the TRSF error interpreter in your terminal:

```bash
trsf
```

2. Continue using your terminal as usual. When an error occurs, TRSF will automatically provide a human-readable explanation:

```bash
$ chmod 777 /etc/hosts
Permission denied: '/etc/hosts'

🔍 TRSF Suggestion:
This error occurred because you don't have sufficient privileges to modify system files.
Try running the command with sudo:
  sudo chmod 777 /etc/hosts

Note: Modifying system files can be dangerous. Make sure you know what you're doing!
```

To stop TRSF, simply press `Ctrl+C` in the terminal where it's running.

## Development

1. Clone the repository

```bash
git clone https://github.com/tebinraouf/trsf.git
cd trsf
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
uv pip install -e ".[dev]"
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your PR adheres to the following:

- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Write clear commit messages

## License

MIT License - see LICENSE file for details.
