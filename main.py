from sockpuppet import VpnApp, VpnConfig
from sockpuppet.backend import SensibleDefaultBackend

if __name__ == "__main__":
    cfg = VpnConfig.load()
    backend = SensibleDefaultBackend(cfg.name, cfg.host, cfg.port)
    VpnApp(backend).run()
