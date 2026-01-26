# Deployment Guide - PythonAnywhere

## 🚀 The "Magic" Build Command
We have created a script that automates everything (git pull, installing requirements, database migrations).

**Whenever you make changes, just do this:**

1. Open a **Bash Console** on PythonAnywhere.
2. Run this command:
   ```bash
   ./build.sh
   ```
3. Go to the **Web** tab and click **Reload**.

---

## Troubleshooting Common Errors

### "No module named 'PIL'"
**Cause:** The `Pillow` library hasn't been installed on the server yet.
**Fix:** Run the `./build.sh` command above. It will automatically run `pip install` for you.

### "Database is locked" or Merge Conflicts
**Cause:** The database changed on the server while you were working.
**Fix:** The `./build.sh` script now automatically handles this by backing up your live database, pulling the code, and then restoring your data. Just run the script.

### "Static files not missing" (CSS/Images gone)
**Cause:** New images weren't collected to the valid folder.
**Fix:** The `./build.sh` script runs `collectstatic` automatically. just run it.
