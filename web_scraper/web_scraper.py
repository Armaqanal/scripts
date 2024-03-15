import requests
import argparse


def fetch_content(url, output_path="output.text"):
    response = requests.get(url)
    content = response.text
    print(content)
    with open(output_path, "w") as file:
        file.write(content)


# fetch_content("https://reqres.in/api/users%22", "output.text")

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="url required !", required=True)
parser.add_argument("--output", help="output_path required !")
args = parser.parse_args()

if args.url is not None:
    if args.output is not None:
        fetch_content(args.url, args.output)
    else:
        fetch_content(args.url)
