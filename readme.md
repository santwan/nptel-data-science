# **Maintaining a Python Virtual Environment**

## **1. Activating the Virtual Environment**

### **Windows**
- **PowerShell:**  
  ```powershell
  venv\Scripts\Activate
  ```
- **Command Prompt (cmd):**  
  ```cmd
  venv\Scripts\activate.bat
  ```
- **Git Bash:**  
  ```bash
  source venv/Scripts/activate  
  ```

### **macOS/Linux**
```bash
source venv/bin/activate
```

---

## **2. Deactivating the Virtual Environment**
Run the following command in any shell:
```bash
deactivate
```

---

## **3. Installing Packages Inside the Virtual Environment**
Once activated, install packages using:
```bash
pip install package_name
```
Example:
```bash
pip install numpy pandas matplotlib
```

---

## **4. Saving Installed Packages (for Reusability)**
To save all installed packages:
```bash
pip freeze > requirements.txt
```

---

## **5. Restoring Packages from `requirements.txt`**
To reinstall dependencies:
```bash
pip install -r requirements.txt
```

---

## **6. Checking Installed Packages**
```bash
pip list
```
or  
```bash
pip freeze
```

---

## **7. Removing a Package**
```bash
pip uninstall package_name
```

---

## **8. Updating a Package**
```bash
pip install --upgrade package_name
```

---

## **9. Deleting (Removing) the Virtual Environment**
If you no longer need the virtual environment, delete the folder:
```bash
rm -rf venv   # Linux/macOS
rmdir /s /q venv   # Windows (cmd)
```
Then recreate it if needed:
```bash
python -m venv venv
```

---

## **10. Checking Which Python is Used in the Virtual Environment**
```bash
which python   # macOS/Linux
where python   # Windows
```
It should show the path inside the `venv` folder.

---

## **11. Avoid Common Mistakes**
✅ Always **activate** the virtual environment before installing packages.  
✅ Use `pip freeze > requirements.txt` to track dependencies.  
✅ Don't install system-wide packages inside the virtual environment.  

---

Following these best practices will help you efficiently manage your **Python virtual environments**! 🚀
