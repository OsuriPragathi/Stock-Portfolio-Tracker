# 📘 Stock Portfolio Tracker

This repository contains a simple, beginner-friendly Python project that helps users calculate their total stock investment value based on predefined stock prices.

---

## 🗂️ Project Structure

```
stock-portfolio-tracker/
├── tracker.py              # Main Python script
├── README.md               # Project overview and instructions
├── requirements.txt        # Python dependencies (optional)
```

---

## 🧾 Features

* User inputs stock symbols and number of shares owned.
* Calculates and displays total investment.
* Option to save the result as a `.txt` or `.csv` file.
* Uses a hardcoded dictionary for stock prices.
* Friendly CLI (Command Line Interface) prompts.

---

## 📦 Requirements

No external libraries are required for the basic version.

```bash
python3 tracker.py
```

If you want to create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

---

## 🚀 How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
cd stock-portfolio-tracker
```

2. Run the script:

```bash
python tracker.py
```

3. Follow the prompts to input stock symbols and quantities.
4. View the total investment summary.
5. Choose whether to save the results to a file.

---

## 🛠️ Example

```bash
Enter a stock symbol (like AAPL, TSLA) or type 'done' to finish: AAPL
How many shares of AAPL do you own? 5
Enter a stock symbol (like AAPL, TSLA) or type 'done' to finish: TSLA
How many shares of TSLA do you own? 3
Enter a stock symbol (like AAPL, TSLA) or type 'done' to finish: done

🧾 Here's a summary of your investments:
- AAPL: 5 shares @ $180 = $900
- TSLA: 3 shares @ $250 = $750

💰 Total Investment Value: $1650
```

---

## 📄 Sample Output File (CSV)

```
Stock,Quantity,Price,Total
AAPL,5,180,900
TSLA,3,250,750
Total Investment,,,1650
```

---

## 🤝 Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## ✨ Acknowledgments

Inspired by beginner Python projects for learning dictionaries, file handling, and basic user input.

Happy tracking! 📊
