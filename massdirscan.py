import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Read the list of websites from the file
with open('websites_list.txt', 'r') as f:
    websites = [line.strip() for line in f.readlines()]

# Read the list of directories from the file
with open('directories.txt', 'r') as f:
    directories = [line.strip() for line in f.readlines()]

# The constant text to search for
constant_text = "some constant text"


def scan_website_directory(website, directory):
    url = f"{website}/{directory}"
    try:
        response = requests.get(url)
        if response.status_code == 200 and constant_text in response.text:
            return url
    except requests.exceptions.RequestException:
        pass
    return None


def main():
    found_urls = []

    with ThreadPoolExecutor() as executor:
        futures = []
        for website in websites:
            for directory in directories:
                futures.append(executor.submit(scan_website_directory, website, directory))

        for future in as_completed(futures):
            result = future.result()
            if result:
                found_urls.append(result)
                print(result)

    # Save the output to a file
    with open('output.txt', 'w') as f:
        for url in found_urls:
            f.write(f"{url}\n")


if __name__ == "__main__":
    main()
