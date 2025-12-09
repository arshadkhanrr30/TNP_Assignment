import sqlite3
import hashlib
from datetime import datetime
import tkinter as tk

from tkinter import ttk, messagebox, simpledialog

DB_FILE = "expenses.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    note TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""") 
conn.commit()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker — Login")
        self.iconbitmap('icon.ico')
        self.geometry("920x600")
        #self.resizable(False, False)
        self.user_id = None
        self.username = None
        self.login_frame = None
        self.register_frame = None
        self.dashboard_frame = None
        self.create_login_frame()

    def create_login_frame(self):
        if self.dashboard_frame:
            self.dashboard_frame.pack_forget()
        if self.register_frame:
            self.register_frame.pack_forget()
        self.login_frame = tk.Frame(self, padx=20, pady=20)
        self.login_frame.pack(expand=True)
        tk.Label(self.login_frame, text="Expense Tracker", font=("Helvetica", 20, "bold")).pack(pady=(0, 10))
        tk.Label(self.login_frame, text="Login", font=("Helvetica", 14)).pack(pady=(0, 10))
        tk.Label(self.login_frame, text="Username:").pack(anchor="w")
        self.login_username = tk.Entry(self.login_frame)
        self.login_username.pack(fill="x")
        tk.Label(self.login_frame, text="Password:").pack(anchor="w", pady=(8,0))
        self.login_password = tk.Entry(self.login_frame, show="*")
        self.login_password.pack(fill="x")
        tk.Button(self.login_frame, text="Login", width=12, command=self.handle_login).pack(pady=(12,6))
        tk.Button(self.login_frame, text="Register", width=12, command=self.create_register_frame).pack()

    def create_register_frame(self):
        self.login_frame.pack_forget()
        self.register_frame = tk.Frame(self, padx=20, pady=20)
        self.register_frame.pack(expand=True)
        tk.Label(self.register_frame, text="Register", font=("Helvetica", 16)).pack(pady=(0, 10))
        tk.Label(self.register_frame, text="Username:").pack(anchor="w")
        self.reg_username = tk.Entry(self.register_frame)
        self.reg_username.pack(fill="x")
        tk.Label(self.register_frame, text="Password:").pack(anchor="w", pady=(8,0))
        self.reg_password = tk.Entry(self.register_frame, show="*")
        self.reg_password.pack(fill="x")
        tk.Label(self.register_frame, text="Confirm Password:").pack(anchor="w", pady=(8,0))
        self.reg_password2 = tk.Entry(self.register_frame, show="*")
        self.reg_password2.pack(fill="x")
        tk.Button(self.register_frame, text="Create Account", width=14, command=self.handle_register).pack(pady=(12,6))
        tk.Button(self.register_frame, text="Back to Login", width=14, command=self.back_to_login).pack()

    def back_to_login(self):
        self.register_frame.pack_forget()
        self.create_login_frame()

    def handle_register(self):
        username = self.reg_username.get().strip()
        pwd = self.reg_password.get()
        pwd2 = self.reg_password2.get()
        if not username or not pwd:
            messagebox.showwarning("Input error", "Username and password cannot be empty.")
            return
        if pwd != pwd2:
            messagebox.showwarning("Input error", "Passwords do not match.")
            return
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(pwd)))
            conn.commit()
            messagebox.showinfo("Success", "Account created! You can now login.")
            self.register_frame.pack_forget()
            self.create_login_frame()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists. Choose a different username.")

    def handle_login(self):
        username = self.login_username.get().strip()
        pwd = self.login_password.get()
        if not username or not pwd:
            messagebox.showwarning("Input error", "Please enter username and password.")
            return
        cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user and user[1] == hash_password(pwd):
            self.user_id = user[0]
            self.username = username
            self.login_frame.pack_forget()
            self.create_dashboard()
        else:
            messagebox.showerror("Login failed", "Invalid username or password.")

    def create_dashboard(self):
        self.title(f"Expense Tracker — {self.username}")
        self.dashboard_frame = tk.Frame(self, padx=10, pady=10)
        self.dashboard_frame.pack(fill="both", expand=True)
        top_frame = tk.Frame(self.dashboard_frame)
        top_frame.pack(fill="x", pady=(0, 8))
        tk.Label(top_frame, text=f"Welcome, {self.username}", font=("Helvetica", 14, "bold")).pack(side="left")
        btn_logout = tk.Button(top_frame, text="Logout", command=self.logout)
        btn_logout.pack(side="right")
        add_frame = tk.LabelFrame(self.dashboard_frame, text="Add / Update Expense", padx=8, pady=8)
        add_frame.pack(fill="x", pady=(0, 8))
        tk.Label(add_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
        self.ent_date = tk.Entry(add_frame)
        self.ent_date.grid(row=0, column=1, sticky="w", padx=6)
        self.ent_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        tk.Label(add_frame, text="Category:").grid(row=0, column=2, sticky="w", padx=(10,0))
        self.ent_category = tk.Entry(add_frame)
        self.ent_category.grid(row=0, column=3, sticky="w", padx=6)
        tk.Label(add_frame, text="Amount:").grid(row=1, column=0, sticky="w", pady=(8,0))
        self.ent_amount = tk.Entry(add_frame)
        self.ent_amount.grid(row=1, column=1, sticky="w", padx=6, pady=(8,0))
        tk.Label(add_frame, text="Note:").grid(row=1, column=2, sticky="w", padx=(10,0), pady=(8,0))
        self.ent_note = tk.Entry(add_frame)
        self.ent_note.grid(row=1, column=3, sticky="w", padx=6, pady=(8,0))
        btn_add = tk.Button(add_frame, text="Add Expense", command=self.add_expense)
        btn_add.grid(row=2, column=1, pady=(10,0))
        btn_update = tk.Button(add_frame, text="Update Selected", command=self.update_selected)
        btn_update.grid(row=2, column=2, pady=(10,0), padx=(8,0))
        btn_delete = tk.Button(add_frame, text="Delete Selected", command=self.delete_selected)
        btn_delete.grid(row=2, column=3, pady=(10,0), padx=(6,0))
        tree_frame = tk.Frame(self.dashboard_frame)
        tree_frame.pack(fill="both", expand=True)
        cols = ("id", "date", "category", "amount", "note")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=12)
        self.tree.heading("id", text="ID")
        self.tree.column("id", width=50, anchor="center")
        self.tree.heading("date", text="Date")
        self.tree.column("date", width=100, anchor="center")
        self.tree.heading("category", text="Category")
        self.tree.column("category", width=150, anchor="w")
        self.tree.heading("amount", text="Amount (₹)")
        self.tree.column("amount", width=100, anchor="e")
        self.tree.heading("note", text="Note")
        self.tree.column("note", width=250, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.bind("<Double-1>", self.on_tree_double_click)
        bottom_frame = tk.Frame(self.dashboard_frame)
        bottom_frame.pack(fill="x", pady=(8, 0))
        self.lbl_total = tk.Label(bottom_frame, text="Total: ₹0.00", font=("Helvetica", 12, "bold"))
        self.lbl_total.pack(side="left", padx=(6,0))
        btn_refresh = tk.Button(bottom_frame, text="Refresh", command=self.refresh_tree)
        btn_refresh.pack(side="right", padx=6)
        btn_export = tk.Button(bottom_frame, text="Export Selected to CSV", command=self.export_selected_csv)
        btn_export.pack(side="right", padx=6)
        btn_predict7 = tk.Button(bottom_frame, text="Predict Next 7 Days", command=self.predict_future_expense)
        btn_predict7.pack(side="right", padx=6)
        btn_predict_month = tk.Button(bottom_frame, text="Predict Next Month", command=self.predict_monthly_expense)
        btn_predict_month.pack(side="right", padx=6)
        btn_budget = tk.Button(bottom_frame, text="Budget Suggestions", command=self.show_budget_suggestions)
        btn_budget.pack(side="right", padx=6)
        self.refresh_tree()

    def add_expense(self):
        date = self.ent_date.get().strip()
        category = self.ent_category.get().strip() or "Misc"
        amount_str = self.ent_amount.get().strip()
        note = self.ent_note.get().strip()
        if not date or not category or not amount_str:
            messagebox.showwarning("Input error", "Date, Category and Amount are required.")
            return
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input error", "Date must be in YYYY-MM-DD format.")
            return
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showwarning("Input error", "Amount must be a number.")
            return
        cursor.execute(
            "INSERT INTO expenses (user_id, date, category, amount, note) VALUES (?, ?, ?, ?, ?)",
            (self.user_id, date, category, amount, note)
        )
        conn.commit()
        messagebox.showinfo("Success", "Expense added.")
        self.clear_inputs()
        self.refresh_tree()

    def refresh_tree(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        cursor.execute("SELECT id, date, category, amount, note FROM expenses WHERE user_id = ? ORDER BY date DESC, id DESC", (self.user_id,))
        rows = cursor.fetchall()
        total = 0.0
        for row in rows:
            self.tree.insert("", "end", values=row)
            total += (row[3] or 0)
        self.lbl_total.config(text=f"Total: ₹{total:.2f}")

    def clear_inputs(self):
        self.ent_date.delete(0, tk.END)
        self.ent_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.ent_category.delete(0, tk.END)
        self.ent_amount.delete(0, tk.END)
        self.ent_note.delete(0, tk.END)

    def on_tree_double_click(self, _event):
        self.populate_inputs_from_selection()

    def populate_inputs_from_selection(self):
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.ent_date.delete(0, tk.END)
        self.ent_date.insert(0, values[1])
        self.ent_category.delete(0, tk.END)
        self.ent_category.insert(0, values[2])
        self.ent_amount.delete(0, tk.END)
        self.ent_amount.insert(0, values[3])
        self.ent_note.delete(0, tk.END)
        self.ent_note.insert(0, values[4] or "")

    def get_selected_row_id(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Please select an expense from the table.")
            return None
        values = self.tree.item(sel[0], "values")
        return values[0]

    def update_selected(self):
        exp_id = self.get_selected_row_id()
        if exp_id is None:
            return
        date = self.ent_date.get().strip()
        category = self.ent_category.get().strip()
        amount_str = self.ent_amount.get().strip()
        note = self.ent_note.get().strip()
        if not date or not category or not amount_str:
            messagebox.showwarning("Input error", "Date, Category and Amount are required.")
            return
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input error", "Date must be in YYYY-MM-DD format.")
            return
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showwarning("Input error", "Amount must be a number.")
            return
        cursor.execute(
            "UPDATE expenses SET date = ?, category = ?, amount = ?, note = ? WHERE id = ? AND user_id = ?",
            (date, category, amount, note, exp_id, self.user_id)
        )
        conn.commit()
        messagebox.showinfo("Success", "Expense updated.")
        self.refresh_tree()

    def delete_selected(self):
        exp_id = self.get_selected_row_id()
        if exp_id is None:
            return
        if messagebox.askyesno("Confirm delete", "Are you sure you want to delete the selected expense?"):
            cursor.execute("DELETE FROM expenses WHERE id = ? AND user_id = ?", (exp_id, self.user_id))
            conn.commit()
            messagebox.showinfo("Deleted", "Expense deleted.")
            self.refresh_tree()

    def export_selected_csv(self):
        import csv
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select at least one row to export.")
            return
        rows = [self.tree.item(s, "values") for s in sel]
        default_filename = f"{self.username}_expenses_export.csv"
        fname = simpledialog.askstring("Export", f"Enter filename (default: {default_filename}):")
        if not fname:
            fname = default_filename
        if not fname.lower().endswith(".csv"):
            fname += ".csv"
        try:
            with open(fname, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "date", "category", "amount", "note"])
                for r in rows:
                    writer.writerow(r)
            messagebox.showinfo("Exported", f"Exported {len(rows)} rows to {fname}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")

    def logout(self):
        if messagebox.askyesno("Logout", "Do you want to logout?"):
            self.dashboard_frame.pack_forget()
            self.user_id = None
            self.username = None
            self.title("Expense Tracker — Login")
            self.create_login_frame()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            try:
                conn.close()
            except:
                pass
            self.destroy()

    def predict_future_expense(self):
        try:
            import pandas as pd
            import numpy as np
            from sklearn.linear_model import LinearRegression
        except Exception:
            messagebox.showerror("Missing library", "Please install pandas, numpy and scikit-learn: pip install pandas numpy scikit-learn")
            return
        cursor.execute("""
            SELECT date, amount 
            FROM expenses 
            WHERE user_id = ? ORDER BY date ASC
        """, (self.user_id,))
        rows = cursor.fetchall()
        if len(rows) < 5:
            messagebox.showwarning("Not enough data", "Add at least 5 expenses for prediction.")
            return
        df = pd.DataFrame(rows, columns=["date", "amount"]) 
        df["date"] = pd.to_datetime(df["date"]) 
        df = df.groupby("date")["amount"].sum().reset_index()
        df["day_num"] = (df["date"] - df["date"].min()).dt.days
        X = df[["day_num"]]
        y = df["amount"]
        model = LinearRegression()
        model.fit(X, y)
        last_day = int(df["day_num"].max())
        future_days = np.array([last_day + i for i in range(1, 8)]).reshape(-1, 1)
        predictions = model.predict(future_days)
        predicted_total = float(predictions.sum())
        daily_text = "\n".join([f"Day +{i}: ₹{predictions[i-1]:.2f}" for i in range(1, 8)])
        messagebox.showinfo("7-Day Expense Prediction", f"Predicted total expense for next 7 days: ₹{predicted_total:.2f}\n\nBreakdown:\n{daily_text}")

    def predict_monthly_expense(self):
        try:
            import pandas as pd
            import numpy as np
            from sklearn.linear_model import LinearRegression
        except Exception:
            messagebox.showerror("Missing library", "Please install pandas, numpy and scikit-learn: pip install pandas numpy scikit-learn")
            return
        cursor.execute("SELECT date, amount FROM expenses WHERE user_id = ? ORDER BY date ASC", (self.user_id,))
        rows = cursor.fetchall()
        if len(rows) < 10:
            messagebox.showwarning("Not enough data", "Add at least 10 expense records (spanning multiple months) for monthly prediction.")
            return
        df = pd.DataFrame(rows, columns=["date", "amount"]) 
        df["date"] = pd.to_datetime(df["date"]) 
        df.set_index("date", inplace=True)
        monthly = df["amount"].resample('M').sum().reset_index()
        monthly["month_num"] = list(range(len(monthly)))
        X = monthly[["month_num"]]
        y = monthly["amount"]
        if len(monthly) < 3:
            predicted_next_month = float(monthly["amount"].mean())
            method = "average"
        else:
            model = LinearRegression()
            model.fit(X, y)
            next_month_idx = np.array([[monthly["month_num"].max() + 1]])
            predicted_next_month = float(model.predict(next_month_idx)[0])
            method = "linear_regression"
        predicted_next_month = max(0.0, float(predicted_next_month))
        last_month_total = float(monthly["amount"].iloc[-1]) if len(monthly) > 0 else 0.0
        pct_change = ((predicted_next_month - last_month_total) / last_month_total * 100) if last_month_total != 0 else float('inf')
        messagebox.showinfo("Monthly Prediction", f"Predicted total for next month: ₹{predicted_next_month:.2f}\nLast month: ₹{last_month_total:.2f}\nExpected change: {pct_change:+.2f}%\n\n(Model used: {method})")

    def show_budget_suggestions(self):
        try:
            import pandas as pd
            import numpy as np
        except Exception:
            messagebox.showerror("Missing library", "Please install pandas and numpy: pip install pandas numpy")
            return
        cursor.execute("SELECT date, category, amount FROM expenses WHERE user_id = ? ORDER BY date ASC", (self.user_id,))
        rows = cursor.fetchall()
        if not rows:
            messagebox.showinfo("No data", "You don't have expense data yet. Add expenses to get suggestions.")
            return
        df = pd.DataFrame(rows, columns=["date", "category", "amount"]) 
        df["date"] = pd.to_datetime(df["date"]) 
        df.set_index("date", inplace=True)
        monthly_totals = df["amount"].resample('M').sum()
        avg_monthly = float(monthly_totals.mean()) if len(monthly_totals) > 0 else 0.0
        last_month = float(monthly_totals.iloc[-1]) if len(monthly_totals) > 0 else 0.0
        recent = df.last('90D').reset_index()
        cat_sums = recent.groupby('category')["amount"].sum().sort_values(ascending=False)
        suggestions = []
        if last_month > avg_monthly * 1.15 and avg_monthly > 0:
            suggestions.append(("Overspending", f"You spent ₹{last_month:.2f} last month, which is higher than your average (₹{avg_monthly:.2f}). Consider reviewing large categories and cutting non-essential spending."))
        else:
            suggestions.append(("Good", f"Your last month's spending (₹{last_month:.2f}) is close to your average (₹{avg_monthly:.2f}). Keep it up!"))
        if not cat_sums.empty:
            top3 = cat_sums.head(3)
            for cat, amt in top3.items():
                reduction = amt * 0.10
                suggestions.append((f"Category: {cat}", f"You spent ₹{amt:.2f} on {cat} in the last 90 days. Try to reduce by ₹{reduction:.2f} (~10%) to save money."))
        target_budget = avg_monthly * 0.9
        suggestions.append(("Budget Target", f"Try a monthly budget of ₹{target_budget:.2f} (10% below your average). Break it into essentials and savings."))
        msg = ""
        for title, text in suggestions:
            msg += f"{title}: {text}\n\n"
        suggestion_window = tk.Toplevel(self)
        suggestion_window.title("Smart Budget Suggestions")
        suggestion_window.geometry("600x400")
        tk.Label(suggestion_window, text="Smart Budget Suggestions", font=("Helvetica", 14, "bold")).pack(pady=(8,4))
        txt = tk.Text(suggestion_window, wrap='word')
        txt.pack(fill='both', expand=True, padx=8, pady=8)
        txt.insert('1.0', msg)
        txt.config(state='disabled')

if __name__ == "__main__":
    app = ExpenseApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
