patterns = {'IPv4': 'HERE'}

@dataclass
class IP:
    addr: str
    type: str

    def __post_init__(self):
        try:
            if not re.search(self.addr, patterns[self.type]):
                raise Exception(f'{self.type} not supported!')
        except Exception as e:
            raise Exception(f'An exception was raised: {e}')
        
@dataclass 
class Connection:
    id: str
    exec_name: str
    local_addr: IP
    pid: str
    remote_addr: IP
    state: str
    uid: UUID 

    def __post_init__(self):
        if not isinstance(self.uid, UUID):
            raise Exception(f'{self.uid} isnt the right type')
        
class Netstat:
    ...

class IpStatHandler:
    ...

type Netstat_Handlers = Tuple[Netstat, ...]
type Connections = Tuple[Connection, ...]

# Better
type Overlay[T] = Tuple[T, ...]
        
class ConnectionScraper(Protocol):
    # Good for fusing multiple system pictures together
    def __call__(self, *overlays: Overlay[Netstat], maxlen: Optional[None]=None) -> Overlay[Connection]:
        ...

def batch_bpf(netstat_overlay: IpStatHandler, max_amount: Optional[int]=None) -> Netstat:
    ...

def connection_callback(*overlays: Overlay[Netstat], maxlen: Optional[None]=None) -> Overlay[Connection]:
    ...
