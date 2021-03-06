import argparse
from syslog import LOG_INFO
from syslog import syslog


def db_log(msg, ident=LOG_INFO):
    print(msg)
    syslog(ident, msg)


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
