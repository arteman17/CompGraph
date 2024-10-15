import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSlider, QColorDialog, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class ColorConverter(QWidget):
    def __init__(self):
        super().__init__()

        # Настройка интерфейса
        self.setWindowTitle("Цветовые модели: RGB, CMYK, HLS")

        # Основные компоненты
        self.rgb_label = QLabel("RGB: ")
        self.cmyk_label = QLabel("CMYK: ")
        self.hls_label = QLabel("HLS: ")

        self.r_input = QLineEdit()
        self.g_input = QLineEdit()
        self.b_input = QLineEdit()

        self.c_input = QLineEdit()
        self.m_input = QLineEdit()
        self.y_input = QLineEdit()
        self.k_input = QLineEdit()

        self.h_input = QLineEdit()
        self.l_input = QLineEdit()
        self.s_input = QLineEdit()


        self.rgb_slider_r = QSlider(Qt.Horizontal)
        self.rgb_slider_g = QSlider(Qt.Horizontal)
        self.rgb_slider_b = QSlider(Qt.Horizontal)

        self.cmyk_slider_c = QSlider(Qt.Horizontal)
        self.cmyk_slider_m = QSlider(Qt.Horizontal)
        self.cmyk_slider_y = QSlider(Qt.Horizontal)
        self.cmyk_slider_k = QSlider(Qt.Horizontal)

        self.hsl_slider_h = QSlider(Qt.Horizontal)
        self.hsl_slider_s = QSlider(Qt.Horizontal)
        self.hsl_slider_l = QSlider(Qt.Horizontal)

        # Ползунки для RGB
        self.rgb_slider_r.setRange(0, 255)
        self.rgb_slider_g.setRange(0, 255)
        self.rgb_slider_b.setRange(0, 255)

        self.cmyk_slider_c.setRange(0, 100)
        self.cmyk_slider_m.setRange(0, 100)
        self.cmyk_slider_y.setRange(0, 100)
        self.cmyk_slider_k.setRange(0, 100)

        self.hsl_slider_h.setRange(0, 100)
        self.hsl_slider_s.setRange(0, 100)
        self.hsl_slider_l.setRange(0, 100)

        self.color_picker_button = QPushButton("Выбрать цвет")

        # Слоты и сигналы
        self.rgb_slider_r.valueChanged.connect(self.update_color_from_rgb_sliders)
        self.rgb_slider_g.valueChanged.connect(self.update_color_from_rgb_sliders)
        self.rgb_slider_b.valueChanged.connect(self.update_color_from_rgb_sliders)

        self.cmyk_slider_c.valueChanged.connect(self.update_color_from_cmyk_sliders)
        self.cmyk_slider_m.valueChanged.connect(self.update_color_from_cmyk_sliders)
        self.cmyk_slider_y.valueChanged.connect(self.update_color_from_cmyk_sliders)
        self.cmyk_slider_k.valueChanged.connect(self.update_color_from_cmyk_sliders)

        self.hsl_slider_h.valueChanged.connect(self.update_color_from_hls_sliders)
        self.hsl_slider_s.valueChanged.connect(self.update_color_from_hls_sliders)
        self.hsl_slider_l.valueChanged.connect(self.update_color_from_hls_sliders)

        self.r_input.textChanged.connect(self.rgb_input_changed)
        self.g_input.textChanged.connect(self.rgb_input_changed)
        self.b_input.textChanged.connect(self.rgb_input_changed)

        self.c_input.textChanged.connect(self.cmyk_input_changed)
        self.m_input.textChanged.connect(self.cmyk_input_changed)
        self.y_input.textChanged.connect(self.cmyk_input_changed)
        self.k_input.textChanged.connect(self.cmyk_input_changed)

        self.h_input.textChanged.connect(self.hls_input_changed)
        self.s_input.textChanged.connect(self.hls_input_changed)
        self.l_input.textChanged.connect(self.hls_input_changed)

        self.color_picker_button.clicked.connect(self.open_color_picker)

        # Основной интерфейс
        layout = QVBoxLayout()

        sliders_layout = QVBoxLayout()
        sliders_layout.addWidget(self.rgb_label)
        r_layout = QHBoxLayout()
        r_layout.addWidget(QLabel("Red"))
        r_layout.addWidget(self.r_input)
        sliders_layout.addLayout(r_layout)
        sliders_layout.addWidget(self.rgb_slider_r)
        g_layout = QHBoxLayout()
        g_layout.addWidget(QLabel("Green"))
        g_layout.addWidget(self.g_input)
        sliders_layout.addLayout(g_layout)
        sliders_layout.addWidget(self.rgb_slider_g)
        b_layout = QHBoxLayout()
        b_layout.addWidget(QLabel("Blue"))
        b_layout.addWidget(self.b_input)
        sliders_layout.addLayout(b_layout)
        sliders_layout.addWidget(self.rgb_slider_b)

        sliders_layout.addWidget(self.cmyk_label)
        c_layout = QHBoxLayout()
        c_layout.addWidget(QLabel("Cyan"))
        c_layout.addWidget(self.c_input)
        sliders_layout.addLayout(c_layout)
        sliders_layout.addWidget(self.cmyk_slider_c)
        m_layout = QHBoxLayout()
        m_layout.addWidget(QLabel("Magenta"))
        m_layout.addWidget(self.m_input)
        sliders_layout.addLayout(m_layout)
        sliders_layout.addWidget(self.cmyk_slider_m)
        y_layout = QHBoxLayout()
        y_layout.addWidget(QLabel("Yellow"))
        y_layout.addWidget(self.y_input)
        sliders_layout.addLayout(y_layout)
        sliders_layout.addWidget(self.cmyk_slider_y)
        k_layout = QHBoxLayout()
        k_layout.addWidget(QLabel("Black"))
        k_layout.addWidget(self.k_input)
        sliders_layout.addLayout(k_layout)
        sliders_layout.addWidget(self.cmyk_slider_k)

        sliders_layout.addWidget(self.hls_label)
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel("Hue"))
        h_layout.addWidget(self.h_input)
        sliders_layout.addLayout(h_layout)
        sliders_layout.addWidget(self.hsl_slider_h)
        s_layout = QHBoxLayout()
        s_layout.addWidget(QLabel("Saturation"))
        s_layout.addWidget(self.s_input)
        sliders_layout.addLayout(s_layout)
        sliders_layout.addWidget(self.hsl_slider_s)
        l_layout = QHBoxLayout()
        l_layout.addWidget(QLabel("Lightness"))
        l_layout.addWidget(self.l_input)
        sliders_layout.addLayout(l_layout)
        sliders_layout.addWidget(self.hsl_slider_l)
        self.color_window = QLabel()
        # self.color_window.setFixedHeight

        layout.addLayout(sliders_layout)
        layout.addWidget(self.color_window)
        layout.addWidget(self.color_picker_button)

        self.setLayout(layout)
        self.update_ui()

    def update_ui(self):
        # Изначальный цвет
        self.set_color(255, 255, 255)  # Белый по умолчанию

    def set_color(self, r, g, b):
        self.block_signals(True)
        color = QColor(r, g, b)
        self.update_rgb_inputs(color)
        self.update_cmyk_inputs(color)
        self.update_hls_inputs(color)
        self.block_signals(False)
        self.color_window.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def set_color_rgb(self, r, g, b):
        self.block_signals(True)
        color = QColor(r, g, b)
        self.update_cmyk_inputs(color)
        self.update_hls_inputs(color)
        self.block_signals(False)
        self.color_window.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def set_color_cmyk(self, r, g, b):
        self.block_signals(True)
        color = QColor(r, g, b)
        self.update_rgb_inputs(color)
        self.update_hls_inputs(color)
        self.block_signals(False)
        self.color_window.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def set_color_hls(self, r, g, b):
        self.block_signals(True)
        color = QColor(r, g, b)
        self.update_rgb_inputs(color)
        self.update_cmyk_inputs(color)
        self.block_signals(False)
        self.color_window.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def block_signals(self, block):
        self.rgb_slider_r.blockSignals(block)
        self.rgb_slider_g.blockSignals(block)
        self.rgb_slider_b.blockSignals(block)

        self.cmyk_slider_c.blockSignals(block)
        self.cmyk_slider_m.blockSignals(block)
        self.cmyk_slider_y.blockSignals(block)
        self.cmyk_slider_k.blockSignals(block)

        self.hsl_slider_h.blockSignals(block)
        self.hsl_slider_s.blockSignals(block)
        self.hsl_slider_l.blockSignals(block)

    def update_rgb_inputs(self, color):
        self.r_input.setText(f"{color.red()}")
        self.g_input.setText(f"{color.green()}")
        self.b_input.setText(f"{color.blue()}")

        self.rgb_slider_r.setValue(color.red())
        self.rgb_slider_g.setValue(color.green())
        self.rgb_slider_b.setValue(color.blue())

    def update_cmyk_inputs(self, color):
        cmyk = color.toCmyk()
        self.c_input.setText(f"{cmyk.cyanF():.2f}")
        self.m_input.setText(f"{cmyk.magentaF():.2f}")
        self.y_input.setText(f"{cmyk.yellowF():.2f}")
        self.k_input.setText(f"{cmyk.blackF():.2f}")
        self.cmyk_slider_c.setValue(int(cmyk.cyanF() * 100))
        self.cmyk_slider_m.setValue(int(cmyk.magentaF() * 100))
        self.cmyk_slider_y.setValue(int(cmyk.yellowF() * 100))
        self.cmyk_slider_k.setValue(int(cmyk.blackF() * 100))


    def update_hls_inputs(self, color):
        hls = color.toHsl()
        self.h_input.setText(f"{hls.hueF():.2f}")
        self.s_input.setText(f"{hls.saturationF():.2f}")
        self.l_input.setText(f"{hls.lightnessF():.2f}")

        self.hsl_slider_h.setValue(int(color.hueF() * 100))
        self.hsl_slider_l.setValue(int(color.lightnessF() * 100))
        self.hsl_slider_s.setValue(int(color.saturationF() * 100))

    def update_color_from_rgb_sliders(self):
        r = self.rgb_slider_r.value()
        g = self.rgb_slider_g.value()
        b = self.rgb_slider_b.value()
        self.r_input.setText(f"{r}")
        self.g_input.setText(f"{g}")
        self.b_input.setText(f"{b}")
        self.set_color_rgb(r, g, b)

    def update_color_from_cmyk_sliders(self):
        c = self.cmyk_slider_c.value() / 100
        m = self.cmyk_slider_m.value() / 100
        y = self.cmyk_slider_y.value() / 100
        k = self.cmyk_slider_k.value() / 100
        self.c_input.setText(f"{c:.2f}")
        self.m_input.setText(f"{m:.2f}")
        self.y_input.setText(f"{y:.2f}")
        self.k_input.setText(f"{k:.2f}")
        rgb = QColor.fromCmykF(c, m, y, k)
        self.set_color_cmyk(rgb.red(), rgb.green(), rgb.blue())

    def update_color_from_hls_sliders(self):
        h = self.hsl_slider_h.value() / 100
        l = self.hsl_slider_l.value() / 100
        s = self.hsl_slider_s.value() / 100
        self.h_input.setText(f"{h:.2f}")
        self.s_input.setText(f"{s:.2f}")
        self.l_input.setText(f"{l:.2f}")
        rgb = QColor.fromHslF(h, s, l)
        self.set_color_hls(rgb.red(), rgb.green(), rgb.blue())

    def rgb_input_changed(self):
        r = int(self.r_input.text())
        g = int(self.g_input.text())
        b = int(self.b_input.text())
        self.rgb_slider_r.setValue(r)
        self.rgb_slider_g.setValue(g)
        self.rgb_slider_b.setValue(b)

    def cmyk_input_changed(self):
        c = float(self.c_input.text())
        m = float(self.m_input.text())
        y = float(self.y_input.text())
        k = float(self.k_input.text())
        self.cmyk_slider_c.setValue(int(c * 100))
        self.cmyk_slider_m.setValue(int(m * 100))
        self.cmyk_slider_y.setValue(int(y * 100))
        self.cmyk_slider_k.setValue(int(k * 100))
        rgb = QColor.fromCmykF(c, m, y, k)

    def hls_input_changed(self):
        h = float(self.h_input.text())
        s = float(self.s_input.text())
        l = float(self.l_input.text())
        self.hsl_slider_h.setValue(int(h * 100))
        self.hsl_slider_s.setValue(int(s * 100))
        self.hsl_slider_l.setValue(int(l * 100))
        rgb = QColor.fromHslF(h, s, l)

    def open_color_picker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.set_color(color.red(), color.green(), color.blue())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorConverter()
    window.setFixedSize(900, 700)
    window.show()
    sys.exit(app.exec_())
