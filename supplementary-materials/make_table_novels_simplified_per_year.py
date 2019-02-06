# Note: Running this script requires code in "Reassembling the Novel". It is
# included here for reference only.
"""Make table showing novels by year and gender, 1837-1901.

Not used in paper.

"""
import argparse
import functools

import numpy as np
import pandas as pd

import datasets
import inference

parser = argparse.ArgumentParser()
parser.add_argument('output_filename', help='Output path for data frame.')


@functools.lru_cache()
def dataset_and_draws():
    """Gather dataset and draws from posterior distributions."""
    raven_forster = datasets.raven_forster_1789_1799()
    novels_1800_1836 = datasets.garside_schöwerling_title_counts()
    novels_1800_1829_by_gender = datasets.garside_schöwerling_title_counts_by_gender()
    df = pd.DataFrame(dict(novels=pd.concat([raven_forster, novels_1800_1836])))
    df = df.join(novels_1800_1829_by_gender)

    # pad dataframe to 1919
    df = pd.concat([df, pd.DataFrame(dict(novels=float('nan')), index=range(1837, 1919 + 1))])
    df = df.join(datasets.publishers_circular())
    df = df.join(datasets.andrew_block())

    # add nstc
    df = df.join(datasets.nineteenth_century_short_title_catalogue_loced())

    # add bassett priors
    bassett_discounted = datasets.bassett_at_the_circulating_library_priors_discounted()
    df = df.join(bassett_discounted[['bassett_25_percentile', 'bassett_50_percentile', 'bassett_75_percentile']])

    # add ellen miller casey athenaeum counts
    df = df.join(datasets.casey_athenaeum_novels())

    # add reader population estimates
    df = df.join(datasets._population_readers())
    df = df.join(datasets._population())

    # add inferences
    fit_extract = inference.sampling()
    return df, fit_extract


def dataset_years():
    """Assembles dataframe for yearly rate table."""
    df, fit_extract = dataset_and_draws()
    fit_extract = fit_extract.copy()
    raven_forster_fit_extract = inference.posterior_raven_forster_1789_1799()

    # combine fit_extract with raven forster
    for var_name in ['y_sim', 'y_unknown_sim', 'y_men_sim', 'y_women_sim']:
        fit_extract[var_name] = np.hstack([raven_forster_fit_extract[var_name], fit_extract[var_name]])
        assert fit_extract[var_name].shape == (10_000, 120 + 11)

    for var_name in ['y_sim', 'y_unknown_sim', 'y_men_sim', 'y_women_sim']:
        p50, p95 = np.split(pd.DataFrame(fit_extract[var_name]).quantile([0.50, 0.95], axis=0).values, 2)
        df.loc[1789:1919, f'{var_name}_p50'], df.loc[1789:1919, f'{var_name}_p95'] = p50.ravel(), p95.ravel()

    assert int(df.loc[1789, 'y_unknown_sim_p50']) > 1
    return df


def make_table_by_year(filename):
    """Make table showing number of new titles published by year and gender.

    Covers the entire period, 1789 to 1919 (inclusive).

    """
    df = dataset_years()

    columns_oi = ['y_men_sim_p50', 'y_women_sim_p50', 'y_unknown_sim_p50']
    df = df[columns_oi]
    df.index.name = 'year'
    df = df.rename(columns={
        'y_men_sim_p50': 'man_authored_p50',
        'y_women_sim_p50': 'woman_authored_p50',
        'y_unknown_sim_p50': 'unknown_p50',
    })
    df.loc[1837:1901].to_csv(filename)
    print(f'saved data frame to {filename}')
    return df


if __name__ == '__main__':
    args = parser.parse_args()
    make_table_by_year(args.output_filename)
