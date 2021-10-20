#! /usr/bin/env python3
#=============================================================================================
# Nombre:       ProxiGG
# Descripción:  Traductor de webs desde consola usando el servicio de Google Traductor.
# Fecha:        19/10/2021 - Ver: 0.1
# Autor:        @as_informatico
#=============================================================================================
import webbrowser
import sys

def _selec_idioma(cod_id):
    # Cargar el listado de idiomas.
    IDIOMAS = ['af','sq','de','am','ar','hy','az','bn','be', 'my','bs','bg','km','kn',
    'ca','ce','cs','ny','zh-CN','si','ko','co','ht','hr','da','sk','sl','es','eo','et',
    'eu','fi','fr','fy','gd','gl','ka','el','gu','ha','haw','iw','hi','hmn','hu','ig',
    'id','en','ga','is','it','ja','jw','kk','rw','ky','ku','lo','la','lv','lt','lb',
    'mk','ml','ms','mg','mt','mi','mr','mn','nl','no','or', 'pa','ps','fa','pl','pt',
    'ro','ru','sm','sr','st','sn','sd','so','sw','sv','su','tl','th','ta','tt','tg','te',
    'tr','tk','uk','ug','ur','uz','vi','xh','yi','yo','zu']

    if cod_id == 'lista':
        _ayuda()
        cod_id = input()

    if cod_id in IDIOMAS:
        return cod_id
    else:
        print('El idioma elegido no existe, introduzca uno válido.\nIntroduzca "lista" para ver los idiomas admitidos.')
        cod_id = input()
        _selec_idioma(cod_id)

def _ayuda():
    # Texto de ayuda al usuario.
    LISTA_IDIOMAS = """
    =============================    A    ===============================\n
    Afrikáans = af, Albanés = sq, Alemán = de, Amhárico = am,\n
    Árabe = ar, Armenio = hy, Azerí = az,\n
    =============================    B    ===============================\n
    Bengalí = bn, Bieloruso = be,Birmano = my, Bosnio = bs, Búlgaro = bg,\n
    =============================    C    ===============================\n
    Camboyano = km, Canarés = kn, Catalán = ca, Cebuano = ce, Checo = cs,\n
    Chichewa = ny, Chino = zh-CN, Cingalés = si, Coreano = ko, Corso = co,\n
    Criollo haitiano = ht, Croata = hr,\n
    =============================    D    ===============================\n
    Danés = da,\n
    =============================    E    ===============================\n
    Eslovaco = sk, Esloveno = sl, Español = es, Esperanto = eo, Estonio = et,\n
    Euskera = eu,\n
    =============================    F    ===============================\n
    Finlandés = fi, Francés = fr, Frisio = fy,\n
    =============================    G    ===============================\n
    Gaelico escocés = gd, Gallego = gl, Georgiano = ka, Griego = el, Gujarati = gu,\n
    =============================    H    ===============================\n
    Hausa = ha, Hawaiano = haw, Hebreo = iw, Hindi = hi, Hmong = hmn, Húngaro = hu,\n
    =============================    I    ===============================\n
    Igbo = ig, Indonesio = id, Inglés = en, Irlandés = ga, Islandés = is,\n
    Italiano = it,\n
    =============================    J    ===============================\n
    Japonés = ja, Javanés = jw,\n
    =============================    K    ===============================\n
    Kazajo = kk, Kinyarwanda = rw, Kirguís = ky, Kurdo = ku,\n
    =============================    L    ===============================\n
    Lao = lo, Latín = la, Letón = lv, Lituano = lt, Luxemburgués = lb,\n
    =============================    M    ===============================\n
    Macedonio = mk, Malayalam = ml, Malayo = ms, Malgache = mg, Maltés = mt,\n
    Maorí = mi, Maratí = mr, Mongol = mn,\n
    =============================    N    ===============================\n
    Neerlandés = nl, Noruego = no,\n
    =============================    O    ===============================\n
    Oriya = or,\n
    =============================    P    ===============================\n
    Panyabí = pa, Pastún = ps, Persa = fa, Polaco = pl, Portugués = pt,\n
    =============================    R    ===============================\n
    Rumano = ro, Ruso = ru,\n
    =============================    S    ===============================\n
    Samoano =sm, Serbio = sr, Sesoto = st, Shona = sn, Sindhi = sd, Somalí = so,\n
    Suajili = sw, Sueco = sv, Sudanés = su,\n
    =============================    T    ===============================\n
    Tagalo = tl, Tailandés = th, Tamil = ta, Tártaro = tt, Tayiko = tg,\n
    Telugu = te, Turco = tr, Turkmeno = tk,\n
    =============================    U    ===============================\n
    Ucraniano = uk, Uigur = ug, Urdu = ur, Uzbeco = uz,\n
    =============================    V    ===============================\n
    Vietnamita = vi,\n
    =============================    X    ===============================\n
    Xhosa = xh,\n
    =============================    Y    ===============================\n
    Yidis = yi, Yoruba = yo,\n
    =============================    Z    ===============================\n
    Zulú = zu,\n

    Introduzca ahora el código del idioma..."""
    print(LISTA_IDIOMAS)
    return

if len(sys.argv) > 1:
    web = str(sys.argv[1])
    x1 = str(sys.argv[2])
    x2 = str(sys.argv[3])
else:
    # Introducir la web a visitar.
    print('Introduzca dirección web:')
    web = input()
    # Introducir el idioma de origen de la página.
    print('Introduzca idioma ORIGEN (es = español, en = inglés, etc.) o "lista" para ver los idiomas admitidos.')
    x = input()
    x1 = str(_selec_idioma(x))
    # Introducir el idioma de destino de la página.
    print('Introduzca idioma DESTINO (es = español, en = inglés, etc.) o "lista" para ver los idiomas admitidos.')
    x = input()
    x2 = str(_selec_idioma(x))

# Dar a la cadena el formato esperado por Google.
web = web.replace('.','-')
CAB_ELIM = ['http://','https://']
for n in CAB_ELIM:
    web = web.replace(n, '')
web = web.split('/', 1)
if len(web) > 1:
    web = 'https://' + web[0] + '.translate.goog/' + web[1] + '?_x_tr_sl=' + x1 + '&_x_tr_hl=' + x2 + '&_x_tr_tl=' + x2
else:
    web = 'https://' + web[0] + '.translate.goog/?_x_tr_sl=' + x1 + '&_x_tr_hl=' + x2 + '&_x_tr_tl=' + x2

# Abrir el navegador con la web traducida.
webbrowser.open(web, new = 1, autoraise = True)
exit
