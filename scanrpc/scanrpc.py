from argparse import ArgumentParser
from configparser import ConfigParser
from collections import OrderedDict

from .utils import *
from .rpc_modules import *

#
# cmd_scan - 'scan' subcommand handler.
#
def cmd_scan(args, config):
    substrate = get_substrate_interface(args, config)

    expect_unsafe_enabled = get_config(args, config, 'expect_unsafe_enabled')
    rpc_modules = get_config(args, config, 'rpc_modules')
    rpc_modules = rpc_modules.split(',')

    calls = []

    if 'account' in rpc_modules or rpc_modules == ['all']:
        scan_module_account(substrate, expect_unsafe_enabled, calls)
    if 'author' in rpc_modules or rpc_modules == ['all']:
        scan_module_author(substrate, expect_unsafe_enabled, calls)
    if 'babe' in rpc_modules or rpc_modules == ['all']:
        scan_module_babe(substrate, expect_unsafe_enabled, calls)
    if 'beefy' in rpc_modules or rpc_modules == ['all']:
        scan_module_beefy(substrate, expect_unsafe_enabled, calls)
    if 'chain' in rpc_modules or rpc_modules == ['all']:
        scan_module_chain(substrate, expect_unsafe_enabled, calls)
    if 'childstate' in rpc_modules or rpc_modules == ['all']:
        scan_module_childstate(substrate, expect_unsafe_enabled, calls)
    if 'grandpa' in rpc_modules or rpc_modules == ['all']:
        scan_module_grandpa(substrate, expect_unsafe_enabled, calls)
    if 'mmr' in rpc_modules or rpc_modules == ['all']:
        scan_module_mmr(substrate, expect_unsafe_enabled, calls)
    if 'offchain' in rpc_modules or rpc_modules == ['all']:
        scan_module_offchain(substrate, expect_unsafe_enabled, calls)
    if 'payment' in rpc_modules or rpc_modules == ['all']:
        scan_module_payment(substrate, expect_unsafe_enabled, calls)
    if 'state' in rpc_modules or rpc_modules == ['all']:
        scan_module_state(substrate, expect_unsafe_enabled, calls)
    if 'subscribe' in rpc_modules or rpc_modules == ['all']:
        scan_module_subscribe(substrate, expect_unsafe_enabled, calls)
    if 'sync' in rpc_modules or rpc_modules == ['all']:
        scan_module_sync(substrate, expect_unsafe_enabled, calls)
    if 'system' in rpc_modules or rpc_modules == ['all']:
        scan_module_system(substrate, expect_unsafe_enabled, calls)
    if 'unsubscribe' in rpc_modules or rpc_modules == ['all']:
        scan_module_unsubscribe(substrate, expect_unsafe_enabled, calls)

    failures = {}
    for call in calls:
        status = call.get('status')
        reason = call.get('reason')
        if status != 'ok':
            failures[reason] = [] if failures.get(reason) is None else failures.get(reason)
            failures[reason].append(call)

    for reason in failures:
        print(f"\n{reason.upper()}")
        print(f"------------------------------")
        for call in failures[reason]:
            message = call.get('message')
            error = call.get('error')
            if call.get('status') == 'warn':
                print(f" - {call.get('method')}. WARNING")
                print(f"   User message: {message}") if message else ""
                print(f"   Full error: {error}")
            elif call.get('status') == 'error':
                print(f" - {call.get('method')}. FAILED")
                print(f"   User message: {message}") if message else ""
                print(f"   Full error: {error}")
            else:
                print(f" - {call.get('method')}. FAILED")
                print(f"   User message: {message}") if message else ""
                print(f"   Full error: {error}")

    if failures == {}:
        print(f"------------------------------")
        print(f"Host is OK")
        


def main():
    args_parser = ArgumentParser(prog='scanrpc')
    args_parser.add_argument("-c", "--config", help="read config from a file", default="default.conf")

    args_parser.add_argument("-r", "--rpc-url", dest="rpc_url", help="substrate RPC Url")
    args_parser.add_argument("-n", "--network", dest="network", help="name of the network to connect")
    args_parser.add_argument("-f", "--types-registry-file", dest="types_registry", help="file with the types of the network to connect")
    
    args_subparsers = args_parser.add_subparsers(title="Commands", help='', dest="command")

    args_subparser_list = args_subparsers.add_parser("scan", help="scan RPC calls")
    args_subparser_list.add_argument("-u", "--expect-unsafe", dest="expect_unsafe_enabled", help='expect endpoint to have unsafe calls enabled', action='store_true', default=False)
    args_subparser_list.add_argument("-m", "--rpc-modules", dest="rpc_modules", help='rpc modules to scan', default='all')

    args = args_parser.parse_args()

    try:
        config = ConfigParser()
        config.read_file(open(args.config))
    except Exception as exc:
        print(f"Unable to read config: {str(exc)}")
        exit(0)

    if not args.command:
        args_parser.print_help()
        exit(1)

    if args.command == 'scan':
        cmd_scan(args, config)


if __name__ == '__main__':
    main()
