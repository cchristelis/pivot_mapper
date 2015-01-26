# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PivotMapper
                                 A QGIS plugin
 Map centre pivots for irrigation.
                             -------------------
        begin                : 2015-01-26
        copyright            : (C) 2015 by Kartoza
        email                : roscoe@Kartoza.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PivotMapper class from file PivotMapper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PivotMapper import PivotMapper
    return PivotMapper(iface)
