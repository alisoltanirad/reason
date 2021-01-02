def progress_bar (iteration, total, prefix = '', suffix = ''):
    length = 60
    percent = '{0:.1f}'.format(100 * (iteration / float(total)))
    filled = int(length * iteration // total)
    bar = '#' * filled + '-' * (length - filled)
    print('{prefix} [{bar}] {percent}% {suffix}'.format(
        prefix=prefix, bar=bar, percent=percent, suffix=suffix
    ))

    if iteration == total:
        print()
