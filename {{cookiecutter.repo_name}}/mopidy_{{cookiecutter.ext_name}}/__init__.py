from __future__ import unicode_literals

import logging
import os

# TODO: Remove entirely if you don't register GStreamer elements below
import pygst
pygst.require('0.10')
import gst
import gobject

from mopidy import config, ext, http


__version__ = '{{ cookiecutter.version }}'

# TODO: If you need to log, use loggers named after the current Python module
logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = '{{ cookiecutter.dist_name }}'
    ext_name = '{{ cookiecutter.ext_name }}'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        # TODO: Comment in and edit, or remove entirely
        #schema['username'] = config.String()
        #schema['password'] = config.Secret()
        return schema

    def setup(self, registry):
        # You will typically only implement one of the following things
        # in a single extension.

        # TODO: Edit or remove entirely
        from .frontend import FoobarFrontend
        registry.add('frontend', FoobarFrontend)

        # TODO: Edit or remove entirely
        from .backend import FoobarBackend
        registry.add('backend', FoobarBackend)

        # TODO: Edit or remove entirely
        registry.add('http:routers', ExtensionHTTP)

        # TODO: Edit or remove entirely
        from .mixer import FoobarMixer
        gobject.type_register(FoobarMixer)
        gst.element_register(FoobarMixer, 'foobarmixer', gst.RANK_MARGINAL)

class ExtensionHTTP(http.Router):
    """
    By default it resolves to localhost:6680/{{ cookiecutter.ext_name }}/
    and will server all files under "static_files" folder. If you wish you can
    override setup_routes method and define custom routing. See tornado library
    documentation for more info.
    """
    name = '{{ cookiecutter.ext_name }}'
    path = os.path.join(os.path.dirname(__file__), 'static_files')
        