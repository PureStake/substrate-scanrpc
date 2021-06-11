from .utils import *


def scan_module_account(substrate, expect_unsafe_enabled, calls=[]):
    method = 'account_nextIndex'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.get_account_nonce('E7ncQKp4xayUoUdpraxBjT7NzLoayLJA4TuPcKKboBkJ5GH')}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_author(substrate, expect_unsafe_enabled, calls=[]):
    method = 'author_hasKey'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x', ''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'author_hasSessionKeys'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'author_insertKey'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['', '', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'author_pendingExtrinsics'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'author_removeExtrinsic'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [[]])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'author_rotateKeys'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'author_submitAndWatchExtrinsic'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled, 
            fail_ok=True, expected_fail_msg='Could not decode `OpaqueExtrinsic.0`',
            user_message="However, this tool is unable to generate a valid extrinsic"
        )
    
    method = 'author_submitExtrinsic'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled, 
            fail_ok=True, expected_fail_msg='Could not decode `OpaqueExtrinsic.0`',
            user_message="However, this tool is unable to generate a valid extrinsic"
        )
    
    method = 'author_unwatchExtrinsic'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_babe(substrate, expect_unsafe_enabled, calls=[]):
    method = 'babe_epochAuthorship'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_beefy(substrate, expect_unsafe_enabled, calls=[]):
    method = 'beefy_subscribeJustifications'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'beefy_unsubscribeJustifications'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_chain(substrate, expect_unsafe_enabled, calls=[]):
    method = 'chain_getBlock'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0xe360cc614f6de435a6e1e2598795aca7ca9dfc658b84ecf8e7139b89d7a161e3'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_getBlockHash'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [5000000])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_getFinalisedHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_getFinalizedHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_getHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0xb267ffd706bbb93779eab04f47c7038031657b0a863794dbdd73170e3976c3e7'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
        fail_ok=True, expected_fail_msg="the max block number is u32",
        user_message="This method is deprecated. Use chain_getHeader instead")

    method = 'chain_getHeader'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0xe360cc614f6de435a6e1e2598795aca7ca9dfc658b84ecf8e7139b89d7a161e3'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_getRuntimeVersion'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0xe360cc614f6de435a6e1e2598795aca7ca9dfc658b84ecf8e7139b89d7a161e3'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_subscribeAllHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_subscribeFinalisedHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_subscribeFinalizedHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_subscribeNewHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_subscribeNewHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_subscribeRuntimeVersion'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_unsubscribeAllHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_unsubscribeFinalisedHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_unsubscribeFinalizedHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_unsubscribeNewHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_unsubscribeNewHeads'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'chain_unsubscribeRuntimeVersion'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_childstate(substrate, expect_unsafe_enabled, calls=[]):
    method = 'childstate_getKeys'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg='InvalidChildStorageKey',
            user_message='However, this tool is unable to generate a valid childKey'
        )

    method = 'childstate_getStorage'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg='InvalidChildStorageKey',
            user_message='However, this tool is unable to generate a valid childKey'
        )

    method = 'childstate_getStorageHash'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg='InvalidChildStorageKey',
            user_message='However, this tool is unable to generate a valid childKey'
        )

    method = 'childstate_getStorageSize'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg='InvalidChildStorageKey',
            user_message='However, this tool is unable to generate a valid childKey'
        )


def scan_module_grandpa(substrate, expect_unsafe_enabled, calls=[]):
    method = 'grandpa_proveFinality'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        res = substrate.rpc_request(method, [5000000])['result']
        print(f" ✔ {method}: (hashed) {get_hashed_value(res).hexdigest()}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg='Block not covered by authority set changes',
            user_message="However, this tool is unable to set a correct block number to receive a correct response"
        )

    method = 'grandpa_roundState'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        res = substrate.rpc_request(method, [])['result']
        print(f" ✔ {method}: (hashed) {get_hashed_value(res).hexdigest()}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'grandpa_subscribeJustifications'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'grandpa_unsubscribeJustifications'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'grandpa_unsubscribeJustifications'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_mmr(substrate, expect_unsafe_enabled, calls=[]):
    method = 'mmr_generateProof'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [1])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
        fail_ok=True, expected_fail_msg="Error while generating the proof",
        user_message="However, this tool is unable to generate a valid leafIndex"
        )


def scan_module_offchain(substrate, expect_unsafe_enabled, calls=[]):
    method = 'offchain_localStorageGet'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['LOCAL', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'offchain_localStorageSet'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['LOCAL', '0x', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_payment(substrate, expect_unsafe_enabled, calls=[]):
    method = 'payment_queryFeeDetails'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
        fail_ok=True, expected_fail_msg="Could not decode `OpaqueExtrinsic.0`",
        user_message="However, this tool is unable to generate a valid extrinsic"
        )
    
    method = 'payment_queryInfo'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
        fail_ok=True, expected_fail_msg="Could not decode `OpaqueExtrinsic.0`",
        user_message="However, this tool is unable to generate a valid extrinsic"
        )


def scan_module_state(substrate, expect_unsafe_enabled, calls=[]):
    method = 'state_call'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['', '0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg="Exported method  is not found",
            user_message="However, this tool is unable to find a valid exported method"
        )
    
    method = 'state_callAt'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['', '0x', '0xe360cc614f6de435a6e1e2598795aca7ca9dfc658b84ecf8e7139b89d7a161e3'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg="Exported method  is not found",
            user_message="However, this tool is unable to find a valid exported method"
        )
    
    method = 'state_getChildReadProof'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x', ['0x']])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled,
            fail_ok=True, expected_fail_msg='InvalidChildStorageKey',
            user_message='However, this tool is unable to generate a valid childKey'
        )
    
    method = 'state_getKeys'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x5c0d1176a568c1f92944340dbfed9e9c530ebca703c85910e7164cb7d1c9e47b'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getKeysPaged'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x5c0d1176a568c1f92944340dbfed9e9c530ebca703c85910e7164cb7d1c9e47b', 1])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getKeysPagedAt'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x5c0d1176a568c1f92944340dbfed9e9c530ebca703c85910e7164cb7d1c9e47b', 1, '0xe360cc614f6de435a6e1e2598795aca7ca9dfc658b84ecf8e7139b89d7a161e3'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getMetadata'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        res = substrate.rpc_request(method, [])['result']
        print(f" ✔ {method}: (hashed) {get_hashed_value(res).hexdigest()}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getPairs'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x5c0d1176a568c1f92944340dbfed9e9c530ebca703c85910e7164cb7d1c9e47b'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getReadProof'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        res = substrate.rpc_request(method, [['0x']])['result']
        print(f" ✔ {method}: (hashed) {get_hashed_value(res).hexdigest()}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getRuntimeVersion'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getStorage'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getStorageAt'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getStorageHash'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getStorageHashAt'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getStorageSize'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_getStorageSizeAt'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_queryStorage'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [['0x'], '0x5c0d1176a568c1f92944340dbfed9e9c530ebca703c85910e7164cb7d1c9e47b'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_queryStorageAt'; is_unsafe = False # weird, but it's actually allowed
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [['0x']])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_subscribeRuntimeVersion'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_subscribeStorage'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [['0x']])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_traceBlock'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x5c0d1176a568c1f92944340dbfed9e9c530ebca703c85910e7164cb7d1c9e47b'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_unsubscribeRuntimeVersion'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)
    
    method = 'state_unsubscribeStorage'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_subscribe(substrate, expect_unsafe_enabled, calls=[]):
    method = 'subscribe_newHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_sync(substrate, expect_unsafe_enabled, calls=[]):
    method = 'sync_state_genSyncSpec'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [True])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)


def scan_module_system(substrate, expect_unsafe_enabled, calls=[]):
    method = 'system_accountNextIndex'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['E7ncQKp4xayUoUdpraxBjT7NzLoayLJA4TuPcKKboBkJ5GH'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_addLogFilter'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_addReservedPeer'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_chain'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_chainType'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_dryRun'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_dryRunAt'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, ['0x'])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_health'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_localListenAddresses'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_localPeerId'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_name'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_nodeRoles'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_peers'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_properties'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_removeReservedPeer'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_reservedPeers'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_resetLogFilter'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_syncState'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_unstable_networkState'; is_unsafe = True
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    method = 'system_version'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

    
def scan_module_unsubscribe(substrate, expect_unsafe_enabled, calls=[]):
    method = 'unsubscribe_newHead'; is_unsafe = False
    calls.append({"method": method, "status": "ok"})
    try:
        print(f" ✔ {method}: {substrate.rpc_request(method, [''])['result']}")
    except Exception as e:
        handle_exception(calls, e, method, is_unsafe, expect_unsafe_enabled)

