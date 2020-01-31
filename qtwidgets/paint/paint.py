import sys
if 'PyQt5' in sys.modules:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtCore import Qt

else:
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2.QtCore import Qt


class Paint(QtWidgets.QLabel):

    def __init__(self, width, height, background='white', *args, **kwargs):
        super().__init__(*args, **kwargs)
        pixmap = QtGui.QPixmap(width, height)
        self.setPixmap(pixmap)

        # Fill the canvas with the initial color.
        painter = QtGui.QPainter(self.pixmap())
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(background))
        brush.setStyle(Qt.SolidPattern)
        painter.fillRect(0, 0, pixmap.width(), pixmap.height(), brush)
        painter.end()

        self.last_x, self.last_y = None, None
        self._pen_color = QtGui.QColor('#000000')
        self._pen_width = 4

    def setPenColor(self, c):
        self._pen_color = QtGui.QColor(c)

    def setPenWidth(self, w):
        self._pen_width = int(w)

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  #  Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(self._pen_width)
        p.setColor(self._pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            self._flood_fill_from_event(e)

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def _flood_fill_from_event(self, e):

        image = self.pixmap().toImage()
        w, h = image.width(), image.height()
        x, y = e.x(), e.y()

        # Get our target color from origin.
        target_color = image.pixel(x, y)

        have_seen = set()
        queue = [(x, y)]

        def get_cardinal_points(have_seen, center_pos):
            points = []
            cx, cy = center_pos
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                xx, yy = cx + x, cy + y
                if (xx >= 0 and xx < w and
                            yy >= 0 and yy < h and
                            (xx, yy) not in have_seen):
                    points.append((xx, yy))
                    have_seen.add((xx, yy))

            return points

        # Now perform the search and fill.
        p = QtGui.QPainter(self.pixmap())
        p.setPen(QtGui.QPen(self._pen_color))

        while queue:
            x, y = queue.pop()
            if image.pixel(x, y) == target_color:
                p.drawPoint(QtCore.QPoint(x, y))
                queue.extend(get_cardinal_points(have_seen, (x, y)))

        self.update()
