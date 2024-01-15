def crear_entrada_m3u(nombre, url, tvg_id, group_title):
    return f"#EXTINF:0 tvg-id=\"{tvg_id}\" group-title=\"{group_title}\",{nombre}\n{url}\n"

def generar_lista_m3u(canales):
    lista_m3u = "#EXTM3U\n"
    for canal in canales:
        lista_m3u += crear_entrada_m3u(**canal)
    return lista_m3u

# Ejemplo de lista de canales
canales_ejemplo = [
    {"nombre": "Conecta TV ✪ | MX", "url": "https://stream8.mexiserver.com:1936/conectatv/conectatv/playlist.m3u8?PlaylistM3UCL", "tvg_id": "ext", "group_title": "Channels"},
    {"nombre": "Mundo de la Musica TV ✪ | CL", "url": "https://tv.streaming-chile.com:1936/mundodelamusicatv/mundodelamusicatv/playlist.m3u8?PlaylistM3UCL", "tvg_id": "ext", "group_title": "Channels"},
    # ... Agrega más canales según sea necesario
]

# Generar la lista M3U
lista_generada = generar_lista_m3u(canales_ejemplo)

# Puedes imprimir o guardar la lista generada
print(lista_generada)
