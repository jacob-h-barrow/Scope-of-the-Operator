from collections.abc import Mapping
from typing import TypeVar
from supporting.utils import Controlled_UUID

# TypeVars will be covered more later
UUID_Key = TypeVar('U')
Numeric = TypeVar('N')

type AccountMapping = Mapping[UUID_Key, Numeric]

## Use the controlled UUID here
def new_account_2() -> AccountMapping:
    try:
        new_id = uuid_handler.getUuid()
        return {new_id: len(uuid_handler.uuids_given)}
    except:
        raise Exception('No more uuids to give')
