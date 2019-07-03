tag_dict = {'odoo': ('odoo',),
            'bootstrap': ('bootstrap', 'css', 'hmtl',),
            'django': ('django',),
            'docker': ('docker', 'containers',),
            'favicon': ('favicon',),
            'jdbc': ('java', 'jdbc', 'oracle'),
            'jquery': ('jquery', 'javascript',),
            'key': ('key', 'public key',),
            'kubernetes': ('kubernetes', 'containers',),
            'legal': ('ley', 'legal', 'código civil',),
            'linux': ('linux',),
            'mariadb': ('mysql', 'mariadb',),
            'mysql': ('mysql', 'mariadb',),
            'otn': ('otn', 'oracle',),
            'python': ('python',),
            'reddit': ('reddit',),
            'rest': ('servicios', 'rest',),
            'spring': ('spring', 'java',),
            'ssh': ('ssh',),
            'stackoverflow': ('stackoverflow',),
            'ubuntu': ('linux', 'ubuntu',),
            }


def leer_tags(cadenas):
    tags = []
    for cadena in cadenas:
        for key, value in tag_dict.items():
            if key.lower() in cadena.lower():
                for tag in value:
                    tags.append(tag)
    return set(tags)
