import dns.resolver
import socket

def get_ns_records(domainn):
    try:
        # Resolver los registros NS del dominio
        ns_records = dns.resolver.resolve(domainn, 'NS')
        ns_ips = {}

        for ns in ns_records:
            ns_name = str(ns.target)

            try:
                # Obtener la dirección IP del NS
                ns_ip = socket.gethostbyname(ns_name)
            except socket.gaierror:
                ns_ip = "No IP found"

            ns_ips[ns_name] = ns_ip

        return ns_ips
    except Exception as e:
        return f"Error occurred: {e}"

# Solicitar los NS para un dominio específico
domain = "uniroca.co"  # Cambia esto por el dominio que necesites
ns_ips = get_ns_records(domain)

# Mostrar los resultados
for nss, ip in ns_ips.items():
    print(f"NS: {nss} - IP: {ip}")
