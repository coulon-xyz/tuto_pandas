import urllib.request
import os
import constants



def download_file(url, file_name):
    output_path = os.path.join(constants.OUTPUT, file_name)
    urllib.request.urlretrieve(url, output_path)
    return output_path


def build_url(url, acronym):
    return url + acronym + ".csv"


def download_prices(acronyms):
    for acronym in acronyms:
        out_file = acronym + ".csv"
        p =download_file(build_url(constants.api_url_root, acronym), out_file)
        print("{} was download in {}".format(acronym, p))


if __name__ == "__main__":
    download_prices(constants.acronyms)


