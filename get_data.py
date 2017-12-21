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
        print("{} was download in {}".format(acronym, p))
def build_df(acronyms):
    l_df = list()
    for acronym in acronyms:
        file_to_load = os.path.join(OUTPUT, acronym + ".csv")
        print("-- {} --".format(acronym))
        df = pd.read_csv(file_to_load, index_col=False, usecols=['date', 'price(USD)'])
        df = df.set_index("date")
        df = df.rename(columns={'price(USD)': acronym})
        l_df.append(df)
        del df

    return pd.concat(l_df, axis=1)


if __name__ == "__main__":
    acronyms = ['eth', 'btc', 'bch', 'ltc', 'xem', 'dcr', 'zec', 'dash', 'doge', 'etc', 'pivx', 'xmr', 'vtc']
    download_prices(acronyms)
    # df = build_df(acronyms)


