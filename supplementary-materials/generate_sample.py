import numpy as np
import pandas as pd

random_seed = 1
count = 75

def main():
    np.random.seed(random_seed)
    df = pd.read_csv('novels-model-1837-1901-20180227.csv', index_col=0)
    df.columns = [col[0] for col in df.columns]  # just 'm', 'w', 'u'
    dfm = pd.melt(df.reset_index(), id_vars=['year'], var_name='gender')
    assert len(dfm) == 3 * (1901 - 1837 + 1)
    proba = dfm['value'].values / dfm['value'].sum()
    records = []
    for draw_index in range(count):
        row = dfm.iloc[np.random.choice(len(dfm), p=proba)]
        records.append((draw_index + 1, ) + tuple(row[['year', 'gender']].tolist()))
    columns = ['sequence_number', 'year', 'gender']
    draws = pd.DataFrame.from_records(records, columns=columns).set_index('sequence_number')  # noqa
    filename = '/tmp/novels-1837-1901-random-sample-20180227.csv'
    draws.to_csv(filename)
    print(f'draws saved to {filename}')


if __name__ == '__main__':
    main()
