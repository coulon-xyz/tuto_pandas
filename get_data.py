import urllib.request
import os
import sys
import pandas as pd

ABSOLUTE = os.path.join(os.path.dirname(__file__))
OUTPUT = os.path.join(ABSOLUTE, "runtime")

url_root = 'https://coinmetrics.io/data/'


def download_file(url, file_name):
    output_path = os.path.join(OUTPUT, file_name)
    urllib.request.urlretrieve(url, output_path)
    return output_path

def build_url(url, acronym):
    return url + acronym + ".csv"

def download_prices(acronyms):
    for acronym in acronyms:
        out_file = acronym + ".csv"
        p =download_file(build_url(url_root, acronym), out_file)


if __name__ == "__main__":
    acronyms = ['eth', 'btc', 'bch', 'ltc', 'xem', 'dcr', 'zec', 'dash', 'doge', 'etc', 'pivx', 'xmr', 'vtc']
    download_prices(acronyms)
    # df = build_df(acronyms)


