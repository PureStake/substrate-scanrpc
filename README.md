# Substrate RPC Scan

Simple command line application to scan the RPC methods of a Substrate node.

## Install

Clone the repository and install the package:

```bash
git clone http://github.com/PureStake/substrate-scanrpc
pip install substrate-scanrpc/
```

NOTE: pip install argument is ambiguous at it can refer to a python package or a local folder. Make sure to include the '/' at the end to avoid ambiguity.


## Usage

After installing the package the _scanrpc_ executable should be available on the system.

```bash
$ scanrpc
usage: scanrpc [-h] [-c CONFIG] [-r RPC_URL] [-n NETWORK] [-f TYPES_REGISTRY] {scan} ...

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        read config from a file
  -r RPC_URL, --rpc-url RPC_URL
                        substrate RPC Url
  -n NETWORK, --network NETWORK
                        name of the network to connect
  -f TYPES_REGISTRY, --types-registry-file TYPES_REGISTRY
                        file with the types of the network to connect

Commands:
  {scan}
    scan                scan RPC calls
```

### Configuration 

The config contains the default parameters:

```bash
[Defaults]
# Endpoint to use
RPC_URL = wss://kusama-rpc.polkadot.io/
# Network to connect
Network = kusama
# Which RPC modules to scan (comma separated list)
RPC_Modules = all
# File with the types of the network to connect
Types_Registry = 
```

### Examples

Full scan of the RPC calls of the default endpoint:

```bash
$ scanrpc scan
```

Full scan of the RPC calls of a custom endpoint:

```bash
$ scanrpc --rpc-url ws://localhost:9944 scan
```

Scan of the `system` module:

```bash
$ scanrpc scan -m system
 ✔ system_accountNextIndex: 18569
 ✔ system_addLogFilter: Unsafe method disabled
 ✔ system_addReservedPeer: Unsafe method disabled
 ✔ system_chain: Kusama
 ✔ system_chainType: Live
 ✔ system_dryRun: Unsafe method disabled
 ✔ system_dryRunAt: Unsafe method disabled
 ✔ system_health: {'isSyncing': False, 'peers': 123, 'shouldHavePeers': True}
 ✔ system_localListenAddresses: ['/ip4/127.0.0.1/tcp/30333/p2p/12D3KooWNUJ5izQKaxbzFcxt4kv71GBLw5QTXWqXBG67g98GaeqQ', '/ip4/10.200.0.82/tcp/30333/p2p/12D3KooWNUJ5izQKaxbzFcxt4kv71GBLw5QTXWqXBG67g98GaeqQ']
 ✔ system_localPeerId: 12D3KooWNUJ5izQKaxbzFcxt4kv71GBLw5QTXWqXBG67g98GaeqQ
 ✔ system_name: Parity Polkadot
 ✔ system_nodeRoles: ['Full']
 ✔ system_peers: Unsafe method disabled
 ✔ system_properties: {'ss58Format': 2, 'tokenDecimals': 12, 'tokenSymbol': 'KSM'}
 ✔ system_removeReservedPeer: Unsafe method disabled
 ✔ system_reservedPeers: []
 ✔ system_resetLogFilter: Unsafe method disabled
 ✔ system_syncState: {'currentBlock': 7869803, 'highestBlock': 7869803, 'startingBlock': 7840261}
 ✔ system_unstable_networkState: Unsafe method disabled
 ✔ system_version: 0.9.3-aa3867609-x86_64-linux-gnu
------------------------------
Host is OK
```
