from vpn import VpnApp, VpnConfig
from vpn.backend import SensibleDefaultBackend

if __name__ == "__main__":
    cfg = VpnConfig.load()
    backend = SensibleDefaultBackend(cfg.name, cfg.host, cfg.port)
    VpnApp(backend).run()
