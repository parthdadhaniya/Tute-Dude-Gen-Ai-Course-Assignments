# Streamlit entry point alias
# Student: Parth Dadhaniya

import os
import runpy

if __name__ == "__main__":
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    runpy.run_path(app_path, run_name="__main__")
else:
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    runpy.run_path(app_path, run_name="__main__")

