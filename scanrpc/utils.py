from substrateinterface import SubstrateInterface, Keypair
from scalecodec.type_registry import SUPPORTED_TYPE_REGISTRY_PRESETS
from scalecodec.type_registry import load_type_registry_preset, load_type_registry_file
import json, hashlib

#
# get_config - Get a default config elements from args and config.
#
def get_config(args, config, key, section='Defaults'):
    if vars(args).get(key) is not None:
        return vars(args)[key]

    if config[section].get(key) is not None:
        return config[section].get(key)

    return config['Defaults'].get(key)


#
# format_balance_to_symbol - Formats a balance in the base decimals of the chain
#
def format_balance_to_symbol(substrate, amount, amount_decimals=0):
    formatted = amount / 10 ** (substrate.token_decimals - amount_decimals)
    formatted = "{:.{}f}".format(formatted, substrate.token_decimals)

    # expected format -> 5.780520362127 KSM
    return f"{formatted} {substrate.token_symbol}"


#
# get_ss58_address_format - Gets the SS58 address format depending on the network
# 
def get_ss58_address_format(network):
    network = network.lower()

    if network == "polkadot": return 0
    if network == "sr25519": return 1
    if network == "kusama": return 2
    if network == "ed25519": return 3
    if network == "katalchain": return 4
    if network == "plasm": return 5
    if network == "bifrost": return 6
    if network == "edgeware": return 7
    if network == "karura": return 8
    if network == "reynolds": return 9
    if network == "acala": return 10
    if network == "laminar": return 11
    if network == "polymath": return 12
    if network == "substratee": return 13
    if network == "totem": return 14
    if network == "synesthesia": return 15
    if network == "kulupu": return 16
    if network == "dark": return 17
    if network == "darwinia": return 18
    if network == "geek": return 19
    if network == "stafi": return 20
    if network == "dock-testnet": return 21
    if network == "dock-mainnet": return 22
    if network == "shift": return 23
    if network == "zero": return 24
    if network == "alphaville": return 25
    if network == "jupiter": return 26
    if network == "subsocial": return 28
    if network == "cord": return 29
    if network == "phala": return 30
    if network == "litentry": return 31
    if network == "robonomics": return 32
    if network == "datahighway": return 33
    if network == "ares": return 34
    if network == "vln": return 35
    if network == "centrifuge": return 36
    if network == "nodle": return 37
    if network == "kilt": return 38
    if network == "poli": return 41
    if network == "substrate": return 42
    if network == "westend": return 42
    if network == "amber": return 42
    if network == "secp256k1": return 43
    if network == "chainx": return 44
    if network == "uniarts": return 45
    if network == "reserved46": return 46
    if network == "reserved47": return 47
    if network == "neatcoin": return 48
    if network == "hydradx": return 63
    if network == "aventus": return 65
    if network == "crust": return 66
    if network == "equilibrium": return 67
    if network == "sora": return 69
    if network == "social-network": return 252
        
    return 42

#
# get_type_preset - Gets the type preset for the network
# 
def get_type_preset(network):
    if network in SUPPORTED_TYPE_REGISTRY_PRESETS:
        return network
    else:
        return "substrate-node-template"

#
# get_substrate_interface - Defines a substrate interface based on default network
# types or a custom types file
# 
def get_substrate_interface(args, config):
    # get default type preset based on network configuration
    network = get_config(args, config, 'network')
    type_preset = get_type_preset(network)
    # by default, load types from this preset
    type_registry = load_type_registry_preset(type_preset)

    # get custom types file. If defined, load types from it
    custom_types_file = get_config(args, config, 'types_registry')
    if custom_types_file is not None and custom_types_file != '':
        type_registry = load_type_registry_file(custom_types_file)

    substrate = SubstrateInterface(
        url=get_config(args, config, 'rpc_url'),
        address_type=get_ss58_address_format(network),
        type_registry_preset=type_preset,
        type_registry=type_registry,
    )

    return substrate



def get_hashed_value(value):
    return hashlib.sha256(
        json.dumps(
            value
        ).encode('utf-8')
    )

def subscription_handler(obj, update_nr, subscription_id):
    hashed_val =  get_hashed_value(obj.value)

    if update_nr == 0:
        print('state_subscribeStorage,state_unsubscribeStorage:', 'initial(hashed)', hashed_val.hexdigest())

    if update_nr > 0:
    # Do something with the update
        print('state_subscribeStorage,state_unsubscribeStorage:', 'changed(hashed)', hashed_val.hexdigest())

    # The execution will block until an arbitrary value is returned, which will be the result of the `query`
    if update_nr > 1:
        return obj


def handle_exception(calls, exception, method, is_unsafe, unsafe_enabled, fail_ok=False, expected_fail_msg='', user_message=''):
    if is_unsafe:
        if unsafe_enabled:
            print(f" ✘ {method}: {str(exception)}")
            calls[-1]['status'] = 'error'
            calls[-1]['reason'] = 'unsafe method failed'
            calls[-1]['message'] = user_message
            calls[-1]['error'] = str(exception)
        if unsafe_enabled == False and not 'Method not found' in str(exception) and not 'UnsafeRpcCalled' in str(exception):
            print(f" ✘ {method}: {str(exception)}")
            calls[-1]['status'] = 'error'
            calls[-1]['reason'] = 'unsafe method failed'
            calls[-1]['message'] = user_message
            calls[-1]['error'] = str(exception)
        if unsafe_enabled == False and ('Method not found' in str(exception) or 'UnsafeRpcCalled' in str(exception)):
            print(f" ✔ {method}: Unsafe method disabled")
    else:
        if fail_ok and expected_fail_msg in str(exception):
            print(f" ✔ {method}: Method available. {user_message}")
            calls[-1]['status'] = 'warn'
            calls[-1]['reason'] = 'warn - safe method not completely tested'
            calls[-1]['message'] = user_message
            calls[-1]['error'] = str(exception)
        else:
            print(f" ✘ {method}: {str(exception)}")
            calls[-1]['status'] = 'error'
            calls[-1]['reason'] = 'safe method failed'
            calls[-1]['message'] = user_message
            calls[-1]['error'] = str(exception)

