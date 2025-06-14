# CLI Calculator

A simple command-line calculator application written in Python that performs basic arithmetic operations.

## Installation

```bash
# Clone the repository
git clone https://github.com/ECHIDNATHEG/cli_calculator.git

# Navigate to the directory
cd cli_calculator
```

## Usage

Run the calculator with the operation and numbers as arguments:

```bash
python MyCLIApp/cli.py [OPERATION] [NUMBERS...]
```

### Operations

- `+` : Addition
- `-` : Subtraction
- `x` : Multiplication
- `/` : Division

### Examples

```bash
# Addition
python MyCLIApp/cli.py + 5 10 15
Result of Sum: 30.0

# Subtraction 
python MyCLIApp/cli.py - 100 20 5
Result of Subtraction: 75.0

# Multiplication
python MyCLIApp/cli.py "x" 2 3 4
Result of Multiplication: 24.0

# Division
python MyCLIApp/cli.py "/" 100 4 5
Result of Division: 5.0
```

**Note**: When using multiplication (`x`) or other special characters, you may need to escape them or use quotes to prevent shell expansion.

## Features

- Supports multiple numbers in a single calculation
- Division by zero detection
- Simple and intuitive interface

## Requirements

- Python 3.x
