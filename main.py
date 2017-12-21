

if __name__ == "__main__":
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

    pass