import subprocess


def main():
    subprocess.run(["black", "."], check=True)
    subprocess.run(["isort", "."], check=True)


if __name__ == "__main__":
    main()
