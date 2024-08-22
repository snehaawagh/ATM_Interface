# ATM Machine Simulation

This project is a simple Python-based simulation of an ATM machine. It allows users to perform basic banking operations such as checking account balance, depositing money, withdrawing money, changing PIN, and viewing transaction history. The program is designed with a simple command-line interface and provides basic input validation.

## Features

- **Account Balance Inquiry**
- **Cash Deposit**
- **Cash Withdrawal**
- **PIN Change**
- **Transaction History**
- **PIN Verification with 3 Attempt Limit**

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/snehaawagh/atm-machine-simulation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd atm-machine-simulation
    ```

### Running the Program

To run the ATM simulation, execute the following command:

```bash
python atm_simulation.py
```

## How It Works

- The program starts with a default PIN (`1234`) and an account balance of `Rs.5000.00`.
- Users have 3 attempts to enter the correct PIN.
- After successful PIN entry, users can choose from options like checking balance, depositing money, withdrawing money, changing PIN, and viewing transaction history.
- The program continues to display the menu until the user chooses to exit.

## Example Usage

```plaintext
**** Welcome to the ATM ****
1: Check Balance
2: Deposit
3: Withdraw
4: Change PIN
5: Transaction History
6: Exit

Choose an option: 1
Your total balance is: Rs.5000.00

Choose an option: 2
Enter amount to deposit: Rs.1500
You have deposited Rs.1500.00
Your total balance is Rs.6500.00

Choose an option: 6
Thank you for using the ATM. Goodbye!
```
## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for new features.

