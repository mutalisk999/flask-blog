# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import hashlib

try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for, current_app


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def calc_md5(data):
    return hashlib.md5(data).hexdigest()


def is_image_jpg_or_jpeg(data):
    return len(data) >= 11 \
           and data[:4] == b'\xff\xd8\xff\xe0' \
           and data[6:11] == b'\x4a\x46\x49\x46\x00'


def is_image_png(data):
    return len(data) >= 6 \
           and data[0:6] == b'\x89\x50\x4e\x47\x0d\x0a'


def is_image_gif(data):
    return len(data) >= 6 and data[0:6] == b'\x47\x49\x46\x38\x39\x61'


def allowed_file_size(data):
    return len(data) <= current_app.config['FLASK_BLOG_ALLOWED_IMAGE_SIZE']


def allowed_file(filename, data):
    if '.' not in filename:
        return False
    file_ext = filename.rsplit('.', 1)[1].lower()
    if file_ext not in current_app.config['FLASK_BLOG_ALLOWED_IMAGE_EXTENSIONS']:
        return False
    if file_ext in ('jpg', 'jpeg') and not is_image_jpg_or_jpeg(data):
        return False
    if file_ext == 'png' and not is_image_png(data):
        return False
    if file_ext == 'gif' and not is_image_gif(data):
        return False
    return True
