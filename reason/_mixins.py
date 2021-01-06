import pandas as pd


def progress_bar(iteration, total, prefix='', suffix=''):
    length = 60
    percent = '{0:.1f}'.format(100 * (iteration / float(total)))
    filled = int(length * iteration // total)
    bar = '#' * filled + '-' * (length - filled)
    print('{prefix} [{bar}] {percent}% {suffix}'.format(
        prefix=prefix, bar=bar, percent=percent, suffix=suffix
    ))

    if iteration == total:
        print()


def is_featuresets_format(input_data):
    if (
        not isinstance(input_data, list) or
        not all(isinstance(item, dict) for item in input_data)
    ):
        return False

    return True


def featuresets_to_dataframe(featuresets):
    data = dict()
    features = featuresets[0].keys()

    for feature in features:
        data[feature] = pd.Series(set[feature] for set in featuresets)

    df = pd.DataFrame(data=data)

    return df
