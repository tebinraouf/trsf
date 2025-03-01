from dotenv import load_dotenv
import os
import subprocess
import shlex
import typer
from groq import Groq
import readline  # Import the readline module

# Load ENV variables
load_dotenv()

HISTFILE = os.path.join(os.path.expanduser("~"), ".trsf_history")

try:
    readline.read_history_file(HISTFILE)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

app = typer.Typer()

# Initialize Groq client using the API key from environment variables
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_error_with_groq(error_message: str) -> str:
    """Send the error message to Groq API and retrieve a suggestion."""
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Error: {error_message}\n Please provide a suggestion to fix this issue. Make it concise and clear. Provide next command to run.",
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Failed to get a suggestion from Groq: {e}"


@app.command()
def trsf():
    """Continuously listen for terminal commands and suggest fixes on errors."""
    try:
        while True:
            try:
                command = input("$ ")
                if command.lower() in ["exit", "quit"]:
                    break

                process = subprocess.run(
                    shlex.split(command), capture_output=True, text=True, shell=True
                )

                if process.returncode != 0:
                    print(f"Error: {process.stderr.strip()}")
                    suggestion = analyze_error_with_groq(process.stderr.strip())
                    print(f"💡 Suggestion: {suggestion}")
                else:
                    print(process.stdout.strip())

            except KeyboardInterrupt:
                print("\nExiting...")
                break
    finally:
        readline.write_history_file(HISTFILE)


@app.command()
def main():
    typer.echo("TRSF is running!!")
    trsf()


if __name__ == "__main__":
    app()
