#!/usr/bin/env python3

import sys
import urllib.parse
import webbrowser

def main():
    command = sys.argv[1]

    if command == "google" and len(sys.argv) > 2:
        query = " ".join(sys.argv[2:])
        encoded_query = urllib.parse.quote(query)
        url = f"https://google.com/search?q={encoded_query}"
        webbrowser.open(url)
        
        
if __name__ == "__main__":
    main()