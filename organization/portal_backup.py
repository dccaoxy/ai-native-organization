"""Verified SQLite backup and restore helpers for the isolated test portal."""
import argparse
from contextlib import closing
import os
from pathlib import Path
import secrets
import sqlite3


def verify(path):
    path=Path(path)
    if not path.is_file():raise FileNotFoundError(path)
    with closing(sqlite3.connect(f'file:{path.as_posix()}?mode=ro',uri=True)) as db:
        result=db.execute('PRAGMA integrity_check').fetchone()[0]
    if result!='ok':raise ValueError(f'integrity_check failed: {result}')
    return {'path':str(path.resolve()),'integrity_check':'ok','size':path.stat().st_size}


def backup(source,destination):
    source=Path(source);destination=Path(destination)
    if not source.is_file():raise FileNotFoundError(source)
    if destination.exists():raise FileExistsError(f'backup destination already exists: {destination}')
    destination.parent.mkdir(parents=True,exist_ok=True)
    temporary=destination.with_name(destination.name+'.tmp-'+secrets.token_hex(8))
    try:
        with closing(sqlite3.connect(f'file:{source.as_posix()}?mode=ro',uri=True)) as source_db:
            with closing(sqlite3.connect(temporary)) as destination_db:source_db.backup(destination_db)
        receipt=verify(temporary)
        os.replace(temporary,destination)
        return {**receipt,'path':str(destination.resolve())}
    finally:
        if temporary.exists():temporary.unlink()


def restore(source,target):
    source=Path(source);target=Path(target)
    verify(source)
    if target.exists():raise FileExistsError(f'restore target already exists: {target}')
    return backup(source,target)


def main():
    parser=argparse.ArgumentParser();commands=parser.add_subparsers(dest='command',required=True)
    for name in ('backup','restore'):
        command=commands.add_parser(name);command.add_argument('source');command.add_argument('destination')
    verify_command=commands.add_parser('verify');verify_command.add_argument('source')
    args=parser.parse_args()
    if args.command=='backup':result=backup(args.source,args.destination)
    elif args.command=='restore':result=restore(args.source,args.destination)
    else:result=verify(args.source)
    print(result)


if __name__=='__main__':main()
