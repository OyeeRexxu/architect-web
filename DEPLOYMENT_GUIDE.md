# Fixing Missing Dropdown & Footer on PythonAnywhere

The issue where the Services dropdown and footer links are missing on PythonAnywhere (but working locally) is likely due to the production environment needing a refresh.

Follow these 3 steps to fix it:

## 1. Pull Latest Changes
Open a **Bash console** on PythonAnywhere and run:
```bash
cd architect-web  # Adjust folder name if different
git pull
```

## 2. Apply Migrations (Just in case)
While still in the console, ensure the database is in sync:
```bash
python manage.py migrate
```

## 3. Reload the Web App
1. Go to the **Web** tab in your PythonAnywhere dashboard.
2. Click the green **Reload** button at the top.

---

### Why this happens?
The "Context Processors" (which inject the services into the navbar/footer) are loaded when the application starts. If you added services or changed code locally, the running process on the server needs to be restarted to pick up those changes and serve the correct data to the templates.
