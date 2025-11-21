import os
import sys
import subprocess
from pathlib import Path


def is_project_venv_active(venv_names=('.venv', 'venv', 'env', 'ENV')):
    """Return True if the current Python interpreter appears to be the project's
    virtual environment. We consider the venv active if the VIRTUAL_ENV
    environment variable points to a venv inside the project folder or if the
    interpreter executable is inside a venv folder in the project.
    """
    base = Path(__file__).resolve().parent

    # Check VIRTUAL_ENV env var first (standard for venv/virtualenv)
    venv_env = os.environ.get('VIRTUAL_ENV')
    if venv_env:
        try:
            venv_path = Path(venv_env).resolve()
            for name in venv_names:
                if venv_path == (base / name).resolve():
                    return True
        except Exception:
            pass

    # Fallback: check if the current python executable sits under a venv folder in project
    try:
        exe_path = Path(sys.executable).resolve()
        for name in venv_names:
            if (base / name).resolve() in exe_path.parents:
                return True
    except Exception:
        pass

    return False


def ensure_package(pkg_name):
    """Ensure a package is importable in the current Python environment.
    If not present, attempt to install it with pip into the active env.
    """
    try:
        __import__(pkg_name)
        return
    except ImportError:
        pass

    try:
        print(f"Package '{pkg_name}' not found. Installing into the active environment...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg_name])
        __import__(pkg_name)
    except Exception as e:
        print(f"Failed to install package '{pkg_name}':", e)
        raise


base = Path(__file__).resolve().parent

# Only attempt automatic installation when the user has activated the project's venv
if is_project_venv_active():
    try:
        ensure_package('flask')
    except Exception:
        print('Could not ensure Flask is installed in the active virtual environment.')
        sys.exit(1)
else:
    # Do not create venv automatically. Instruct the user to activate per README.
    print('It looks like the project virtual environment is not active.')
    print('Follow the README instructions to create and activate the venv, for example:')
    print()
    print('  python3 -m venv .venv')
    print('  source .venv/bin/activate')
    print()
    print('When the virtual environment is active, rerun this script and it will')
    print("attempt to install Flask into that environment if it's missing.")
    sys.exit(1)

from flask import Flask


app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    # Development server; for production use a WSGI server
    app.run(debug=True, host='127.0.0.1', port=5000)
