import subprocess
import time
import pytest
import os
import sys
import signal

# Path to the cloned app
APP_DIR = "builds/cloned_app"


def run_evaluation():
    print("--- 🚀 STARTING AGENT EVALUATION ---")

    if not os.path.exists(APP_DIR):
        print(f"❌ Error: Output directory '{APP_DIR}' not found.")
        print("   Please run 'python main.py' first.")
        sys.exit(1)

    app_process = None
    try:
        print(f"   -> Starting Next.js app in '{APP_DIR}'...")
        app_process = subprocess.Popen(
            ["pnpm", "run", "dev"],
            cwd=APP_DIR,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid
        )

        print("   -> Waiting 10 seconds for app to boot...")
        time.sleep(10)

        poll = app_process.poll()
        if poll is not None:
            print("❌ Error: Next.js app failed to start.")
            print(app_process.stderr.read().decode())
            return

        print("✅ App is running.")

        print("\n--- RUNNING PYTEST ---")
        pytest_args = [
            "evaluation/tests/test_visuals.py",
            "--headed"
        ]

        exit_code = pytest.main(pytest_args)
        print("--- PYTEST COMPLETE ---")

        if exit_code == 0:
            print("\n--- 🥳 EVALUATION SUCCEEDED ---")
        else:
            print("\n--- 🥵 EVALUATION FAILED ---")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

    finally:
        if app_process and app_process.poll() is None:
            print("\n   -> Shutting down Next.js app...")
            os.killpg(os.getpgid(app_process.pid), signal.SIGTERM)
            app_process.wait()
            print("✅ App shut down.")

        print("--- 🚀 EVALUATION COMPLETE ---")


if __name__ == "__main__":
    run_evaluation()