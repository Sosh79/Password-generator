# Password Generator Tool

A secure, cross-platform password generator with interactive and automated modes.

## Features

- Generates cryptographically secure random passwords
- Supports both Windows and Linux
- Interactive mode with prompts
- Command-line arguments for automation
- Optional special characters
- Save passwords to file
- Open source and customizable

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sosh79/Password-generator.git
cd Password-generator
```

2. Make the scripts executable (Linux):

```bash
chmod +x passgen.sh
```

## Usage

### Windows

Run the batch file:

```bash
passgen.bat
```

### Linux

Run the shell script:

```bash
./passgen.sh
```

### Command-line Options

- `-n NUM`: Number of passwords to generate
- `-l LENGTH`: Password length
- `-s`: Simple mode (no special characters)

### Examples

1. Generate 5 passwords of length 12:

```bash
./passgen.sh -n 5 -l 12
```

2. Interactive mode with save prompt:

```bash
./passgen.sh
```

3. Generate simple passwords (no special chars):

```bash
./passgen.sh -s -n 3 -l 8
```

## File Structure

- `password_gen.py`: Main password generation script
- `passgen.bat`: Windows batch file wrapper
- `passgen.sh`: Linux shell script wrapper
- `Password.txt`: Saved passwords (created when saving)

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

[MIT](https://github.com/Sosh79/Password-generator/blob/main/LICENSE)
