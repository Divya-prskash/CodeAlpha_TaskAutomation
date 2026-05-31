import os
import re
import shutil

def move_jpg_files(source_folder=".", dest_folder="JPG_Files"):
    """Move all .jpg files from source_folder into dest_folder."""
    os.makedirs(dest_folder, exist_ok=True)
    moved = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            src = os.path.join(source_folder, file)
            dst = os.path.join(dest_folder, file)
            shutil.move(src, dst)
            print(f"  Moved: {file} -> {dest_folder}/")
            moved += 1
    print(f"  {moved} .jpg file(s) moved." if moved else "  No .jpg files found.")

def extract_emails(input_file="emails_input.txt", output_file="emails_output.txt"):
    """Extract all email addresses from input_file and save to output_file."""
    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write("Contact alice@example.com or bob@work.org for info.\n")
            f.write("Also reach charlie@mail.net and dave@company.co.uk.\n")
        print(f"  Demo file '{input_file}' created.")

    with open(input_file, "r") as f:
        content = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", content)
    unique_emails = list(dict.fromkeys(emails))

    with open(output_file, "w") as f:
        f.write("\n".join(unique_emails))

    print(f"  {len(unique_emails)} email(s) extracted -> saved to '{output_file}'")
    for e in unique_emails:
        print(f"     {e}")

def scrape_webpage_title(url="https://www.codealpha.tech", output_file="webpage_title.txt"):
    """Scrape the title of a webpage and save it."""
    try:
        import urllib.request
        with urllib.request.urlopen(url, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")
        match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        title = match.group(1).strip() if match else "No title found"
        with open(output_file, "w") as f:
            f.write(f"URL   : {url}\nTitle : {title}\n")
        print(f"  Title scraped: '{title}' -> saved to '{output_file}'")
    except Exception as e:
        print(f"  Could not fetch URL ({e}). Saving placeholder.")
        with open(output_file, "w") as f:
            f.write(f"URL   : {url}\nTitle : (Could not fetch - check internet connection)\n")

def main():
    print("=" * 45)
    print("    Task Automation with Python")
    print("=" * 45)
    print("1. Move all .jpg files to a new folder")
    print("2. Extract emails from a .txt file")
    print("3. Scrape webpage title and save it")
    print("4. Run ALL automations")
    print("0. Exit")

    choice = input("\nChoose an option: ").strip()
    print()

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        scrape_webpage_title()
    elif choice == "4":
        print("-- Moving .jpg files --")
        move_jpg_files()
        print("\n-- Extracting emails --")
        extract_emails()
        print("\n-- Scraping webpage title --")
        scrape_webpage_title()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
