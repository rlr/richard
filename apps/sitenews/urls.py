# richard -- video index system
# Copyright (C) 2012 richard contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'sitenews.views',

    # news item
    url(r'entry/(?P<pk>\d+)/(?P<slug>[\w-]*)/?$',
        'news', name='sitenews-news'),

    # news archive for a year
    url(r'archives/(?P<year>[0-9]{4})/?$',
        'news_archive_year', name='sitenews-archive-year'),

    # news listing
    url(r'/?$',
        'news_list', name='sitenews-list'),
)
