* blind_xxe_v1.py
      
      usage: blind_xxe.py [options] <file>

      positional arguments:
        FILE                  Specifies file to exfiltrate using Blind XXE
                              technique.

      optional arguments:
        -h, --help            show this help message and exit
        -l LISTEN, --listen LISTEN
                              Specifies interface address to bind the HTTP server on
                              / listen on. Default: 0.0.0.0 (all interfaces)
        -p PORT, --port PORT  Specifies the port to listen on. Default: 8080
        -r HOST, --rhost HOST
                              Specifies attackers host address where the victim's
                              XML parser should refer while fetching external
                              entities
        -d, --debug           Display debug output.
