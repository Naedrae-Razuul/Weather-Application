# Nathaniel Masson
# 4/16/23
#
#
#
#


from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json

city = "City"
state = "State/Reigon"
country = "Country"
global latitude
global longitude
time_zone = "Time Zone"
global last_updated
#global temp_c
temp_f = "112"
condition = "Partly Cloudy"
icon = ""
wind_mph = 6
#global wind_kph
#global gust_mph
#global gust_kph
#global wind_degree
humidity = 64
#global feelslike_c
#global feelslike_f
#global uv_levels
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(-1, -1, 1201, 901))
        self.mainFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setGeometry(QtCore.QRect(200, 30, 261, 191))
        self.frame.setStyleSheet("color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.humidity = QtWidgets.QLabel(self.mainFrame)
        self.humidity.setGeometry(QtCore.QRect(140, 250, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.humidity.setFont(font)
        self.humidity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.humidity.setAutoFillBackground(False)
        self.humidity.setStyleSheet("color: rgb(0, 170, 255);")
        self.humidity.setFrameShape(QtWidgets.QFrame.Box)
        self.humidity.setFrameShadow(QtWidgets.QFrame.Plain)
        self.humidity.setLineWidth(2)
        self.humidity.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.humidity.setObjectName("humidity")
        self.humidity_label = QtWidgets.QLabel(self.mainFrame)
        self.humidity_label.setGeometry(QtCore.QRect(110, 240, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.humidity_label.setFont(font)
        self.humidity_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.humidity_label.setAutoFillBackground(False)
        self.humidity_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.humidity_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.humidity_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.humidity_label.setLineWidth(2)
        self.humidity_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.humidity_label.setObjectName("humidity_label")
        self.wind_label = QtWidgets.QLabel(self.mainFrame)
        self.wind_label.setGeometry(QtCore.QRect(380, 240, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.wind_label.setFont(font)
        self.wind_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wind_label.setAutoFillBackground(False)
        self.wind_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.wind_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wind_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.wind_label.setLineWidth(2)
        self.wind_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.wind_label.setObjectName("wind_label")
        self.wind = QtWidgets.QLabel(self.mainFrame)
        self.wind.setGeometry(QtCore.QRect(350, 250, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.wind.setFont(font)
        self.wind.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wind.setAutoFillBackground(False)
        self.wind.setStyleSheet("color: rgb(0, 170, 255);\n"
"")
        self.wind.setFrameShape(QtWidgets.QFrame.Box)
        self.wind.setFrameShadow(QtWidgets.QFrame.Plain)
        self.wind.setLineWidth(2)
        self.wind.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.wind.setObjectName("wind")
        self.temp = QtWidgets.QLabel(self.mainFrame)
        self.temp.setGeometry(QtCore.QRect(240, 50, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(58)
        self.temp.setFont(font)
        self.temp.setStyleSheet("color: rgb(255, 255, 255);")
        self.temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.condition = QtWidgets.QLabel(self.mainFrame)
        self.condition.setGeometry(QtCore.QRect(210, 140, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.condition.setFont(font)
        self.condition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.condition.setAutoFillBackground(False)
        self.condition.setStyleSheet("color: rgb(255, 255, 255);")
        self.condition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.condition.setFrameShadow(QtWidgets.QFrame.Plain)
        self.condition.setLineWidth(2)
        self.condition.setAlignment(QtCore.Qt.AlignCenter)
        self.condition.setObjectName("condition")
        self.frame_3 = QtWidgets.QFrame(self.mainFrame)
        self.frame_3.setGeometry(QtCore.QRect(750, 60, 401, 251))
        self.frame_3.setStyleSheet("background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.country_edit = QtWidgets.QPlainTextEdit(self.frame_3)
        self.country_edit.setGeometry(QtCore.QRect(10, 10, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.country_edit.setFont(font)
        self.country_edit.setStyleSheet("color: rgb(255, 255, 255);")
        self.country_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.country_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.country_edit.setBackgroundVisible(False)
        self.country_edit.setObjectName("country_edit")
        self.state_edit = QtWidgets.QPlainTextEdit(self.frame_3)
        self.state_edit.setGeometry(QtCore.QRect(10, 90, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.state_edit.setFont(font)
        self.state_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.state_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.state_edit.setObjectName("state_edit")
        self.city_edit = QtWidgets.QPlainTextEdit(self.frame_3)
        self.city_edit.setGeometry(QtCore.QRect(10, 170, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.city_edit.setFont(font)
        self.city_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.city_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.city_edit.setObjectName("city_edit")
        self.img = QtWidgets.QTextBrowser(self.mainFrame)
        self.img.setGeometry(QtCore.QRect(470, 30, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.img.setFont(font)
        self.img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.img.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.img.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img.setObjectName("img")
        self.label = QtWidgets.QLabel(self.mainFrame)
        self.label.setGeometry(QtCore.QRect(750, 320, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.img_2 = QtWidgets.QTextBrowser(self.mainFrame)
        self.img_2.setGeometry(QtCore.QRect(120, 30, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.img_2.setFont(font)
        self.img_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.img_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.img_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_2.setObjectName("img_2")
        self.pushButton = QtWidgets.QPushButton(self.mainFrame)
        self.pushButton.setGeometry(QtCore.QRect(1030, 320, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(126, 126, 126);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.wind.raise_()
        self.frame.raise_()
        self.humidity.raise_()
        self.humidity_label.raise_()
        self.wind_label.raise_()
        self.temp.raise_()
        self.condition.raise_()
        self.frame_3.raise_()
        self.img.raise_()
        self.label.raise_()
        self.img_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def goFunc():
            # save country, state, city text
            try:
                country = self.country_edit.toPlainText()
                state = self.state_edit.toPlainText()
                city = self.city_edit.toPlainText()

                # clear value to ensure it worked properly
                self.country_edit.setPlainText("")
                self.state_edit.setPlainText("")
                self.city_edit.setPlainText("")

                base_url = "http://api.weatherapi.com/v1/current.json?"
                key = "6df2711ec1d74300bb1143444231604"
                city = country + ", " + state + ", " + city + "&aqi=no"
                url = base_url + "key=" + key + "&q=" + city

                response = requests.get(url)
                data = response.json()
                city = data['location']['name']
                state = data['location']['region']
                country = data['location']['country']
                latitude = data['location']['lat']
                longitude = data['location']['lon']
                time_zone = data['location']['tz_id']
                last_updated = data['current']['last_updated']
                temp_c = data['current']['temp_c']
                temp_f = data['current']['temp_f']
                condition = data['current']['condition']['text']
                icon = data['current']['condition']['icon']
                wind_mph = data['current']['wind_mph']
                wind_kph = data['current']['wind_kph']
                gust_mph = data['current']['gust_mph']
                gust_kph = data['current']['gust_kph']
                wind_degree = data['current']['wind_degree']
                humidity = data['current']['humidity']
                feelslike_c = data['current']['feelslike_c']
                feelslike_f = data['current']['feelslike_f']
                uv_levels = data['current']['uv']
                self.humidity.setText(str(humidity) + "%")
                self.wind.setText(str(wind_mph) + " MPH")
                self.temp.setText(str(temp_f))
                self.condition.setText(str(condition))
            except:
                print("")
        self.pushButton.clicked.connect(goFunc)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.humidity.setText(_translate("MainWindow", str(humidity) + "%"))
        self.humidity_label.setText(_translate("MainWindow", "HUMIDITY"))
        self.wind_label.setText(_translate("MainWindow", "WIND"))
        self.wind.setText(_translate("MainWindow", str(wind_mph) + " MPH"))
        self.temp.setText(_translate("MainWindow", str(temp_f)))
        self.condition.setText(_translate("MainWindow", str(condition)))
        self.country_edit.setPlainText(_translate("MainWindow", str(country)))
        self.state_edit.setPlainText(_translate("MainWindow", str(state)))
        self.city_edit.setPlainText(_translate("MainWindow", str(city)))
        self.pushButton.setText(_translate("MainWindow", "Go"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())