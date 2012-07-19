from cmsplugin_codebragger.models import CodebraggerProjectTeaser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mycode.models import Project

class CodebraggerProjectTeaserPlugin(CMSPluginBase):
    module = 'CodeBragger'
    model = CodebraggerProjectTeaser
    name = _("Codebragger Project Teaser")
    render_template = "codebragger/cmsplugins/project_teaser.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'project': instance.project,
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + u"cms/images/plugins/image.png"
    
plugin_pool.register_plugin(CodebraggerProjectTeaserPlugin)
