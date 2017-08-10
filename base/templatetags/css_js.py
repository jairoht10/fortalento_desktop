from fortalento.settings import STATICFILES_DIRS
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.simple_tag
def bootstrap_min_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/bootstrap/css/bootstrap.min.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def select2_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/select2/select2.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def styles_css():

    archivo = open(STATICFILES_DIRS[0]+"css/styles.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def ionicons_min_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/ionicons-2.0.1/css/ionicons.min.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def buttons_dataTables_min_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/css/buttons.dataTables.min.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def dataTables_bootstrap_min_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/media/css/dataTables.bootstrap.min.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def responsive_bootstrap_min_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Responsive/css/responsive.bootstrap.min.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def buttons_bootstrap_min_css():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/css/buttons.bootstrap.min.css",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def jquery_3_1_1_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/jQuery/jquery-3.1.1.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def bootstrap_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/bootstrap/js/bootstrap.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def select2_full_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/select2/select2.full.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def jquery_mask_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/jquery.mask-1.14.0/jquery.mask.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def ajax_request_js():

    archivo = open(STATICFILES_DIRS[0]+"js/ajax.request.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def jquery_dataTables_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/media/js/jquery.dataTables.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def dataTables_bootstrap_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/media/js/dataTables.bootstrap.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def dataTables_responsive_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Responsive/js/dataTables.responsive.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def dataTables_buttons_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/js/dataTables.buttons.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def buttons_html5_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/js/buttons.html5.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def buttons_flash_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/js/buttons.flash.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def buttons_print_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/js/buttons.print.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def buttons_bootstrap_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/DataTables-1.10.15/extensions/Buttons/js/buttons.bootstrap.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def jszip_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/jszip/jszip.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def pdfmake_min_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/pdfmake/pdfmake.min.js",'r').read()
    return mark_safe(archivo)

@register.simple_tag
def vfs_fonts_js():

    archivo = open(STATICFILES_DIRS[0]+"plugins/pdfmake/vfs_fonts.js",'r').read()
    return mark_safe(archivo)
