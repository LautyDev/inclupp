import os
import re
import sys
import tempfile
import subprocess
import requests
from urllib.parse import urlparse
from colorama import init, Fore

VERSION = "1.0.0"

init(autoreset=True)

def is_url(path):
    try:
        result = urlparse(path)
        return all([result.scheme in ("http", "https"), result.netloc, result.path])
    except Exception:
        return False

def download_file(url, temp_dir):
    try:
        print(Fore.CYAN + f"🔄 Downloading: {url}")
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            raise ValueError("The URL does not contain a valid filename.")
        temp_path = os.path.join(temp_dir, filename)
        with open(temp_path, 'wb') as f:
            f.write(response.content)
        print(Fore.GREEN + f"✅ Saved to: {temp_path}")
        return temp_path
    except Exception as e:
        print(Fore.RED + f"❌ Error downloading {url}: {e}")
        sys.exit(1)

def process_file(input_path, temp_dir):
    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(Fore.RED + f"❌ Error reading {input_path}: {e}")
        sys.exit(1)

    processed_lines = []
    include_pattern = re.compile(r'^\s*#include\s+[<"]([^">]+)[">]')

    for line in lines:
        match = include_pattern.match(line)
        if match:
            path = match.group(1)
            if is_url(path):
                downloaded_path = download_file(path, temp_dir)
                processed_lines.append(f'#include "{downloaded_path}"\n')
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)

    return processed_lines

def main():
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "⚠️ Usage: inclupp <source_file.c or .cpp>")
        sys.exit(1)

    if sys.argv[1] in ("--version", "-v"):
        print(Fore.MAGENTA + f"Inclu++ version {VERSION}")
        sys.exit(0)

    source_file = sys.argv[1]
    temp_dir = tempfile.mkdtemp()

    print(Fore.CYAN + f"🔧 Processing source file: {source_file}")
    processed_code = process_file(source_file, temp_dir)

    processed_file = os.path.join(temp_dir, os.path.basename(source_file))
    try:
        with open(processed_file, 'w') as f:
            f.writelines(processed_code)
        print(Fore.GREEN + f"✅ Processed file saved to: {processed_file}")
    except Exception as e:
        print(Fore.RED + f"❌ Error writing processed file: {e}")
        sys.exit(1)

    output_executable = os.path.splitext(source_file)[0]
    compile_command = ["g++", processed_file, "-o", output_executable]

    print(Fore.CYAN + "🔨 Compiling the processed file...")
    try:
        subprocess.run(compile_command, check=True)
        print(Fore.GREEN + f"🎉 Compilation successful: {output_executable}")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"❌ Compilation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()